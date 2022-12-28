CREATE TABLE "User" (
	"id"	INTEGER NOT NULL,
	"mail"	TEXT NOT NULL,
	"username"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	PRIMARY KEY("id")
);

CREATE TABLE "Preference" (
	"id"	INTEGER NOT NULL,
	"positions"	INTEGER,
	"department"	TEXT,
	"year"	INTEGER,
	"base"	BLOB,
	"user_id"	TEXT NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("user_id") REFERENCES "User"("id")
);