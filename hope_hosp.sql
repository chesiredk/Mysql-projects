use hope_hosp;
CREATE TABLE DEPARTMENT(
		DepartmentID      Int          NOT NULL  AUTO_INCREMENT,
        DepatmentName     Char(30)     NOT NULL,
        DepartmentHead    Char(30)     NOT NULL,
        OfficeNumber      Char(30)     NOT NULL,
        DepartmentPhone   Char(12)     NOT NULL,
        CONSTRAINT      DEPARTMENTPK    PRIMARY KEY(DepartmentID)
	); 
    
CREATE TABLE NURSE(
		NurseID           int        NOT NULL AUTO_INCREMENT,
        FristName        Char(30)    NOT NULL,
        LastName         Char(30)    NOT NULL,
        DepartmentID     int         NOT NULL,
        CONSTRAINT  NURSEPK    PRIMARY KEY(NurseID),
        CONSTRAINT  NURSEFK    FOREIGN KEY(DepartmentID)
        REFERENCES DEPARTMENT(DepartmentID)
								ON UPDATE NO ACTION
								ON DELETE NO ACTION
        );

CREATE TABLE DOCTOR(
		DoctorID      int         NOT NULL AUTO_INCREMENT,
        FristName     Char(30)    NOT NULL,
        LastName      Char(30)    NOT NULL,
        DepartmentID   int        NOT NULL,
        CONSTRAINT  DOCTORPK     PRIMARY KEY(DoctorID),
        CONSTRAINT  DOCTORFK    FOREIGN KEY(DepartmentID)
        REFERENCES DEPARTMENT(DepartmentID)
								ON UPDATE NO ACTION
								ON DELETE NO ACTION
        );

CREATE TABLE FACULTY(
	    FacultyID       int       NOT NULL   AUTO_INCREMENT,
        FirstName       Char(30)  NOT NULL,
        LastName        Char(30)  NOT NULL,
        DepartmentID    Char(30)  NOT NULL,
        CONSTRAINT      WORKERSPK PRIMARY KEY(FacultyID),
		CONSTRAINT      WORKERSFK FOREIGN KEY (DepartmentID)
							REFERENCES DEPARTMENT(DepartmentID)
								ON UPDATE NO ACTION
								ON DELETE NO ACTION
	);
        
CREATE TABLE PATIENT(
		PatientID		   Int			  NOT NULL  AUTO_INCREMENT,
		FirstName 		   Char(25)	      NOT NULL,
		LastName		   Char(25)	      NOT NULL,
		Phone			   Char(12) 	  NOT NULL,
        Gender             Char(12)       NOT NULL,
        EmergencyContact   Char(12)       NOT NULL,
        ConditionDetails   Char(200)      NOT NULL,
        NurseID            Char(30)       NOT NULL,
		AdmissionDate      date           NOT NULL,
		CONSTRAINT		PATIENTPK    	  PRIMARY KEY(PatientID),
        CONSTRAINT      PATIENTFK         FOREIGN KEY(NurseID)
        REFERENCES NURSE(NurseID)
								ON UPDATE NO ACTION
								ON DELETE NO ACTION
	);


        
