package com.otp.otpserver.model.pojo.dto.application;

import com.otp.otpserver.model.pojo.erd.Application;
import lombok.Data;

import java.io.Serializable;

@Data
public class ApplicationNoId implements Serializable {
    private String appName;

    public Application toApplicationErd(){
        Application app = new Application();
        app.setAppId(null);
        app.setAppName(appName);
        return app;
    }
}
