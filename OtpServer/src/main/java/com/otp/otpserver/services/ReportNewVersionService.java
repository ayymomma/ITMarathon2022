package com.otp.otpserver.services;

import com.otp.otpserver.model.pojo.dto.AppVersionRequest;
import com.otp.otpserver.model.pojo.dto.AppVersionResponse;

import java.util.List;

public interface ReportNewVersionService {

    List<AppVersionResponse> getNewVersions(List<AppVersionRequest> appVersionRequest);
}
