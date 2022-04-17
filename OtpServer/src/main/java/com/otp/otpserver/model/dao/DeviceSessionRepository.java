package com.otp.otpserver.model.dao;

import com.otp.otpserver.model.pojo.erd.DeviceSession;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface DeviceSessionRepository extends CrudRepository<DeviceSession, Integer> {
    DeviceSession findByDeviceId(String deviceId);
}
