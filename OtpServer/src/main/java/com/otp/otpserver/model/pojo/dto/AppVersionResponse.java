package com.otp.otpserver.model.pojo.dto;

import com.otp.otpserver.model.pojo.erd.Version;
import lombok.Data;

import java.util.List;

@Data
public class AppVersionResponse {

    private String appName;
    private List<VersionResponse> newVersions;
}
