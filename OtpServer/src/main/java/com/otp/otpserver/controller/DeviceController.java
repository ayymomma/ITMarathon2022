package com.otp.otpserver.controller;

import com.otp.otpserver.model.dao.DeviceAppsRepository;
import com.otp.otpserver.model.dao.NotificationRepository;
import com.otp.otpserver.model.exception.HttpResponseException;
import com.otp.otpserver.model.pojo.dto.application.AppVersionRequest;
import com.otp.otpserver.model.pojo.dto.device.DeviceOnlyId;
import com.otp.otpserver.model.pojo.dto.device.DeviceResponse;
import com.otp.otpserver.model.pojo.dto.notification.NotificationResponse;
import com.otp.otpserver.model.pojo.erd.*;
import com.otp.otpserver.services.ApplicationService;
import com.otp.otpserver.services.DeviceService;
import com.otp.otpserver.services.VersionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

import static com.otp.otpserver.services.utils.ResponseEntityUtil.FromHttpResponseError;
import static org.springframework.http.ResponseEntity.ok;

@Controller
@RequestMapping(path = "/api/devices")
public class DeviceController {

    @Autowired
    private VersionService versionService;
    @Autowired
    private ApplicationService applicationService;

    private final DeviceAppsRepository deviceAppsRepository;
    private final NotificationRepository notificationRepository;

    @Autowired
    private DeviceService deviceService;

    public DeviceController(DeviceAppsRepository deviceAppsRepository, NotificationRepository notificationRepository) {
        this.deviceAppsRepository = deviceAppsRepository;
        this.notificationRepository = notificationRepository;
    }

    @PostMapping(path = "connect")
    public @ResponseBody
    ResponseEntity<?> connectDevice(@RequestBody DeviceOnlyId deviceId) {
        try {
            DeviceSession session = deviceService.connectDevice(deviceId.getDeviceId());
            Device device = deviceService.getDeviceOfId(deviceId.getDeviceId());
            DeviceResponse response = new DeviceResponse(device);

            return ok(response);
        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

    @PostMapping(path = "{DEVICE_ID}/save-apps")
    public @ResponseBody
    ResponseEntity<?> saveAllAppsFromDevice(@PathVariable(name = "DEVICE_ID")  String deviceId,
                                           @RequestBody List<AppVersionRequest> apps) {
        try {
            // Check for device
            Device existing = deviceService.getDeviceOfId(deviceId);

            // Delete all registered
           deviceAppsRepository.deleteAllByDeviceId(deviceId);

            // Populate
            List<RegisteredApps> saved = new ArrayList<>();

            // Add all the apps
            for(AppVersionRequest appVersionRequest : apps){

                RegisteredApps registeredApps = new RegisteredApps();
                registeredApps.setDeviceAppId(null);
                registeredApps.setAppName(appVersionRequest.getAppName());
                registeredApps.setVersionName(appVersionRequest.getVersionName());
                registeredApps.setDeviceId(deviceId);

                RegisteredApps newSave = deviceAppsRepository.save(registeredApps);

                saved.add(newSave);
            }

            return ok(saved);
        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

    @GetMapping(path = "{DEVICE_ID}/apps")
    public @ResponseBody
    ResponseEntity<?> getAllAppsFromDevice(@PathVariable(name = "DEVICE_ID")  String deviceId) {
        try {
            // Check for device
            Device existing = deviceService.getDeviceOfId(deviceId);

            List<RegisteredApps> allApps = deviceAppsRepository.findAllByDeviceId(deviceId);
            List<AppVersionRequest> requests = new ArrayList<>();

            for(RegisteredApps registeredApps : allApps){
                AppVersionRequest appVersionRequest = new AppVersionRequest();
                appVersionRequest.setAppName(registeredApps.getAppName());
                appVersionRequest.setVersionName(registeredApps.getVersionName());
                requests.add(appVersionRequest);
            }
            return ok(requests);
        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

    @PostMapping(path = "keep-alive")
    public @ResponseBody
    ResponseEntity<?> keepAliveDevice(@RequestBody DeviceOnlyId deviceId) {
        try {
            DeviceSession session = deviceService.keepAlive(deviceId.getDeviceId());
            Device device = deviceService.getDeviceOfId(deviceId.getDeviceId());
            DeviceResponse response = new DeviceResponse(device);

            // Check if there are any Notifications for update
            List<UpdateNotification> uploads = notificationRepository.findAllByDeviceId(deviceId.getDeviceId());

            if(!uploads.isEmpty()){
                List<NotificationResponse> responses = new ArrayList<>();

                for(UpdateNotification update : uploads){
                    try {
                        List<Application> app = applicationService.getApplicationsByName(update.getAppName());
                        Version version = versionService.getVersionOfNameAndAppid(update.getVersionName(), app.get(0).getAppId());

                        NotificationResponse notificationResponse = new NotificationResponse();
                        notificationResponse.setAppName(update.getAppName());
                        notificationResponse.setVersionName(update.getVersionName());
                        notificationResponse.setAppPath(version.getAppPath());

                        responses.add(notificationResponse);
                    }
                    catch (HttpResponseException e){
                        // Do nothing
                    }
                }
                return ok(responses);
            }

            return ok().build();
        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

    @PostMapping(path = "disconnect")
    public @ResponseBody
    ResponseEntity<?> disconnectDevice(@RequestBody DeviceOnlyId deviceId) {
        try {
            DeviceSession session = deviceService.disconnectDevice(deviceId.getDeviceId());
            Device device = deviceService.getDeviceOfId(deviceId.getDeviceId());
            DeviceResponse response = new DeviceResponse(device);

            return ok(response);
        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

}
