package com.otp.otpserver.model.pojo.erd;

import lombok.Data;

import javax.persistence.*;
import java.sql.Timestamp;

@Data
@Entity
@Table(name = "TOKENS")
public class LoginToken {
    @Id
    @Column(name = "TOKEN", nullable = false, unique = true)
    private String token;

    @Column(name = "USER_ID", nullable = false)
    private Integer userId;

    @Column(name = "TIMESTAMP", nullable = false)
    private Timestamp timestamp;
}