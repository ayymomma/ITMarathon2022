package com.otp.otpserver.model.pojo.dto;

import com.otp.otpserver.model.pojo.erd.Application;
import com.otp.otpserver.model.pojo.erd.Version;
import lombok.Data;

import javax.persistence.*;
import java.sql.Timestamp;
import java.time.LocalDate;

@Data
public class VersionResponse {

    private String versionName;

    private Timestamp timestamp;

    public VersionResponse(Version version){
        versionName = version.getVersionName();
        timestamp = version.getTimestamp();
    }

}
