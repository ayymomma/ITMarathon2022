package com.otp.otpserver.model.pojo.erd;

import lombok.Data;

import javax.persistence.*;

@Data
@Entity
@Table(name = "USERS")
public class User {
    @Id
    @GeneratedValue
    @Column(name = "USER_ID", nullable = false)
    private Integer userId;

    @Column(name = "USERNAME", nullable = false)
    private String username;

    @Column(name = "PASSWORD", nullable = false)
    private String password;

    @Column(name = "ROLE", nullable = false)
    private String role;

}