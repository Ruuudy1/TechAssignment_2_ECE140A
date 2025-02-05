-- Create and use Challenge3 database
CREATE DATABASE IF NOT EXISTS Challenge3;
USE Challenge3;

-- Create courses table
create table courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    course_title VARCHAR(255),
    course_number INT,
    department_name VARCHAR(100),
    instructor VARCHAR(100),
    quarter VARCHAR(50)
);

-- Create course_schedule table
CREATE TABLE IF NOT EXISTS course_schedule (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    course VARCHAR(255),
    role ENUM('student', 'instructional assistant'),
    week_day VARCHAR(100)
);

-- Insert sample data into courses
INSERT INTO courses (name, course_title, course_number, department_name, instructor, quarter) VALUES
('ECE 140A', 'Product Engineering', 'ECE140A', 'Electrical and Computer Engineering', 'Ramsin', 'Winter 2024'),
('CSE 101', 'Algorithms', 'CSE101', 'Computer Science and Engineering', 'Miles Jones', 'Winter 2024'),
('CSE 110', 'Engineering Probability and Statistics', 'CSE110', 'Computer Science and Engineering', 'Michael Cobeltz', 'Winter 2024');

-- Insert sample data into course_schedule
INSERT INTO course_schedule (name, course, role, week_day) VALUES
('Ramsin', 'ECE 140A', 'instructional assistant', 'Monday, Wednesday'),
('Keith Muller', 'CSE 101', 'instructional assistant', 'Tuesday, Thursday'),
('Christiano Ronaldo', 'CSE 110', 'student', 'Monday, Wednesday, Friday');

-- Query all rows from both tables
SELECT * FROM courses;
SELECT * FROM course_schedule;

-- Remove one row from each table
DELETE FROM courses WHERE course_number = 'CSE110';
DELETE FROM course_schedule WHERE name = 'Christiano Ronaldo';
