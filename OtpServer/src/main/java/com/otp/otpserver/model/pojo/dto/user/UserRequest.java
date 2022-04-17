package com.otp.otpserver.model.pojo.dto.user;

import com.otp.otpserver.model.pojo.erd.User;
import lombok.Data;

@Data
public class UserRequest {
    private String username;
    private String password;
    private String repeatPassword;
}
