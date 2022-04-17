
CREATE TABLE users (
    user_id     INTEGER NOT NULL,
    username    VARCHAR2(255) NOT NULL,
    password    VARCHAR2(255) NOT NULL,
    role        VARCHAR2(255) NOT NULL,
    PRIMARY KEY (user_id)
);

INSERT INTO users VALUES(
    1,
    'admin',
    'admin',
    'ADMIN'
);

CREATE TABLE Devices (
    device_id       VARCHAR2(255) NOT NULL,
    device_name     VARCHAR2(255) NOT NULL,
    user_id         INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

CREATE TABLE applications (
    app_id          INTEGER NOT NULL,
    app_name        VARCHAR2(255) NOT NULL,
    app_path        VARCHAR2(255),
    PRIMARY KEY(app_id)
);


drop table versions;
CREATE TABLE versions (
    version_id      INTEGER NOT NULL,
    version_name    VARCHAR2(255) NOT NULL,
    timestamp       TIMESTAMP NOT NULL,
    app_id          INTEGER NOT NULL,
    PRIMARY KEY(version_id),
    FOREIGN KEY (app_id) REFERENCES applications(app_id)
);

ALTER TABLE versions ADD app_path varchar2(255);
ALTER TABLE versions ADD CONSTRAINT not_null_path NOT NULL;
ALTER TABLE versions ADD CONSTRAINT dfPath DEFAULT '/' FOR app_path;


ALTER TABLE TOKENS ADD CONSTRAINT user_token_fk FOREIGN KEY (user_id) REFERENCES user (user_id);

ALTER TABLE SESSIONS MODIFY SESSIONS device_id varchar2(255) not null;

SELECT * FROM applications;
SELECT * FROM versions;
SELECT * FROM devices;
SELECT * FROM users;
SELECT * FROM sessions;