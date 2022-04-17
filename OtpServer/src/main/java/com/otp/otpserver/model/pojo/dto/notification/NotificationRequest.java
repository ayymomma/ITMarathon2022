package com.otp.otpserver.model.pojo.dto.notification;

import lombok.Data;

@Data
public class NotificationRequest {

    private String deviceId;

    private String versionName;

    private String appName;
}
