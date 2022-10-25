import sqlite3
connector = sqlite3.connect('db/tabelis.db')
cursor = connector.cursor()

query = '''
CREATE TABLE IF NOT EXISTS person (
	id integer PRIMARY KEY AUTOINCREMENT,
	name VARCHAR (50),
	second_name VARCHAR(50),
	personal_id VARCHAR(12),
	phone VARCHAR(15),
	e_mail VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS status (
	id integer PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS clothing_type (
	id integer PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS clothing (
	id integer PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(255),
	size VARCHAR(30),
	type_id integer, FOREIGN KEY (type_id) REFERENCES cothing_type(id)
);

CREATE TABLE IF NOT EXISTS supply_action (
	id integer PRIMARY KEY AUTOINCREMENT,
	status_id integer, 
	person_id integer, 
	helmet_id integer, 
	jacket_id integer, 
	panties_id integer, 
	shoes_id integer,
    FOREIGN KEY(status_id) REFERENCES status(id),
    FOREIGN KEY(person_id) REFERENCES person(id),
    FOREIGN KEY(helmet_id) REFERENCES clothing(id),
    FOREIGN KEY(jacket_id) REFERENCES clothing(id),
    FOREIGN KEY(panties_id) REFERENCES clothing(id),
    FOREIGN KEY(shoes_id) REFERENCES clothing(id)
);
'''
cursor.execute(query)
connector.commit()
connector.close

