package com.otp.otpserver.services.impl;

import com.otp.otpserver.model.pojo.dto.application.AppVersionRequest;
import com.otp.otpserver.model.pojo.dto.application.AppVersionResponse;
import com.otp.otpserver.model.pojo.dto.version.VersionResponse;
import com.otp.otpserver.model.pojo.erd.Application;
import com.otp.otpserver.model.pojo.erd.Version;
import com.otp.otpserver.services.ApplicationService;
import com.otp.otpserver.services.ReportNewVersionService;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class ReportNewVersionImpl implements ReportNewVersionService {

    private final ApplicationService applicationService;

    public ReportNewVersionImpl(ApplicationService applicationService) {
        this.applicationService = applicationService;
    }

    @Override
    public List<AppVersionResponse> getNewVersions(List<AppVersionRequest> appVersionRequest) {

        ArrayList<AppVersionResponse> versions = new ArrayList<>();
        List<Application> allApplications = applicationService.getAllApplications();

        // Pentru fiecare aplicatie search versiuni noi
        for(AppVersionRequest userApp: appVersionRequest){
            for(Application app : allApplications)
            {
                // We got a match
                if (app.getAppName().equals(userApp.getAppName())){

                    // Look for newer versions
                    List<Version> newVersions = applicationService.getNewerVersions(app.getAppId(), userApp.getVersionName());

                    if(!newVersions.isEmpty()){
                        List<VersionResponse> versionResponses = new ArrayList<>();
                        for(Version v : newVersions){
                            versionResponses.add(new VersionResponse(v));
                        }

                        // Add newer versions in list
                        AppVersionResponse appVersionResponse = new AppVersionResponse();
                        appVersionResponse.setAppName(app.getAppName());
                        appVersionResponse.setNewVersions(versionResponses);

                        // Add to list
                        versions.add(appVersionResponse);
                    }

                    break;
                }
            }
        }
        return versions;
    }
}
