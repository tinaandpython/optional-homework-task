class Student:
    def __init__(self, name, credits):
        self._name = name
        self.credits = credits

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, credits):
        if credits < 0:
            self._credits = 0
        elif credits > 30:
            self._credits = 30
        else:
            self._credits = credits


    def print_student(self):
        print(f'Student: {self._name}, credits: {self.credits}')




student1 = Student("Mantas", -5)
student2 = Student("Julija", 35)
student3 = Student("Tomas", 12)

student1.print_student()
student2.print_student()
student3.print_student()
