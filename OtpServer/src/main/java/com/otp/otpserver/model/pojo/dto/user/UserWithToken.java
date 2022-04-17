package com.otp.otpserver.model.pojo.dto.user;

import lombok.Data;

@Data
public class UserWithToken {
    private String username;
    private String token;
    private String role;
}
