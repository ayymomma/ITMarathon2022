package com.otp.otpserver.services.impl;

import com.otp.otpserver.model.dao.VersionRepository;
import com.otp.otpserver.model.exception.HttpResponseException;
import com.otp.otpserver.model.pojo.erd.Application;
import com.otp.otpserver.model.pojo.erd.Version;
import com.otp.otpserver.services.VersionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class VersionServiceImpl implements VersionService {

    @Autowired
    private VersionRepository versionRepository;

    @Override
    public List<Version> getAllVersionsOfApp(Integer appId) {

        List<Version> versionList = versionRepository.findByAppAppId(appId);

        if(versionList.isEmpty())
            throw new HttpResponseException("Application does not exist.", HttpStatus.NOT_FOUND);

        return versionRepository.findByAppAppId(appId);
    }

    @Override
    public Version getLastVersionOfApp(Integer appId) {
        return versionRepository.findByAppAppIdAndVersionLatest(appId);
    }

    @Override
    public Version getVersionOfId(Integer versionId) {
        Optional<Version> version = versionRepository.findById(versionId);

        if(version.isEmpty())
            throw new HttpResponseException("Version does not exist.", HttpStatus.NOT_FOUND);

        return version.get();
    }

    @Override
    public Version deleteVersion(Integer versionId) {
        Optional<Version> version = versionRepository.findById(versionId);
        if (version.isEmpty())
            throw new HttpResponseException("Version does not exist.", HttpStatus.NOT_FOUND);

        versionRepository.delete(version.get());
        return version.get();
    }

    @Override
    public List<Version> deleteAllVersionsOfApp(Integer appId) {

        return versionRepository.deleteAllByAppAppId(appId);
    }

    @Override
    public Version addVersion(Version version) {
        // Id is not important
        version.setVersionId(null);

        // se cauta sa nu fie acelasi nume si prenume
        List<Version> otherVersionList = versionRepository.findAllByAppAppIdAndVersionName(version.getApp().getAppId(), version.getVersionName());

        if (!otherVersionList.isEmpty())
            throw new HttpResponseException("A version with this name already exits.", HttpStatus.CONFLICT);

        // Se adauga versiune pentru app
        return versionRepository.save(version);
    }

    @Override
    public Version updateVersion(Integer versionId, Version version) {
        return null;
    }
}
