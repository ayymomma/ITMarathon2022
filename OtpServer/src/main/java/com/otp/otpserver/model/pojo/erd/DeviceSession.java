package com.otp.otpserver.model.pojo.erd;

import lombok.Data;

import javax.persistence.*;
import java.sql.Timestamp;

@Data
@Entity
@Table(name = "SESSIONS")
public class DeviceSession {
    @Id
    @GeneratedValue
    @Column(name = "SESSION_ID", nullable = false)
    private Integer sessionId;

    @Column(name = "DEVICE_ID", nullable = false)
    private Integer deviceId;

    @Column(name = "TIMESTAMP", nullable = false)
    private Timestamp timestamp;

}