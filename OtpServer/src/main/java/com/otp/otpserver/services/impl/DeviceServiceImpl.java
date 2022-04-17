package com.otp.otpserver.services.impl;

import com.otp.otpserver.model.dao.DeviceRepository;
import com.otp.otpserver.model.dao.DeviceSessionRepository;
import com.otp.otpserver.model.exception.HttpResponseException;
import com.otp.otpserver.model.pojo.dto.device.DeviceRequest;
import com.otp.otpserver.model.pojo.erd.Device;
import com.otp.otpserver.model.pojo.erd.DeviceSession;
import com.otp.otpserver.model.pojo.erd.User;
import com.otp.otpserver.services.DeviceService;
import com.otp.otpserver.services.UserService;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;

import java.sql.Timestamp;
import java.util.List;
import java.util.Optional;

@Service
public class DeviceServiceImpl implements DeviceService {

    private final DeviceRepository deviceRepository;
    private final UserService userService;
    private final DeviceSessionRepository deviceSessionRepository;

    public DeviceServiceImpl(DeviceRepository deviceRepository, UserService userService, DeviceSessionRepository deviceSessionRepository) {
        this.deviceRepository = deviceRepository;
        this.userService = userService;
        this.deviceSessionRepository = deviceSessionRepository;
    }

    @Override
    public Device addDevice(DeviceRequest deviceRequest, Integer userId) {
        // Check if device with same name for userid
        User existUser = userService.getUserById(userId);

        if(existUser == null)
            throw new HttpResponseException("User not found!", HttpStatus.NOT_FOUND);

        Device exists = deviceRepository.findByDeviceNameAndUserUserId(deviceRequest.getDeviceName(), userId);

        if(exists != null)
            throw new HttpResponseException("A device with this name already exists!", HttpStatus.CONFLICT);


        Device newDevice = new Device();
        newDevice.setDeviceName(deviceRequest.getDeviceName());
        newDevice.setUser(existUser);
        newDevice.setDeviceId(null);

        deviceRepository.save(newDevice);

        return newDevice;
    }

    @Override
    public List<Device> getAllDevicesOfUser(Integer userId) {
        // It exist
        User user = userService.getUserById(userId);

        return (List<Device>) deviceRepository.findAllByUserUserId(userId);
    }

    @Override
    public DeviceSession connectDevice(Integer deviceId) {

        // Check if device exists
        Optional<Device> exists = deviceRepository.findById(deviceId);

        if(exists.isEmpty())
            throw new HttpResponseException("Device not found!", HttpStatus.NOT_FOUND);

        Device device = exists.get();

        // Save session into database
        // Check if session exists
        DeviceSession deviceSession = deviceSessionRepository.findByDeviceId(deviceId);

        if(deviceSession != null){
            // Delete old session
            deviceSessionRepository.delete(deviceSession);
        }

        // Add new session
        deviceSession = new DeviceSession();
        deviceSession.setDeviceId(deviceId);
        deviceSession.setTimestamp(new Timestamp(System.currentTimeMillis()));


        return deviceSessionRepository.save(deviceSession);
    }

    @Override
    public DeviceSession keepAlive(Integer deviceId) {

        // Check if device exists
        Optional<Device> exists = deviceRepository.findById(deviceId);

        if(exists.isEmpty())
            throw new HttpResponseException("Device not found!", HttpStatus.NOT_FOUND);

        Device device = exists.get();

        // Check if session exists
        DeviceSession deviceSession = deviceSessionRepository.findByDeviceId(deviceId);

        if(deviceSession == null)
            throw new HttpResponseException("Device is not online!", HttpStatus.NOT_FOUND);

        // Update timestamp
        deviceSession.setTimestamp(new Timestamp(System.currentTimeMillis()));

        return deviceSessionRepository.save(deviceSession);
    }
}
