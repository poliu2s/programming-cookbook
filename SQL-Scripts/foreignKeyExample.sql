CREATE TABLE User(
U_id int NOT NULL,
Username varchar(50),
Password varchar(60),
FirstName varchar(100),
LastName varchar(100),
PRIMARY KEY (U_id)
)

CREATE TABLE Project
(
P_id int NOT NULL,
Name varchar(100),
Owner int NOT NULL,
Description text,
PRIMARY KEY (P_id),
FOREIGN KEY (Owner) REFERENCES User(U_id)
)