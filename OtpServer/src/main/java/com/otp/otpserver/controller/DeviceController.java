package com.otp.otpserver.controller;

import com.otp.otpserver.model.exception.HttpResponseException;
import com.otp.otpserver.model.pojo.erd.DeviceSession;
import com.otp.otpserver.services.DeviceService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import static com.otp.otpserver.services.utils.ResponseEntityUtil.FromHttpResponseError;
import static org.springframework.http.ResponseEntity.ok;

@Controller
@RequestMapping(path = "/api/devices")
public class DeviceController {

    @Autowired
    private DeviceService deviceService;

    @PostMapping(path = "connect")
    public @ResponseBody
    ResponseEntity<?> connectDevice(@RequestBody Integer deviceId) {
        try {
            DeviceSession session = deviceService.connectDevice(deviceId);
            return ok(session);
        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

    @PostMapping(path = "keep-alive")
    public @ResponseBody
    ResponseEntity<?> keepAliveDevice(@RequestBody Integer deviceId) {
        try {
            DeviceSession session = deviceService.keepAlive(deviceId);
            return ok(session);
        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }
}
