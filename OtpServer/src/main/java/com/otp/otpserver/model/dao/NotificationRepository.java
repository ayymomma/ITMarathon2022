package com.otp.otpserver.model.dao;

import com.otp.otpserver.model.pojo.erd.UpdateNotification;
import org.hibernate.sql.Update;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface NotificationRepository extends CrudRepository<UpdateNotification, Integer> {

    List<UpdateNotification> findAllByDeviceId(String deviceId);

}
