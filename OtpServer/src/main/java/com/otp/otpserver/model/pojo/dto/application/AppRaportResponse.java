package com.otp.otpserver.model.pojo.dto.application;

import lombok.Data;

import java.util.List;

@Data
public class AppRaportResponse {

    private List<AppVersionRequest> appVersionRequestList;

}
