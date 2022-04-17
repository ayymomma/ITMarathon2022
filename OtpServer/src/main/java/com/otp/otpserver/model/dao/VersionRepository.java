package com.otp.otpserver.model.dao;

import com.otp.otpserver.model.pojo.erd.Version;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface VersionRepository extends CrudRepository<Version, Integer> {
    List<Version> findByAppAppId(Integer appId);

    @Query(
            value = "SELECT * FROM version v WHERE v.app_id = ?1 ORDER BY v.timestamp DESC LIMIT 1",
            nativeQuery = true
    )
    Version findByAppAppIdAndVersionLatest(Integer appId);

    List<Version> findAllByAppAppIdAndVersionName(Integer appId, String versionName);

    List<Version> deleteAllByAppAppId(Integer appId);
}
