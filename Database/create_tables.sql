
CREATE TABLE users (
    user_id     INTEGER NOT NULL,
    username    VARCHAR2(255) NOT NULL,
    password    VARCHAR2(255) NOT NULL,
    role        VARCHAR2(255) NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE Devices (
    device_id       INTEGER NOT NULL,
    defice_name     VARCHAR2(255) NOT NULL,
    user_id         INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

CREATE TABLE applications (
    app_id          INTEGER NOT NULL,
    app_name        VARCHAR2(255) NOT NULL,
    app_path        VARCHAR2(255),
    PRIMARY KEY(app_id)
);

CREATE TABLE versions (
    version_id      INTEGER NOT NULL,
    version_name    VARCHAR2(255) NOT NULL,
    timestamp       DATE NOT NULL,
    app_id          INTEGER NOT NULL,
    PRIMARY KEY(version_id),
    FOREIGN KEY (app_id) REFERENCES applications(app_id)
);