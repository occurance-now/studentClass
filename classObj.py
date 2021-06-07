
#print(dir(my_list))
#self is the instance passed in

class Student:

    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already enrolled \
in the course")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} not found")

    def find_in_file(self, filename):
        with open(file_name) as f:
            line_count = 0
            for line in f:
                first_name, last_name, course_details = Student.prep_record(line.strip())
                student_read_in = Student(first_name, last_name, course_details)
                if line != "\n":
                    line_count += 1
                if self == student_read_in:
                    return True, line_count

            return False, line_count

    def add_to_file(self, filename):
        record_exists, line_count = self.find_in_file(filename)

        if record_exists:
            return "Record Already Exists"
        else:
            record_to_add = Student.prep_to_write(self.first_name, self.last_name, self.courses)
            with open(filename, "a+") as to_write:
                to_write.write(record_to_add+"\n")

            return "Record Added"

    def update_record(self, filename):
        record_exists, line_count = self.find_in_file(filename)
        print(record_exists)

        if self.find_in_file(filename):
            want_to_update = int(input(f"Do you want to update {self.first_name}, {self.last_name}'s file? Press 1 for yes or 2 to exit->"))
            if want_to_update == 1:
                old_record = Student.prep_to_write(self.first_name, self.last_name, self.courses)
                self.first_name = input("Enter New First Name->")
                self.last_name = input("Enter New Last Name->")
                updated_courses = []

                for i in self.courses:
                    course_edit = input(f"{i}, Enter new ->")
                    updated_courses.append(course_edit)

                self.courses = updated_courses
                record_to_add = Student.prep_to_write(self.first_name, self.last_name, self.courses)
                with open(filename, "a+") as to_write:
                    to_write.write(record_to_add+"\n")

                with open(filename, "r") as f:
                    lines = f.readlines()

                with open(filename, "w") as to_write:
                    for line in lines:
                        if line.strip("\n") != old_record:
                            to_write.write(line)

                return "Record Edited"
            else:
                print("exit")
        else:
            return "File Does Not excist"


    @staticmethod
    def prep_record(line):
        line = line.split(":")
        first_name, last_name = line[0].split(",")
        course_details = line[1].rstrip().split(",")
        return first_name, last_name, course_details

    @staticmethod
    def prep_to_write(first_name, last_name, courses):
        full_name = first_name+','+last_name
        courses = ",".join(courses)
        return full_name+':'+courses

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name

    def __len__(self):
        return len(self.courses)

    def __repr__(self):
        return f"Student('{self.first_name}','{self.last_name}', '{self.courses}')"

    def __str__(self):
        return f"First Name: {self.first_name.capitalize()}\
        \nLast Name: {self.last_name.capitalize()}\
        \nCourses: {', '.join(map(str.capitalize, self.courses))}"



class StudentAthlete(Student):

    def __init__(self, first, last, courses=None, sport=None):
        super().__init__(first, last, courses)
        self.sport = sport


courses = ['python','ruby','javascript']
file_name = "data.txt"

shane = Student("shane","palmer",["python","ruby","javascript"])
joe = Student("Jeff","Tarley",["python","ruby","javascript"])
jane = StudentAthlete("jane", "doe", courses, "hockey")

print(jane.sport)
print(isinstance(jane, Student))



#print(joe.find_in_file(file_name))
#print(joe.add_to_file(file_name))
#print(joe.update_record(file_name))
#student1.add_course("java")
#print(student1.courses)
#student1.remove_course("python")
#print(student1.courses)
#print(repr(student1))
