drop view Oct10_person_view ;
drop view Oct10_emp_view ;
drop view Oct10_mgr_view ;

create view Oct10_person_view as
SELECT 
    person_id,
    type,
    name,
    age
FROM Oct10_person where type = 'oct10_person' ;

create or replace TRIGGER Oct10_person_trigger
     INSTEAD OF insert ON Oct10_person_view
     FOR EACH ROW
BEGIN
    insert into Oct10_person(
        person_id,
        type,
        name,
        age)
    VALUES ( 
        :NEW.person_id,
        'oct10_person',
        :NEW.name,
        :NEW.age) ;
END;
/

create view Oct10_emp_view as
SELECT 
    person_id,
    type,
    name,
    age, sal
FROM Oct10_person where type = 'oct10_emp' ;

create or replace TRIGGER Oct10_emp_trigger
     INSTEAD OF insert ON Oct10_emp_view
     FOR EACH ROW
BEGIN
    insert into Oct10_person(
        person_id,
        type,
        name,
        age, sal)
    VALUES ( 
        :NEW.person_id,
        'oct10_emp',
        :NEW.name,
        :NEW.age,
        :NEW.sal) ;
END;
/

create view Oct10_mgr_view as
SELECT 
    person_id,
    type,
    name,
    age, org
FROM Oct10_person where type = 'oct10_mgr' ;

create or replace TRIGGER Oct10_mgr_trigger
     INSTEAD OF insert ON Oct10_mgr_view
     FOR EACH ROW
BEGIN
    insert into Oct10_person(
        person_id,
        type,
        name,
        age, org)
    VALUES ( 
        :NEW.person_id,
        'oct10_mgr',
        :NEW.name,
        :NEW.age,
        :NEW.org) ;
END;
/