-- In challenge3.sql

-- Create and use challenge3 database
create database if not exists challenge3;
use challenge3;

-- Create courses table with course_number as int
create table courses (
    id int auto_increment primary key,
    name varchar(100),
    course_title varchar(255),
    course_number int,
    department_name varchar(100),
    instructor varchar(100),
    quarter varchar(50)
);

-- Create course_schedule table with role defined as varchar
create table course_schedule (
    id int auto_increment primary key,
    name varchar(100),
    course varchar(255),
    role varchar(50),
    week_day varchar(100)
);

-- Insert sample data into courses
insert into courses (name, course_title, course_number, department_name, instructor, quarter) values
    ('ece 140a', 'product engineering', 140, 'electrical and computer engineering', 'ramsin', 'winter 2024'),
    ('cse 101', 'algorithms', 101, 'computer science and engineering', 'miles jones', 'winter 2024'),
    ('cse 110', 'engineering probability and statistics', 110, 'computer science and engineering', 'michael cobeltz', 'winter 2024');

-- Insert sample data into course_schedule
insert into course_schedule (name, course, role, week_day) values
    ('ramsin', 'ece 140a', 'instructional assistant', 'monday, wednesday'),
    ('keith muller', 'cse 101', 'instructional assistant', 'tuesday, thursday'),
    ('christiano ronaldo', 'cse 110', 'student', 'monday, wednesday, friday');

-- Query all rows from both tables
select * from courses;
select * from course_schedule;

-- Remove one row from each table
delete from courses where course_number = 110;
delete from course_schedule where name = 'christiano ronaldo';
