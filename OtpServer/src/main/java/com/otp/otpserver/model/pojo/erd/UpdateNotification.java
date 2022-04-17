package com.otp.otpserver.model.pojo.erd;

import lombok.Data;

import javax.persistence.*;

@Data
@Entity
@Table(name = "NOTIFICATION")
public class UpdateNotification {
    @Id
    @GeneratedValue
    @Column(name = "NOTIFICATION_ID", nullable = false)
    private Integer notificationId;

    @Column(name = "DEVICE_ID", nullable = false)
    private String deviceId;

    @Column(name = "VERSION_NAME", nullable = false)
    private String versionName;

    @Column(name = "APP_NAME", nullable = false)
    private String appName;

}