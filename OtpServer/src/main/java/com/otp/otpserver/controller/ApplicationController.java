package com.otp.otpserver.controller;

import com.otp.otpserver.model.exception.HttpResponseException;
import com.otp.otpserver.model.pojo.dto.application.AppVersionRequest;
import com.otp.otpserver.model.pojo.dto.application.AppVersionResponse;
import com.otp.otpserver.model.pojo.dto.version.VersionRequest;
import com.otp.otpserver.model.pojo.dto.version.VersionResponse;
import com.otp.otpserver.model.pojo.erd.Application;
import com.otp.otpserver.model.pojo.erd.Version;
import com.otp.otpserver.services.ApplicationService;
import com.otp.otpserver.services.ReportNewVersionService;
import com.otp.otpserver.services.VersionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.List;

import static com.otp.otpserver.services.utils.ResponseEntityUtil.FromHttpResponseError;
import static org.springframework.http.ResponseEntity.ok;
import static org.springframework.http.ResponseEntity.status;


@Controller
@RequestMapping(path = "/api/applications")
public class ApplicationController {

    @Autowired
    private ApplicationService applicationService;

    @Autowired
    private VersionService versionService;

    @Autowired
    private ReportNewVersionService reportNewVersionService;


    /**
     * Gets a list of apps with versions avenable
     * @param appVersionRequest List of (appName, versionName)
     * @return A list of apps and list of versions available
     */
    @PostMapping(path = "check-versions")
    public @ResponseBody
    ResponseEntity<?> getLatestVersionList(@RequestBody List<AppVersionRequest> appVersionRequest){
        try{
            List<AppVersionResponse> appVersionResponse = reportNewVersionService.getNewVersions(appVersionRequest);

            return ok(appVersionResponse);
        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

    @GetMapping(path = "{ID}")
    public @ResponseBody
    ResponseEntity<?> getApplication(@PathVariable("ID") Integer id) {
        try {
            Application app = applicationService.getApplication(id);

            return ok(app);

        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

    @GetMapping(path = "{ID}/versions")
    public @ResponseBody
    ResponseEntity<?> getVersions(@PathVariable("ID") Integer appId) {
        try {
            List<Version> versionList = applicationService.getAllVersionsOfApp(appId);
            List<VersionResponse> versionResponses = new ArrayList<>();

            for(Version version : versionList){
                versionResponses.add(new VersionResponse(version));
            }
            return ok(versionResponses);

        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

    /*
    Add an author to DB
     */
    @PostMapping(path = "")
    public @ResponseBody
    ResponseEntity<?> addApplication(@RequestBody Application app) {
        try {
            Application createdApp = applicationService.addApplication(app);

            return status(HttpStatus.CREATED).body(createdApp);
        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

    /*
    Get all applications from DB
     */
    @GetMapping(path = "")
    public @ResponseBody
    ResponseEntity<?> getAllApplications(
            @RequestParam(required = false) String name
    ) {
        try {
            // This returns a JSON  with the apps
            List<Application> applicationList;

            if (name == null) applicationList = applicationService.getAllApplications();
            else applicationList = applicationService.getApplicationsByName(name);

            return ok().body(applicationList);

        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

    /*
    Update an author from DB
     */
    @PutMapping(path = "{ID}")
    public @ResponseBody
    ResponseEntity<?> updateApplication(@PathVariable(name = "ID") Integer appId,
            @RequestBody Application application
    ) {
        try {
            Application updatedApp = applicationService.updateApplication(appId, application);

            return ok().body(updatedApp);

        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

    /**
     * Method responsible for deleting an author
     *
     * @param appId the id of the author
     * @return The deleted author
     */
    @DeleteMapping(path = "{ID}")
    public @ResponseBody
    ResponseEntity<?> deleteApp(@PathVariable("ID") Integer appId) {
        try {
            Application deletedApp = applicationService.deleteApplication(appId);
            return ok().body(deletedApp);
        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }

    @PostMapping(path = "{ID}/add_version")
    public @ResponseBody
    ResponseEntity<?> addVersionToApp(@PathVariable(name = "ID") Integer appId, @RequestBody VersionRequest version){
        try {
            Application findApp = applicationService.getApplication(appId);

            Version versionERD = new Version();
            versionERD.setVersionName(version.getVersionName());
            versionERD.setApp(findApp);
            versionERD.setTimestamp(new Timestamp(System.currentTimeMillis()));

            Version added = versionService.addVersion(versionERD);

            return ok().body(new VersionResponse(added));
        } catch (HttpResponseException e) {
            return FromHttpResponseError(e);
        }
    }



}
