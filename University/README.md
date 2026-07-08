# University Management System

A Python-based university management system that models the hierarchical structure of a university including faculties, courses, students, professors, and staff members.

## Overview

This system provides a comprehensive object-oriented model for managing university entities. It includes classes for University, Faculty, Course Units, Fields of Study, Students, Professors, and various staff roles including Cooks, Servers, and Guards.

## Features

- University management with faculty, course, student, professor, and staff tracking
- Class methods for adding and removing entities from the system
- Inheritance hierarchy for personnel (Personnel -> Professor/Guard/DinningHallStaff -> Cook/Server)
- String and representation methods for all classes
- Student information including dormitory status
- Course management with faculty and lecturer assignments

## Class Structure

### University
The main container class that manages all university entities. Contains class-level lists for tracking:
- Faculties
- Courses
- Students
- Professors
- Cooks
- Servers
- Fields of study

**Key Methods:**
- `add_faculty(name, university, location)`
- `add_course(name, faculties, lecturers)`
- `add_student(name, student_id, date_of_birth, year_of_entry, city, dorm_situation, dorm_location)`
- `add_professor(name, courses)`
- `add_cook(name, staff_id)`
- `add_server(name, staff_id)`
- `add_field(name, courses)`
- Corresponding remove methods for each entity type

### Faculty
Represents a faculty within the university.

**Attributes:**
- `name`: Faculty name
- `university`: Associated university
- `location`: Physical location

### Course Unit
Represents an academic course.

**Attributes:**
- `name`: Course name
- `faculties`: List of associated faculties
- `lecturers`: List of lecturers teaching the course

### Field of Study
Represents an academic discipline.

**Attributes:**
- `name`: Field name
- `courses`: List of courses in this field

### Student
Represents a student in the university.

**Attributes:**
- `name`: Student name
- `student_id`: Unique identifier
- `date_of_birth`: Date of birth
- `year_of_entry`: Year of enrollment
- `city`: City of origin
- `dorm_situation`: Boolean indicating dorm residency
- `dorm_location`: Dormitory location

### Personnel (Base Class)
Parent class for all staff members.

**Attributes:**
- `name`: Staff name
- `role`: Staff role

### Professor
Extends Personnel with professor-specific attributes.

**Attributes:**
- `courses`: List of courses taught

### Guard
Extends Personnel with guard-specific attributes.

**Attributes:**
- `guard_id`: Guard identification

### DinningHallStaff (Base Class)
Parent class for dining hall staff.

**Attributes:**
- `staff_id`: Staff identification

### Cook
Extends DinningHallStaff.

### Server
Extends DinningHallStaff.

### President
Represents the university president.

**Attributes:**
- `name`: President name
- `university`: Associated university
- `date_of_birth`: Date of birth

## Usage Example

```python
# Create a university
uni = University("Example University", "123 University Ave")

# Add a faculty
University.add_faculty("Engineering", uni, "Building A")

# Add a student
University.add_student(
    "John Doe", 
    "S12345", 
    "1995-01-01", 
    "2020", 
    "New York", 
    True, 
    "Dormitory A"
)

# Add a professor
University.add_professor("Dr. Smith", ["Physics 101", "Physics 201"])

# Add a course
University.add_course("Physics 101", ["Engineering"], ["Dr. Smith"])
```

## Notes

- The University class uses class methods for adding and removing entities, which may need adjustment if you want instance-level management
- Some attributes like `faculties` and `lecturers` in Course_unit are expected to be lists of object references
- The `dorm_situation` parameter defaults to False and `dorm_location` defaults to "don't have" in the add_student method, though the Student class constructor has these as parameters

## Potential Improvements

- Implement instance methods for entity management rather than class methods
- Add proper validation for entity relationships
- Implement data persistence
- Add search and filtering functionality
- Implement authentication and authorization systems
- Add course registration and grading functionality
- Create a user interface layer
