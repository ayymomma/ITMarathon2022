package com.otp.otpserver.model.pojo.erd;

import lombok.Data;

import javax.persistence.*;
import java.sql.Timestamp;
import java.time.LocalDate;

@Data
@Entity
@Table(name = "VERSIONS")
public class Version {
    @Id
    @GeneratedValue
    @Column(name = "VERSION_ID", nullable = false)
    private Integer versionId;

    @Column(name = "VERSION_NAME", nullable = false)
    private String versionName;

    @Column(name = "TIMESTAMP", nullable = false)
    private Timestamp timestamp;

    @Column(name = "APP_PATH")
    private String appPath;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "APP_ID", nullable = false)
    private Application app;


}