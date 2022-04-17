package com.otp.otpserver.services;

import com.otp.otpserver.model.pojo.erd.Application;
import com.otp.otpserver.model.pojo.erd.Version;

import java.util.List;

public interface ApplicationService {
    List<Application> getAllApplications();

    Application getApplication(Integer appId);

    Application deleteApplication(Integer appId);

    Application addApplication(Application application);

    Application updateApplication(Integer appId, Application application);

    List<Application> getApplicationsByName(String name);

    List<Version> getAllVersionsOfApp(Integer appId);

    List<Version> getNewerVersions(Integer appId, String versionName);
}
