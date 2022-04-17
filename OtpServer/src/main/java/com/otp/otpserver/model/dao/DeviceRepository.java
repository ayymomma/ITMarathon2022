package com.otp.otpserver.model.dao;

import com.otp.otpserver.model.pojo.erd.Application;
import com.otp.otpserver.model.pojo.erd.Device;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface DeviceRepository extends CrudRepository<Device, String> {
    Device findByDeviceIdAndUserUserId(String deviceId, Integer userId);
    List<Device> findAllByUserUserId(Integer userId);
}
