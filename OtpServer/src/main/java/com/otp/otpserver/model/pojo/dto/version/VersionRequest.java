package com.otp.otpserver.model.pojo.dto.version;

import lombok.Data;

@Data
public class VersionRequest {
    private String versionName;
    private String appPath;
}
