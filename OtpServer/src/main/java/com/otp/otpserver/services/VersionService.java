package com.otp.otpserver.services;

import com.otp.otpserver.model.pojo.erd.Version;

import java.util.List;

public interface VersionService {
    List<Version> getAllVersionsOfApp(Integer appId);

    Version getLastVersionOfApp(Integer appId);

    Version getVersionOfId(Integer versionId);

    Version getVersionOfNameAndAppid(String versionName, Integer appId);

    Version deleteVersion(Integer versionId);

    List<Version> deleteAllVersionsOfApp(Integer appId);

    Version addVersion(Version version);


    Version updateVersion(Integer versionId, Version version);


}
