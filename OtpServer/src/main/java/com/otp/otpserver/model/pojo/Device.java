package com.otp.otpserver.model.pojo;

import lombok.Data;

import javax.persistence.*;

@Data
@Entity
@Table(name = "DEVICES")
public class Device {
    @Id
    @GeneratedValue
    @Column(name = "DEVICE_ID", nullable = false)
    private Long deviceId;

    @Column(name = "DEVICE_NAME", nullable = false)
    private String deviceName;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "USER_ID")
    private User user;
}