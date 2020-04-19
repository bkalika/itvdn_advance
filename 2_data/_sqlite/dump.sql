BEGIN TRANSACTION;
CREATE TABLE "users" (
                id INTEGER PRIMARY KEY,
                first_name VARCHAR(30) NOT NULL,
                last_name VARCHAR(30) NOT NULL,
                birthday VARCHAR(30)
    );
INSERT INTO "users" VALUES(1,'Bohdan','Kalika','15-03-1996');
INSERT INTO "users" VALUES(2,'Nazar','Kalika','23-05-2002');
COMMIT;
