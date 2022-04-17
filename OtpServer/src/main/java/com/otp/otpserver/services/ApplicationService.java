package com.otp.otpserver.services;

import com.otp.otpserver.model.pojo.Application;

import java.util.List;

public interface ApplicationService {
    List<Application> getAllApplications();

    Application getApplication(Integer appId);

    Application deleteApplication(Integer appId);

    Application addApplication(Application application);

    Application updateApplication(Integer appId, Application application);

    List<Application> getApplicationsByName(String name);

}
