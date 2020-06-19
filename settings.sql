BEGIN TRANSACTION;
CREATE TABLE "wait_time" (
	"minTime"	INTEGER NOT NULL UNIQUE,
	"maxTime"	INTEGER NOT NULL UNIQUE
);
CREATE TABLE "dataTargets" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"username"	TEXT NOT NULL UNIQUE,
	"posts"	INTEGER,
	"posts_used"	INTEGER
);
CREATE TABLE "captions" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"caption"	TEXT UNIQUE,
	"last_used"	INTEGER,
	"likes"	INTEGER,
	"comments"	INTEGER
);
CREATE TABLE "hashtags" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"hashtag"	TEXT NOT NULL UNIQUE,
	"last_used"	TEXT,
	"likes"	INTEGER,
	"comments"	INTEGER
);
CREATE TABLE "resupplying" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"date_of_resupply"	TEXT NOT NULL,
	"amount_downloaded"	INTEGER NOT NULL
);
CREATE TABLE "imageHashes" (
	"image_name"	TEXT NOT NULL,
	"image_hash"	BLOB NOT NULL,
	"used_datetime"	TEXT NOT NULL
);
COMMIT;