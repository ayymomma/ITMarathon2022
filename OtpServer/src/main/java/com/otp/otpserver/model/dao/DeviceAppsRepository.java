package com.otp.otpserver.model.dao;

import com.otp.otpserver.model.pojo.erd.LoginToken;
import com.otp.otpserver.model.pojo.erd.RegisteredApps;
import org.springframework.data.repository.CrudRepository;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

public interface DeviceAppsRepository extends CrudRepository<RegisteredApps, Integer> {

    @Transactional
    void deleteAllByDeviceId(String deviceId);

    List<RegisteredApps> findAllByDeviceId(String deviceId);

    List<RegisteredApps> findByDeviceIdAndAppNameAndVersionName(String deviceId, String appName, String versionName);
}
