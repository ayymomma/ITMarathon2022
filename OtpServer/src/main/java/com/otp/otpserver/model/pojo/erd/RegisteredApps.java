package com.otp.otpserver.model.pojo.erd;

import lombok.Data;

import javax.persistence.*;

@Data
@Entity
@Table(name = "DEVICE_APPS")
public class RegisteredApps {
    @Id
    @GeneratedValue
    @Column(name = "DEVICE_APP_ID", nullable = false)
    private Integer deviceAppId;

    @Column(name = "DEVICE_ID", nullable = false)
    private String deviceId;

    @Column(name = "APP_NAME", nullable = false)
    private String appName;

    @Column(name = "VERSION_NAME", nullable = false)
    private String versionName;
}