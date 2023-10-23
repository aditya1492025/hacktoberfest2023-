import sqlite3

class Student:
    def __init__(self, name, address, contact_number, academic_records):
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.academic_records = academic_records

class StudentInformationSystem:
    def __init__(self):
        self.connection = sqlite3.connect('student_database.db')
        self.cursor = self.connection.cursor()

        # Create the student table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            academic_records TEXT NOT NULL
        )''')

    def add_student(self, student):
        self.cursor.execute('''INSERT INTO students (name, address, contact_number, academic_records) VALUES (?, ?, ?, ?)''',
                           (student.name, student.address, student.contact_number, student.academic_records))
        self.connection.commit()

    def update_student(self, student):
        self.cursor.execute('''UPDATE students SET name = ?, address = ?, contact_number = ?, academic_records = ? WHERE id = ?''',
                           (student.name, student.address, student.contact_number, student.academic_records, student.id))
        self.connection.commit()

    def delete_student(self, student_id):
        self.cursor.execute('''DELETE FROM students WHERE id = ?''', (student_id,))
        self.connection.commit()

    def get_all_students(self):
        self.cursor.execute('''SELECT * FROM students''')
        students = self.cursor.fetchall()
        return students

if __name__ == '__main__':
    sis = StudentInformationSystem()

    # Add a new student
    new_student = Student('John Doe', '123 Main Street', '123-456-7890', 'A')
    sis.add_student(new_student)

    # Update a student's information
    existing_student = sis.get_all_students()[0]
    existing_student.address = '456 Elm Street'
    sis.update_student(existing_student)

    # Delete a student
    sis.delete_student(existing_student.id)

    # Get all students
    students = sis.get_all_students()
    for student in students:
        print(student.name)
