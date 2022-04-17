package com.otp.otpserver.model.dao;

import com.otp.otpserver.model.pojo.erd.Application;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface ApplicationRepository extends CrudRepository<Application, Integer> {
    List<Application> findByAppName(String name);
}
