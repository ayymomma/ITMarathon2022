package com.otp.otpserver.model.pojo.dto.application;

import com.otp.otpserver.model.pojo.dto.version.VersionOnlyName;
import com.otp.otpserver.model.pojo.erd.Application;
import lombok.Data;

import javax.persistence.Column;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import java.util.List;

@Data
public class ApplicationMaximal {
    private Integer appId;
    private String appName;
    private List<VersionOnlyName> versions;

    public ApplicationMaximal(Application app, List<VersionOnlyName> versions){
        this.appId = app.getAppId();
        this.appName = app.getAppName();
        this.versions = versions;
    }
}
