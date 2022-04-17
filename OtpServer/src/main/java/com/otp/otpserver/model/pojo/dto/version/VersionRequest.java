package com.otp.otpserver.model.pojo.dto.version;

import lombok.Data;

import java.time.LocalDate;

@Data
public class VersionRequest {
    private String versionName;
}
