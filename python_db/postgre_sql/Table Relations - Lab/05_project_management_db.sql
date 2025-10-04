CREATE DATABASE project_management;

CREATE TABLE clients (
	id SERIAL PRIMARY KEY,
	name VARCHAR(10)
);

CREATE TABLE projects (
	id SERIAL PRIMARY KEY,
	client_id INT REFERENCES clients,
	project_lead_id INT
);

CREATE TABLE employees (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	project_id INT REFERENCES projects
);

ALTER TABLE projects
ADD CONSTRAINT fk_project_eployees
	FOREIGN KEY(project_lead_id)
		REFERENCES employees(id)
;