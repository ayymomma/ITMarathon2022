package com.otp.otpserver.model.dao;

import com.otp.otpserver.model.pojo.erd.User;
import org.springframework.data.repository.CrudRepository;

public interface UserRepository extends CrudRepository<User, Integer> {
    User findByUsernameAndPassword(String username, String password);
    User findByUsername(String username);
}
