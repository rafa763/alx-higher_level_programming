-- convert hbtn_0c_0 database to UTF8
ALTER hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY 
	name 
	COLLATE utf8mb4_unicode_ci;
