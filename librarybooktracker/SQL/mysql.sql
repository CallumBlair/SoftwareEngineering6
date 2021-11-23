--CREATE SCRIPTS

--Creates the Book table
CREATE TABLE book_tbl
(
	book_id VARCHAR(5),
	book_title VARCHAR(20), 
	book_isbn VARCHAR(13), 
	CONSTRAINT book_tbl_pk PRIMARY KEY (book_id)
);
--Creates the Author table
CREATE TABLE auth_tbl
(
	author_id VARCHAR(5),
	auth_name VARCHAR(20), 
	CONSTRAINT auth_tbl_pk PRIMARY KEY (author_id)
);
--Creates the Member table
CREATE TABLE member_tbl
(
	member_id VARCHAR(10),
	member_name VARCHAR(20), 
	member_hash VARCHAR(20), 
	member_postcode VARCHAR(6), 
	CONSTRAINT member_tbl_pk PRIMARY KEY (member_id)
);
--Creates the Active loans table
CREATE TABLE active_loan_tbl
(
	loan_id VARCHAR(5),
	book_id VARCHAR(5), 
	member_id VARCHAR(10),
	creation_date DATE,
	return_date DATE,
	returned BOOLEAN,
	CONSTRAINT active_loan_tbl_pk PRIMARY KEY (loan_id)
);
--Creates the Past loans table
CREATE TABLE past_loan_tbl
(
	loan_id VARCHAR(5),
	book_id VARCHAR(5), 
	member_id VARCHAR(10),
	creation_date DATE,
	return_date DATE,
	returned BOOLEAN,
	CONSTRAINT past_loan_tbl_pk PRIMARY KEY (loan_id)
);
--Creates the Book Author link table
CREATE TABLE book_auth_lk
(
	fk_book_id VARCHAR(5),
	fk_auth_id VARCHAR(5),
	FOREIGN KEY (fk_book_id) REFERENCES book_tbl(book_id),
	FOREIGN KEY (fk_auth_id) REFERENCES auth_tbl(auth_id),
	CONSTRAINT book_auth_pk PRIMARY KEY (fk_book_id,fk_auth_id)
);

COMMIT;
--DROP SCRIPT

drop table book_tbl
drop table auth_tbl
drop table member_tbl
drop table active_loan_tbl
drop table past_loan_tbl
drop table book_auth_lk
