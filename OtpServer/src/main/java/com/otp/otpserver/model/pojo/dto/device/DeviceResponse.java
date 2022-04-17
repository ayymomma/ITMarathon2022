package com.otp.otpserver.model.pojo.dto.device;

import com.otp.otpserver.model.pojo.erd.Device;
import lombok.Data;

@Data
public class DeviceResponse {
    private String deviceId;
    private String deviceName;

    public DeviceResponse(Device device){
        deviceId = device.getDeviceId();
        deviceName = device.getDeviceName();
    }
}
