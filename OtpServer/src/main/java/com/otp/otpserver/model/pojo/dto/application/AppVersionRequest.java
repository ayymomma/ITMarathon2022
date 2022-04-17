package com.otp.otpserver.model.pojo.dto.application;

import lombok.Data;

@Data
public class AppVersionRequest {

    private String appName;
    private String versionName;
}
