# User authentication system in the faculty

class University():
    list_of_faculties = []
    list_of_courses = []
    list_of_students = []
    list_of_professors = []
    list_of_cooks = []
    list_of_servers = []
    list_of_fields = []
    
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        pass

    def __repr__(self):
        pass

class Faculty():
    list_of_courses = []

    def __init__(self, name: str, university: 'University', location: str):
        self.name = name
        self.university = university
        self.location = location

    def __str__(self):
        pass

    def __repr__(self):
        pass

class Course_unit():
    def __init__(self, name: str, faculties: list, lecturers: list):
        self.name = name
        self.faculties = faculties
        self.lecturers = lecturers

    def __str__(self):
        pass

    def __repr__(self):
        pass

class Field_of_study():
    def __init__(self, name: str, courses: list):
        self.name = name
        self.courses = courses

    def __str__(self):
        pass

    def __repr__(self):
        pass

class Student():
    def __init__(self, name, student_id, date_of_birth, year_of_entry, city, dorm_situation=False, dorm_location="don't have"):
        self.name = name
        self.student_id = student_id
        self.date_of_birth = date_of_birth
        self.year_of_entry = year_of_entry
        self.dorm_situation = dorm_situation
        self.dorm_location = dorm_location

    def __str__(self):
        pass

    def __repr__(self):
        pass

class President():
    def __init__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

class Personnel():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        pass

    def __repr__(self):
        pass

class Professor(Personnel):
    def __init__(self, name: str, courses: list):
        super().__init__(name, "Professor")
        self.courses = courses

    def __str__(self):
        pass

    def __repr__(self):
        pass

class Guard(Personnel):
    def __init__(self, name: str, guard_ID: str):
        super().__init__(name, "Guard")
        self.guard_ID = guard_ID

    def __str__(self):
        pass

    def __repr__(self):
        pass

class DinningHallStaff(Personnel):
    def __init__(self, name, staff_ID):
        super().__init__(name, "DinningHallStaff")
        self.staff_ID = staff_ID

    def __str__(self):
        pass

    def __repr__(self):
        pass

class Cook(DinningHallStaff):
    def __init__(self, name: str, staff_ID: str):
        super().__init__(name, staff_ID)

    def __str__(self):
        pass

    def __repr__(self):
        pass

class Server(DinningHallStaff):
    def __init__(self, name: str, staff_ID: str):
        super().__init__(name, staff_ID)

    def __str__(self):
        pass

    def __repr__(self):
        pass
