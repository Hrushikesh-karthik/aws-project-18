#COMMANDS TO RUN SHELL SCRIPT

chmod +x scr.sh --> grant permission to - make a file executable.

run it using -->    ./scr.sh

#MySQL

mysql -h <your-rds-endpoint> -u admin -p

CREATE DATABASE flask_crud;
USE flask_crud;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address VARCHAR(255)
);
