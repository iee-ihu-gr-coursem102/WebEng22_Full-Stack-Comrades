CREATE TABLE IF NOT EXISTS User(
	"user_id"	INTEGER NOT NULL,
	"mail"	TEXT NOT NULL,
	"username"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	PRIMARY KEY("user_id")
);

CREATE TABLE IF NOT EXISTS Preferences(
	"preference_id"	INTEGER NOT NULL,
	"user_id"	INTEGER NOT NULL,
	"city"	TEXT,
	"university"	TEXT,
	"department"	TEXT,
	PRIMARY KEY("preference_id")
);