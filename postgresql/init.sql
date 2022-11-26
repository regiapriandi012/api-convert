CREATE USER 'auth_user'@'localhost' IDENTIFIED BY '123456';

CREATE DATABASE auth_db;

GRANT ALL PRIVILEGES ON auth_db.* TO 'auth_user'@'localhost';

use auth_db;

CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR (255) NOT NULL,
    password VARCHAR (255) NOT NULL
);

INSERT INTO user (email, password) VALUES ('regiapriandi012@gmail.com', '123456');
