package com.otp.otpserver.model.pojo.dto.user;

import com.otp.otpserver.model.dao.UserRepository;
import com.otp.otpserver.model.pojo.erd.User;
import lombok.Data;

@Data
public class UserResponse {
    private Integer userId;
    private String username;
    private String role;

    public UserResponse(User user){
        userId = user.getUserId();
        username = user.getUsername();
        role = user.getRole();
    }
}
