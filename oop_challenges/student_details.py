import pickle

class Student:
    def __init__(self, stud_id, name, marks):
        self.stud_id = stud_id
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f"Student(name='{self.name}', stud_id='{self.stud_id}', marks={self.marks})"

def save_student(student, filename='students.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(student,file)

def load_student(filename='students.pkl'):
    with open(filename, 'rb') as file:
        student = pickle.load(file)
        return student

if __name__ == '__main__':

    students = [
        Student('S001', 'Neil', {'Math': 75, 'Science': 80}),
        Student('S002', 'Bob', {'Math': 68, 'Science': 74}),
        Student('S003', 'Sam', {'Math': 95, 'Science': 86})
    ]

    save_student(students)

    print(load_student())

