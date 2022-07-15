BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Employee" (
	"id (PK)"	INTEGER,
	"employee_code"	TEXT,
	"firstname"	TEXT,
	"middlename"	TEXT,
	"lastname"	TEXT,
	"department_id (FK)"	INTEGER,
	"position_id (FK)"	INTEGER,
	"salary"	NUMERIC,
	PRIMARY KEY("id (PK)")
);
CREATE TABLE IF NOT EXISTS "Department" (
	"id (PK)"	INTEGER,
	"name"	TEXT,
	PRIMARY KEY("id (PK)")
);
CREATE TABLE IF NOT EXISTS "Deductions" (
	"id (PK)"	INTEGER,
	"deduction"	TEXT,
	"description"	TEXT,
	PRIMARY KEY("id (PK)")
);
CREATE TABLE IF NOT EXISTS "Allowances" (
	"id (PK)"	INTEGER,
	"allowance"	TEXT,
	"description"	TEXT,
	PRIMARY KEY("id (PK)")
);
CREATE TABLE IF NOT EXISTS "Position" (
	"id (PK)"	INTEGER,
	"department_id (FK)"	INTEGER,
	PRIMARY KEY("id (PK)")
);
CREATE TABLE IF NOT EXISTS "Employee Allowances" (
	"id (PK)"	INTEGER,
	"employee_id (FK)"	INTEGER,
	"allowance_id (FK)"	INTEGER,
	"type"	INTEGER,
	"amount"	NUMERIC,
	"effective_date"	INTEGER,
	"date_created"	INTEGER,
	PRIMARY KEY("id (PK)")
);
CREATE TABLE IF NOT EXISTS "Employee Deductions" (
	"id (PK)"	INTEGER,
	"employee_id (FK)"	INTEGER,
	"deduction_id (FK)"	INTEGER,
	"type"	INTEGER,
	"amount"	NUMERIC,
	"effective_date"	INTEGER,
	"date_created"	INTEGER,
	PRIMARY KEY("id (PK)")
);
CREATE TABLE IF NOT EXISTS "Attendance" (
	"id (PK)"	INTEGER,
	"employee_id (FK)"	INTEGER,
	"log_type"	INTEGER,
	"datetime_log"	INTEGER,
	PRIMARY KEY("id (PK)")
);
CREATE TABLE IF NOT EXISTS "Payroll Table" (
	"id (PK)"	INTEGER,
	"ref_no"	TEXT,
	"date_from"	INTEGER,
	"date_to"	INTEGER,
	"type"	INTEGER,
	"status"	INTEGER,
	"date_created"	INTEGER,
	PRIMARY KEY("id (PK)")
);
CREATE TABLE IF NOT EXISTS "Payslip" (
	"id (PK)"	INTEGER,
	"payroll_id (FK)"	INTEGER,
	"employee_id (FK)"	INTEGER,
	"present"	INTEGER,
	"absent"	INTEGER,
	"salary"	NUMERIC,
	"allowance_amount"	NUMERIC,
	"allowances"	TEXT,
	"deduction_amount"	NUMERIC,
	"deductions"	TEXT,
	"net"	NUMERIC,
	"date_created"	INTEGER,
	PRIMARY KEY("id (PK)")
);
CREATE TABLE IF NOT EXISTS "Users" (
	"id (PK)"	INTEGER,
	"name"	TEXT,
	"username"	TEXT,
	"password"	TEXT,
	"type"	INTEGER,
	PRIMARY KEY("id (PK)")
);
COMMIT;
