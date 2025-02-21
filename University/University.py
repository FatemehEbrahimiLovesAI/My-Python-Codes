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
        return f"{self.name} university : address -> {self.address}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.address})"
    
    @classmethod
    def add_faculty(self,name : str,university : str,location : str):
        new_faculty = Faculty(name,university,location)
        University.list_of_faculties.append(new_faculty)

    @classmethod
    def add_course(self,name: str, faculties: list, lecturers: list):
        new_course = Course_unit(name,faculties,lecturers)
        University.list_of_courses.append(new_course)

    @classmethod
    def add_student(self, name, student_id, date_of_birth, year_of_entry, city, dorm_situation=False, dorm_location="don't have"):
        new_student = Student(name,student_id,date_of_birth)
        University.list_of_students.append(new_student)

    @classmethod
    def add_professor(self, name: str, courses: list):
        new_professor = Professor(name,courses)
        University.list_of_professors.append(new_professor)

    @classmethod
    def add_cook(self , name: str, staff_id: str):
        new_cook = Cook(name,staff_id)
        University.list_of_cooks.append(new_cook)
    
    @classmethod
    def add_server(self, name: str, staff_id: str):
        new_server = Server(name,staff_id)
        University.list_of_servers.append(new_server)

    @classmethod
    def add_field(self , name: str, courses: list):
        new_field = Field_of_study(name,courses)
        University.list_of_fields.append(new_field)

    @classmethod
    def remove_faculty(self):
        if self in University.list_of_faculties:
            University.list_of_faculties.remove(self)

    @classmethod
    def remove_course(self):
        if self in University.list_of_courses:
            University.list_of_courses.remove(self)

    @classmethod
    def remove_student(self):
        if self in University.list_of_students:
            University.list_of_students.remove(self)

    @classmethod
    def remove_professor(self):
        if self in University.list_of_professors:
            University.list_of_professors.remove(self)

    @classmethod
    def remove_cook(self):
        if self in University.list_of_cooks:
            University.list_of_cooks.remove(self)

    @classmethod
    def remove_server(self):
        if self in University.list_of_servers:
            University.list_of_servers.remove(self)

    @classmethod
    def remove_field(self):
        if self in University.list_of_fields:
            University.list_of_fields.remove(self)

class Faculty():
    list_of_courses = []

    def __init__(self, name: str, university: 'University', location: str):
        self.name = name
        self.university = university
        self.location = location

    def __str__(self):
        return f"name: {self.name}\nuniversity: {self.university}\nlocation: {self.location}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.university},{self.location})"
    

class Course_unit():
    def __init__(self, name: str, faculties: list, lecturers: list):
        self.name = name
        self.faculties = faculties
        self.lecturers = lecturers

    def __str__(self):
        return f"course name: {self.name}\ncourse faculties: {self.faculties}\ncourse lecturers: {self.lecturers}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.faculties},{self.lecturers})"

class Field_of_study():
    def __init__(self, name: str, courses: list):
        self.name = name
        self.courses = courses

    def __str__(self):
        return f"Field name: {self.name}\nField courses: {self.courses}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.courses})"

class Student():
    def __init__(self, name, student_id, date_of_birth, year_of_entry, city, dorm_situation=False, dorm_location="don't have"):
        self.name = name
        self.student_id = student_id
        self.date_of_birth = date_of_birth
        self.year_of_entry = year_of_entry
        self.city = city
        self.dorm_situation = dorm_situation
        self.dorm_location = dorm_location

    def __str__(self):
        return f"student name: {self.name}\nstudent ID: {self.student_id}\ndate of birth: {self.date_of_birth}\nyear of entry: {self.year_of_entry}\ndorm situation: {self.dorm_situation}\ndorm location: {self.dorm_location}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.student_id},{self.date_of_birth},{self.year_of_entry},{self.dorm_situation},{self.dorm_location})"

class President():
    def __init__(self,name,university,date_of_birth):
        self.name = name
        self.university = university
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"President name: {self.name}\nuniversity: {self.university}\ndate of birth: {self.date_of_birth}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.university},{self.date_of_birth})"

class Personnel():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"Personnel name: {self.name}\nPersonnel role: {self.role}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.role})"

class Professor(Personnel):
    def __init__(self, name: str, courses: list):
        super().__init__(name, "Professor")
        self.courses = courses

    def __str__(self):
        return f"Professor name: {self.name}\nProfessor courses: {self.courses}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.courses})"

class Guard(Personnel):
    def __init__(self, name: str, guard_id: str):
        super().__init__(name, "Guard")
        self.guard_id = guard_id

    def __str__(self):
        return f"Guard name: {self.name}\nGuard ID: {self.guard_id}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.guard_id})"

class DinningHallStaff(Personnel):
    def __init__(self, name, staff_id):
        super().__init__(name, "DinningHallStaff")
        self.staff_id = staff_id

    def __str__(self):
        return f"staff name: {self.name}\nstaff ID: {self.staff_id}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.staff_id})"

class Cook(DinningHallStaff):
    def __init__(self, name: str, staff_id: str):
        super().__init__(name, staff_id)

    def __str__(self):
        return f"cook name: {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.staff_id})"

class Server(DinningHallStaff):
    def __init__(self, name: str, staff_id: str):
        super().__init__(name, staff_id)

    def __str__(self):
        return f"server name: {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.staff_id})"
