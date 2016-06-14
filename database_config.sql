SELECT 'Dropping database and user if exists' as '';
DROP DATABASE IF EXISTS project;
DROP USER IF EXISTS 'project_user'@'localhost';

SELECT 'Creating database and user' as '';
CREATE DATABASE project CHARACTER SET UTF8;
CREATE USER 'project_user'@'localhost' IDENTIFIED BY '&@^&Xl#iP#Fl6l';

SELECT 'Granting privileges to project' as '';
GRANT ALL PRIVILEGES ON project.* TO project_user@localhost;
FLUSH PRIVILEGES;