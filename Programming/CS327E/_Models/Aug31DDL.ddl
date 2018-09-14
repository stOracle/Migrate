-- Generated by Oracle SQL Developer Data Modeler 4.1.3.901
--   at:        2016-09-14 16:34:37 CDT
--   site:      Oracle Database 11g
--   type:      Oracle Database 11g




DROP TABLE Aug31_Person CASCADE CONSTRAINTS ;

DROP TABLE Aug31_Phone CASCADE CONSTRAINTS ;

CREATE TABLE Aug31_Person
  (
    person_id INTEGER NOT NULL ,
    name      VARCHAR2 (256)
  ) ;
ALTER TABLE Aug31_Person ADD CONSTRAINT Aug31_Person_PK PRIMARY KEY ( person_id ) ;


CREATE TABLE Aug31_Phone
  (
    phone_id               INTEGER NOT NULL ,
    type                   VARCHAR2 (256) ,
    phone                  VARCHAR2 (256) ,
    Aug31_Person_person_id INTEGER NOT NULL
  ) ;
ALTER TABLE Aug31_Phone ADD CONSTRAINT Aug31_Phone_PK PRIMARY KEY ( phone_id ) ;


ALTER TABLE Aug31_Phone ADD CONSTRAINT Aug31_Phone_Aug31_Person_FK FOREIGN KEY ( Aug31_Person_person_id ) REFERENCES Aug31_Person ( person_id ) ;

CREATE SEQUENCE Aug31_Person_person_id_SEQ START WITH 1 NOCACHE ORDER ;
CREATE OR REPLACE TRIGGER Aug31_Person_person_id_TRG BEFORE
  INSERT ON Aug31_Person FOR EACH ROW WHEN (NEW.person_id IS NULL) BEGIN :NEW.person_id := Aug31_Person_person_id_SEQ.NEXTVAL;
END;
/

CREATE SEQUENCE Aug31_Phone_phone_id_SEQ START WITH 1 NOCACHE ORDER ;
CREATE OR REPLACE TRIGGER Aug31_Phone_phone_id_TRG BEFORE
  INSERT ON Aug31_Phone FOR EACH ROW WHEN (NEW.phone_id IS NULL) BEGIN :NEW.phone_id := Aug31_Phone_phone_id_SEQ.NEXTVAL;
END;
/


-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                             2
-- CREATE INDEX                             0
-- ALTER TABLE                              3
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           2
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          2
-- CREATE MATERIALIZED VIEW                 0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
