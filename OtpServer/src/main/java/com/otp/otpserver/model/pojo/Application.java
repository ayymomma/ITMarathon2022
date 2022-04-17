package com.otp.otpserver.model.pojo;

import lombok.Data;

import javax.persistence.*;

@Data
@Entity
@Table(name = "APPLICATIONS")
public class Application {
    @Id
    @GeneratedValue
    @Column(name = "APP_ID", nullable = false)
    private Integer appId;

    @Column(name = "APP_NAME", nullable = false)
    private String appName;

    @Column(name = "APP_PATH")
    private String appPath;


}