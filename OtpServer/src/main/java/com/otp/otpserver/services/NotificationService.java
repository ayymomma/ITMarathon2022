package com.otp.otpserver.services;

import com.otp.otpserver.model.pojo.erd.UpdateNotification;

public interface NotificationService {

    void addUpdateNotification(UpdateNotification notificationRequest);
}
