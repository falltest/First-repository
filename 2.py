class Student:
    def __init__(self, name: str, age: int, grades: list):
        self.name = name
        self.age = age
        self.grades = grades
    def count_scholership(self):
        s = 0
        count = 0
        for i in self.grades:
            s += i
            count += 1
        return s / count 
student = Student('Denis', 97, [5, 6, 4])
print(student.count_scholership())