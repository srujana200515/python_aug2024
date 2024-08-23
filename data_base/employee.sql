use srujana_db;
create table employees(id int primary key auto_increment, name varchar(50) not null, designation varchar(40) not null, technology varchar(30) not null, phone_num bigint unique, commission int, salary float default 0, years_of_exp int);
select * from persons;
 insert into employees(name,designation,technology,phone_num,commission, salary,years_of_exp) values('srujana','manager','python','2222222222','40','100000','5');
 
 insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp) values('sinchana','manager','java','100066000','50','1000000','6');

insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp) values('Neeha','teamleader','c','00258413320','10','100000','5');

insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp) values('bhagya','assistent','c++','553322110','10','100000','5');


insert into employees(name,designation,technology,salary,years_of_exp) values('mala','manager','python','100000','5');


insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp) values('vijji','employee','c','5841229035','10','100000','5');

insert into employees (name,designation,technology,phone_num,commission,salary,years_of_exp) values('yukta','manager','python','1029384756','10','100000','5');

insert into employees(name,designation,technology,phone_num,commission,salary,years_of_exp) values('pallavi','teamleader','rust','713245890','10','100000','5');

insert into employees (name,designation,technology,phone_num,commission,salary,years_of_exp) values('disha','manager','javascript','789012345','10','100000','5');

insert into employees (name,designation,technology,phone_num,commission,salary,years_of_exp) values('pavitra','teamleader','java','984454210','10','100000','5');



insert into employees (name,designation,technology,phone_num,salary,years_of_exp) values('nandini','designer','python','0512006660','3500000','5');

insert into employees (name,designation,technology) values('taniea','designer','python');
select * from employees;



