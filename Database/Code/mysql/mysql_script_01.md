CREATE DATABASE projects;

use projects;

CREATE TABLE projects (project_id INT(11) NOT NULL AUTO_INCREMENT, title VARCHAR(30), description VARCHAR(255), PRIMARY KEY (project_id));

show tables;

CREATE TABLE tasks (task_id INT(11) NOT NULL AUTO_INCREMENT, project_id INT(11) NOT NULL, description VARCHAR(255), PRIMARY KEY (task_id), FOREIGN KEY(project_id) REFERENCES projects(project_id));

INSERT INTO projects(title, description) VALUES("Organize Photos", "Organize old iPhone photos by year");

INSERT INTO tasks(description, project_id) VALUES("Organize 2020 photos", 1);
INSERT INTO tasks(description, project_id) VALUES("Organize 2019 photos", 1);

INSERT INTO projects(title, description) VALUES ("Read more", "Read a book a month this year");
INSERT INTO tasks(description, project_id) VALUES("Read The Huntress", 2);

SELECT * FROM tasks;
SELECT * FROM projects;

CREATE DATABASE household;