package com.otp.otpserver.services.utils;

import com.otp.otpserver.model.exception.HttpResponseException;
import org.springframework.http.ResponseEntity;

import static org.springframework.http.ResponseEntity.status;

public class ResponseEntityUtil {

    public static ResponseEntity<?> FromHttpResponseError(HttpResponseException e){
        return status(e.getStatus()).body(e.getMessage());
    }
}
