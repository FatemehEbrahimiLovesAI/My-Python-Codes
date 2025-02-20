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

    def add_faculty(self):
        pass

    def add_course(self):
        pass

    def add_student(self):
        pass

    def add_professor(self):
        pass

    def add_cook(self):
        pass

    def add_server(self):
        pass

    def add_field(self):
        pass

    def remove_faculty(self):
        pass

    def remove_course(self):
        pass

    def remove_student(self):
        pass

    def remove_professor(self):
        pass

    def remove_cook(self):
        pass

    def remove_server(self):
        pass

    def remove_field(self):
        pass

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
