class Student:
    def __init__(self,student_id,student_name,attendance):
        self.student_id=student_id
        self.student_name=student_name
        self.attendance=attendance
class Assessment:
    def __init__(self,assessment_score):
        self.assessment_score=assessment_score
class PlacementManager:
    def add_student(self):
        self.Student.append(Student)
    def __init__(self,assessment_score):
        self.assessment_score=assessment_score
    def add_student(self):
        self.Student.append(Student)
    def check_eligibilty(self): 
        if(self.attendance>=75 and self.assessment_score>=60):
            print("eligible")
        else:
            print("not eligible")
    def generate_report(self):
        print("Student id  is {self.student_id}")
        print("Student_name is {self.student_id}")
        print("Student attendance is {self.attendance}")
        print("Student assessment score is {self.assessment}")
                
        
    