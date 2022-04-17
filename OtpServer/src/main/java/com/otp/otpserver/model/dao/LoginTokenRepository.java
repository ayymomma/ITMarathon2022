package com.otp.otpserver.model.dao;

import com.otp.otpserver.model.pojo.erd.LoginToken;
import com.otp.otpserver.model.pojo.erd.User;
import org.springframework.data.repository.CrudRepository;

public interface LoginTokenRepository extends CrudRepository<LoginToken, String> {
}
