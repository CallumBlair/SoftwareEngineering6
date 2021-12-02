-- CREATE SCRIPTS

-- Creates the Book table
CREATE TABLE book_tbl
(
	book_isbn VARCHAR(25),
	book_title VARCHAR(100), 
	CONSTRAINT book_tbl_pk PRIMARY KEY (book_isbn)
);

-- Creates the Book Instance table
CREATE TABLE instance_tbl
(
	book_id VARCHAR(25),
	fk_book_isbn VARCHAR(25),
	book_status VARCHAR(100),
	FOREIGN KEY (fk_book_isbn)
		REFERENCES book_tbl(book_isbn),
	CONSTRAINT instance_tbl_pk PRIMARY KEY (book_id)
);

-- Creates the Author table
CREATE TABLE auth_tbl
(
	author_id int NOT NULL,
	auth_name VARCHAR(50), 
	CONSTRAINT auth_tbl_pk PRIMARY KEY (author_id)
);

-- Creates the Staff table
CREATE TABLE staff_tbl
(
	staff_id int NOT NULL AUTO_INCREMENT,
	staff_name VARCHAR(50), 
	staff_pw VARCHAR(20), 
	staff_postcode VARCHAR(8), 
	CONSTRAINT staff_tbl_pk PRIMARY KEY (staff_id)
);

-- Creates the Member table
CREATE TABLE member_tbl
(
	member_id int NOT NULL AUTO_INCREMENT,
	member_name VARCHAR(50), 
	member_pw VARCHAR(20), 
	member_postcode VARCHAR(8), 
	CONSTRAINT member_tbl_pk PRIMARY KEY (member_id)
);
ALTER TABLE member_tbl AUTO_INCREMENT=10000; 

-- Creates the Active loans table
CREATE TABLE active_loan_tbl
(
	loan_id int NOT NULL AUTO_INCREMENT,
	book_id VARCHAR(25) UNIQUE,
	member_id int,
	creation_date DATE,
	return_date DATE,
	returned BOOLEAN,
	FOREIGN KEY (book_id)
		REFERENCES instance_tbl(book_id),
	FOREIGN KEY (member_id)
		REFERENCES member_tbl(member_id),
	CONSTRAINT active_loan_tbl_pk PRIMARY KEY (loan_id)
);

-- Creates the Past loans table
CREATE TABLE past_loan_tbl
(
	loan_id int UNIQUE,
	book_id VARCHAR(25) , 
	member_id int,
	creation_date DATE,
	return_date DATE,
	returned BOOLEAN,
	CONSTRAINT past_loan_tbl_pk PRIMARY KEY (loan_id)
);
-- Creates the Book Author link table
CREATE TABLE book_auth_lk
(
	fk_book_id VARCHAR(25),
	fk_auth_id int,
	FOREIGN KEY (fk_book_id)
		REFERENCES book_tbl(book_isbn),
	FOREIGN KEY (fk_auth_id)
		REFERENCES auth_tbl(author_id),
	CONSTRAINT book_auth_pk PRIMARY KEY (fk_book_id,fk_auth_id)
);

COMMIT;

-- INSERT SCRIPTS

-- Staff INSERT
INSERT INTO staff_tbl(staff_name,staff_pw,staff_postcode) VALUES('Mr Bennett','Teacher1', 'UB10 0JU');
INSERT INTO staff_tbl(staff_name,staff_pw,staff_postcode) VALUES('Mr Dalton','Teacher2', 'PO36 9JD');

-- Member INSERT
INSERT INTO member_tbl(member_name,member_pw,member_postcode) VALUES('Andrew','Password1', 'LN9 6PL');
INSERT INTO member_tbl(member_name,member_pw,member_postcode) VALUES('Peter','Password2', 'EC3M 7HJ');
INSERT INTO member_tbl(member_name,member_pw,member_postcode) VALUES('Aiden','Password3', 'DN14 5SN');
INSERT INTO member_tbl(member_name,member_pw,member_postcode) VALUES('David','Password4', 'PA47 7SR');
INSERT INTO member_tbl(member_name,member_pw,member_postcode) VALUES('Sarah','Password5', 'B90 4EY');
INSERT INTO member_tbl(member_name,member_pw,member_postcode) VALUES('Michael','Password6', 'LE14 4AW');
INSERT INTO member_tbl(member_name,member_pw,member_postcode) VALUES('Isobele','Password7', 'PH35 4HJ');

