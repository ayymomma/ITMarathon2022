package com.otp.otpserver.services;

import com.otp.otpserver.model.pojo.dto.device.DeviceRequest;
import com.otp.otpserver.model.pojo.erd.Device;
import com.otp.otpserver.model.pojo.erd.DeviceSession;

import java.util.List;

public interface DeviceService {
    Device addDevice(DeviceRequest deviceRequest, Integer userId);

    List<Device> getAllDevicesOfUser(Integer userId);

    DeviceSession connectDevice(String deviceId);

    DeviceSession keepAlive(String deviceId);

    Device getDeviceOfId(String deviceId);

    DeviceSession disconnectDevice(String deviceId);
}
