CREATE TABLE "User" (
	"id"	INTEGER NOT NULL,
	"mail"	TEXT NOT NULL,
	"username"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	PRIMARY KEY("id")
);

CREATE TABLE "Dashboard" (
	"id"	INTEGER NOT NULL,
	"school"	TEXT,
	"base"	TEXT,
	"year"	TEXT,
	"department"	TEXT,
	"user_id"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("user_id") REFERENCES "User"("id")
);