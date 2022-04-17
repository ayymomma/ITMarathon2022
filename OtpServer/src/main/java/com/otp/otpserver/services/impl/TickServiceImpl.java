package com.otp.otpserver.services.impl;

import com.otp.otpserver.services.TickService;

public class TickServiceImpl implements TickService {
    @Override
    public void tick() {
        System.out.println("Server has ticked");
    }

    @Override
    public long getDelay() {
        return 3000;
    }
}
