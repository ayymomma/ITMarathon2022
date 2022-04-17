package com.otp.otpserver.controller;

import com.otp.otpserver.model.dao.DeviceRepository;
import com.otp.otpserver.model.exception.HttpResponseException;
import com.otp.otpserver.model.pojo.dto.device.DeviceRequest;
import com.otp.otpserver.model.pojo.dto.device.DeviceResponse;
import com.otp.otpserver.model.pojo.dto.user.UserLogin;
import com.otp.otpserver.model.pojo.dto.user.UserRequest;
import com.otp.otpserver.model.pojo.dto.user.UserResponse;
import com.otp.otpserver.model.pojo.dto.user.UserWithToken;
import com.otp.otpserver.model.pojo.erd.Device;
import com.otp.otpserver.model.pojo.erd.User;
import com.otp.otpserver.services.DeviceService;
import com.otp.otpserver.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Function;

import static com.otp.otpserver.services.utils.ResponseEntityUtil.FromHttpResponseError;
import static org.springframework.http.ResponseEntity.status;

@Controller
@RequestMapping(path = "/api/users")
public class UserController {

    @Autowired
    private UserService userService;

    @Autowired
    private DeviceService deviceService;


    @PostMapping(path = "add-device")
    public @ResponseBody
    ResponseEntity<?> addDevice(@RequestHeader(HttpHeaders.AUTHORIZATION) String token, @RequestBody DeviceRequest deviceRequest){
        try {
            User validUser = userService.validateToken(token);

            if (validUser == null)
                throw new HttpResponseException("Token is not valid!", HttpStatus.UNAUTHORIZED);

            Device added = deviceService.addDevice(deviceRequest, validUser.getUserId());

            return status(HttpStatus.CREATED).body(new DeviceResponse(added));

        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

    @GetMapping(path="devices")
    public @ResponseBody
    ResponseEntity<?> getAllDevices(@RequestHeader(HttpHeaders.AUTHORIZATION) String token){
        try {
            User validUser = userService.validateToken(token);

            List<Device> allDevices = deviceService.getAllDevicesOfUser(validUser.getUserId());
            List<DeviceResponse> result = new ArrayList<>();

            for(Device device : allDevices)
                result.add(new DeviceResponse(device));

            return status(HttpStatus.CREATED).body(result);

        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }

    }

    @PostMapping(path = "login")
    public @ResponseBody
    ResponseEntity<?> userLogin(@RequestBody UserLogin loginData) {
        try {
            UserWithToken token = userService.login(loginData.getUsername(), loginData.getPassword());
            return status(HttpStatus.OK).body(token);

        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

    @PostMapping(path = "register")
    public @ResponseBody
    ResponseEntity<?> userLogin(@RequestBody UserRequest userRequest) {
        try {
            UserResponse userResponse = userService.register(userRequest);
            return status(HttpStatus.OK).body(userResponse);

        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

    @PostMapping(path = "logout")
    public @ResponseBody
    ResponseEntity<?> logout(@RequestHeader(HttpHeaders.AUTHORIZATION) String token){
        try {
            UserResponse userResponse = userService.logout(token);
            return status(HttpStatus.OK).body(userResponse);

        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }
}
