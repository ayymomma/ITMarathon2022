package com.otp.otpserver.services;

import com.otp.otpserver.model.pojo.dto.user.UserRequest;
import com.otp.otpserver.model.pojo.dto.user.UserResponse;
import com.otp.otpserver.model.pojo.dto.user.UserWithToken;
import com.otp.otpserver.model.pojo.erd.User;

public interface UserService {

    UserWithToken login(String username, String password);

    UserResponse register(UserRequest userRequest);

    UserResponse logout(String token);

    User validateToken(String token);

    User getUserById(Integer userId);
}
