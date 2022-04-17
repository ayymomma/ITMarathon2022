package com.otp.otpserver.model.pojo.dto.version;

import com.otp.otpserver.model.pojo.erd.Version;
import lombok.Data;

@Data
public class VersionOnlyName {
    private String versionName;

    public VersionOnlyName(Version version){
        versionName = version.getVersionName();
    }
}
