CREATE TABLE Person (
	id integer PRIMARY KEY AUTOINCREMENT,
	name varchar,
	second_name varchar,
	personal_id varchar,
	phone varchar,
	e_mail varchar
);

CREATE TABLE supply_action (
	id integer PRIMARY KEY AUTOINCREMENT,
	status_id integer,
	person_id integer,
	helmet_id integer,
	jacket_id integer,
	panties_id integer,
	shoes_id integer
);

CREATE TABLE statusas (
	id integer PRIMARY KEY AUTOINCREMENT,
	name varchar
);

CREATE TABLE clothing (
	id integer PRIMARY KEY AUTOINCREMENT,
	name varchar,
	size varchar,
	type_id integer
);

CREATE TABLE clothing_type (
	id integer PRIMARY KEY AUTOINCREMENT,
	name varchar
);






