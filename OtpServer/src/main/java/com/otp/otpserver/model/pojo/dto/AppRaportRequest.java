package com.otp.otpserver.model.pojo.dto;

import lombok.Data;

import java.util.List;

@Data
public class AppRaportRequest {

    private List<AppVersionRequest> appVersionRequestList;

}