-- Author INSERT
INSERT INTO auth_tbl(author_id, auth_name) VALUES('1','Jeremy Clarkson');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('2','David Walliams');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('3','Francis Crosby');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('4','Tiffany Goodall');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('5','Troy McMillan');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('6','Quentin Docter');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('7','Emmett Dulaney');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('8','Toby Skandier');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('9','Tim Walker');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('10','Eoin Colfer');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('11','Anothony Horowitz');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('12','Charlie Higson');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('13','Garth Nix');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('14','Michael Dawson');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('15','Enid Blyton');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('16','Lee Childs');
INSERT INTO auth_tbl(author_id, auth_name) VALUES('17','Barbra Nadel');

-- Book INSERT
INSERT INTO book_tbl(book_title,book_isbn) VALUES('The Mystery of the Burnt Cottage','978-1-4052-0393-7');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('Double of Die','9780-4-322032');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('Artemis Fowl and the Lost Colony','0-141-39268-6');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('The flying Fizzler','978-0-571-23301-4');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('Abhorsen','0-00-713735-4');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('The devil and his boy','978-1-4063-0569-2');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('Return to Groosham Grange','978-0-7445-8345-8');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('Public Enemy Number Two','978-1-4063-0681-1');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('The World According to Clarkson Volume 2','978-0-141-02860-6');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('Dont Stop me now','978-0-718-14905-5');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('Python Programming third addition','9781435455009');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('A Noble Killing','978-0-7553-7161-7');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('Killing Floor','978-0-553-82616-6');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('CompTIA A+','978-1-119-13785-6');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('A handbook of Fighter Aircraft','1-84309-444-4');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('CCNA Security','978-1-119-40993-9');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('Student CookBook','978-1-78713-015-9');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('Gangsta Granny','978-0-00-737144-0');
INSERT INTO book_tbl(book_title,book_isbn) VALUES('The World According to Clarkson Volume 1','0-141-01789-9');

-- Instance INSERT
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0001','978-1-4052-0393-7','As New');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0002','9780-4-322032','As New');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0003','0-141-39268-6','Worn');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0004','978-0-571-23301-4','As New');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0005','0-00-713735-4','Damaged');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0006','978-1-4063-0569-2','As New');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0007','978-0-7445-8345-8','Worn');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0008','978-1-4063-0681-1','Worn');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0009','978-0-141-02860-6','Worn');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0010','978-0-718-14905-5','Damaged');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0011','9781435455009','As New');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0012','978-0-7553-7161-7','Worn');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0013','978-0-553-82616-6','As New');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0014','978-1-119-13785-6','As New');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0015','1-84309-444-4','Damaged');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0016','978-1-119-40993-9','Worn');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0017','978-0-00-737144-0','As New');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0018','978-1-78713-015-9','Worn');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0019','0-141-01789-9','Worn');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0020','0-141-01789-9','As New');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0021','978-0-571-23301-4','Damaged');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0022','978-1-4052-0393-7','Worn');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0023','978-0-571-23301-4','Worn');
INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('0024','978-1-119-13785-6','Damaged');

-- Book Auth Lnk Insert
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('978-1-4052-0393-7','15');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('0-141-01789-9','1');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('978-1-4063-0681-1','11');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('978-0-571-23301-4','9');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('9781435455009','14');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('978-0-00-737144-0','2');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('978-0-718-14905-5','1');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('978-1-78713-015-9','4');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('978-1-119-40993-9','5');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('978-0-7553-7161-7','17');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('1-84309-444-4','3');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('978-0-141-02860-6','1');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('978-0-7445-8345-8','11');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('978-1-4063-0569-2','11');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('9780-4-322032','12');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('0-141-39268-6','10');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('0-00-713735-4','13');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('978-1-119-13785-6','6');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('978-1-119-13785-6','7');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('978-1-119-13785-6','8');
INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('978-0-553-82616-6','16');

COMMIT;

-- DROP SCRIPT
drop table book_auth_lk;
drop table active_loan_tbl;
drop table past_loan_tbl;
drop table instance_tbl;
drop table book_tbl;
drop table auth_tbl;
drop table member_tbl;
drop table staff_tbl;

COMMIT;