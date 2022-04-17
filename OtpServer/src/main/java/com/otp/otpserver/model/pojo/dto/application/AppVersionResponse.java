package com.otp.otpserver.model.pojo.dto.application;

import com.otp.otpserver.model.pojo.dto.version.VersionResponse;
import lombok.Data;

import java.util.List;

@Data
public class AppVersionResponse {

    private String appName;
    private List<VersionResponse> newVersions;
}
