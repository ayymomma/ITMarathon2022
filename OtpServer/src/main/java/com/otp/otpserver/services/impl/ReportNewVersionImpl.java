package com.otp.otpserver.services.impl;

import com.otp.otpserver.model.pojo.dto.application.AppVersionRequest;
import com.otp.otpserver.model.pojo.dto.application.AppVersionResponse;
import com.otp.otpserver.services.ReportNewVersionService;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class ReportNewVersionImpl implements ReportNewVersionService {

    @Override
    public List<AppVersionResponse> getNewVersions(List<AppVersionRequest> appVersionRequest) {
        return new ArrayList<>();
    }
}
