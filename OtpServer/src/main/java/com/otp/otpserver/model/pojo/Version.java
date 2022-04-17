package com.otp.otpserver.model.pojo;

import lombok.Data;

import javax.persistence.*;
import java.time.LocalDate;

@Data
@Entity
@Table(name = "VERSIONS")
public class Version {
    @Id
    @Column(name = "VERSION_ID", nullable = false)
    private Integer versionId;

    @Column(name = "VERSION_NAME", nullable = false)
    private String versionName;

    @Column(name = "TIMESTAMP", nullable = false)
    private LocalDate timestamp;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "APP_ID", nullable = false)
    private Application app;

}