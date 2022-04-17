package com.otp.otpserver.controller;


import com.otp.otpserver.model.dao.NotificationRepository;
import com.otp.otpserver.model.exception.HttpResponseException;
import com.otp.otpserver.model.pojo.dto.notification.NotificationRequest;
import com.otp.otpserver.model.pojo.erd.UpdateNotification;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import static com.otp.otpserver.services.utils.ResponseEntityUtil.FromHttpResponseError;

@Controller
@RequestMapping(path = "/api/notification")
public class NotificationController {

    private final NotificationRepository notificationRepository;

    public NotificationController(NotificationRepository notificationRepository) {
        this.notificationRepository = notificationRepository;
    }

    @PostMapping(path = "")
    public @ResponseBody
    ResponseEntity<?> createUpdateNotification(@RequestBody NotificationRequest notificationRequest) {
        try {
            UpdateNotification updateNotification = new UpdateNotification();
            updateNotification.setAppName(notificationRequest.getAppName());
            updateNotification.setDeviceId(notificationRequest.getDeviceId());
            updateNotification.setVersionName(notificationRequest.getVersionName());

            notificationRepository.save(updateNotification);
            return null;

        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

//    @PostMapping(path = "{DEVICE_ID}")
//    public @ResponseBody
//    ResponseEntity<?> downloadAppVersion(@RequestBody ) {
//        try {
//
//        } catch (HttpResponseException e) {
//            return FromHttpResponseError(e);
//        }
//    }


}
