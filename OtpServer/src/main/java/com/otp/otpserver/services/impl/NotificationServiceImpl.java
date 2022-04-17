package com.otp.otpserver.services.impl;

//
//@Service
//public class NotificationServiceImpl implements NotificationService {
//    @Autowired
//    private ApplicationService applicationService;
//    @Autowired
//    private VersionService versionService;
//
//    private final NotificationRepository notificationRepository;
//
//    public NotificationServiceImpl(NotificationRepository notificationRepository) {
//        this.notificationRepository = notificationRepository;
//    }
//
//
//    @Override
//    public Notificatio addUpdateNotification(NotificationRequest notificationRequest) {
//
//        UpdateNotification toBeAdded = new UpdateNotification();
//        List<Application> application = applicationService.getApplicationsByName(notificationRequest.getAppName());
//
//        if(application.isEmpty())
//            throw new HttpResponseException("No application with this name!", HttpStatus.NOT_FOUND);
//
//        Version version = versionService.getVersionOfNameAndAppid(notificationRequest.getVersionName(), application.get(0).getAppId());
//
//        toBeAdded.setAppId(application.get(0).getAppId());
//        toBeAdded.setDeviceId(notificationRequest.getDeviceId());
//        toBeAdded.setVersionId(version.getVersionId());
//
//        notificationRepository.save(toBeAdded);
//
//    }
//}
