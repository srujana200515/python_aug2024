create table IF NOT EXISTS persons(id int primary key auto_increment , name varchar(50) not null, gender varchar(2), location varchar(50),age int check(age > 0));

 select * from persons;
 
 insert into persons(name,gender,location,age) values('srujana' ,'F' ,'Raichur',19);
 
 insert into persons(name,gender,location,age) values('sinchana' ,'F' ,'Raichur',20);
 
 insert into persons(name,gender,location,age) values('Neeha' ,'F' ,'Raichur',19);
 
 insert into persons(name,gender,location,age) values('Bhagya' ,'F' ,'Raichur',19);
 
 insert into persons(name,gender,location,age) values('Yukta' ,'F' ,'Bijapur',19);
 
 insert into persons(name,gender,location)    values('srujana' ,'F' ,'Raichur');
 
 insert into persons(name,gender,location,age) values('Pallavi' ,'F' ,'hospet',19);
 
 
 insert into persons(name,gender,location)    values('Disha' ,'F' ,'bagalkot');
 
 insert into persons(name,gender,location)    values('sru' ,'F' ,'Raichur');
 
 insert into persons(name,gender,age)          values ('srujana' ,'F' ,19);
 
 insert into persons(name,gender)              values('srujana' ,'F' );
 
 insert into persons(name,gender,location)    values('srujana' ,'F' ,'Raichur');
 
 insert into persons(name,gender,location,age) values('srujana' ,'F' ,'lingusugur',19);
 
 insert into persons(name,gender,location,age) values('srujana' ,'F' ,'Raichur',19);
 
 insert into persons(name,gender,location,age) values('srujana' ,'F' ,'Raichur',19);
 
 insert into persons(name,gender,location,age) values('srujana' ,'F' ,'Raichur',19);
 
 insert into persons(name,gender,location,age) values('srujana' ,'F' ,'Raichur',19);
 
 insert into persons(name)                     values('srujana' );
 
 insert into persons(name,gender,location)    values('Akash' ,'m' ,'Bijapur');
 
 insert into persons(name,gender,location,age) values('Yukta' ,'f' ,'Bijapur',19);
 
 insert into persons(name,gender,location,age) values('Nandini' ,'f' ,'belgavi',20);
 
 insert into persons(name,gender,location,age) values('Nandini' ,'f' ,'belgavi',20);
 
 insert  into persons(name,gender,location,age) values('Taniea' ,'f' ,'Honnavar',19);
 select name,location  from persons; 

 
 select location from persons;

 select distinct location from persons;
 
 select * from persons where age < 50;
 select * from persons  where location='Raichur';
 select * from persons  where age between 15 and 20;
 select * from persons where name like 'P%';
 select * from persons where name like 'P___a';
 select * from persons  where location in ('bijapur','belgavi','bagalkot');
 select * from persons  where location ='Raichur' or location='belgavi';
 select * from persons  where location =null;
 select * from persons  where location ='null';
 select * from persons  where location is null;
 
 
 
 
 



 
 
 
 
