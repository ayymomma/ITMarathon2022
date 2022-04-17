package com.otp.otpserver.controller;

import com.otp.otpserver.model.exception.HttpResponseException;
import com.otp.otpserver.model.pojo.Application;
import com.otp.otpserver.model.pojo.dto.ApplicationNoId;
import com.otp.otpserver.services.ApplicationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;

import static com.otp.otpserver.services.utils.ResponseEntityUtil.FromHttpResponseError;
import static org.springframework.http.ResponseEntity.ok;
import static org.springframework.http.ResponseEntity.status;


@Controller
@RequestMapping(path = "/api/applications")
public class ApplicationController {

    @Autowired
    private ApplicationService applicationService;

    /**
     * Method responsible for getting an author from db
     *
     * @param id the id of the author
     * @return An author
     */
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
            @RequestBody ApplicationNoId application
    ) {
        try {
            Application updatedApp = applicationService.updateApplication(appId, application.toApplicationErd());

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


}
