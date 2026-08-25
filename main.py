import sqlite3
from dbInit import setup_database  

def view_students(cursor):
    print("\n--- Registered Students ---")
    cursor.execute("SELECT * FROM Students;")
    rows = cursor.fetchall()
    if not rows:
        print("No students found.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} {row[2]} | Major: {row[3]}")

def add_student(cursor, conn):
    print("\n--- Add New Student ---")
    try:
        student_id = int(input("Enter Student ID: "))
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        major = input("Enter Major: ")
        
        cursor.execute('''
            INSERT INTO Students (StudentID, FirstName, LastName, Major) 
            VALUES (?, ?, ?, ?)
        ''', (student_id, first_name, last_name, major))
        conn.commit()
        print("Student added successfully!")
    except ValueError:
        print("Error: Student ID must be an integer.")
    except sqlite3.IntegrityError:
        print(f"Error: Student with ID {student_id} already exists.")

def delete_student(cursor, conn):
    print("\n--- Delete Student ---")
    try:
        student_id = int(input("Enter Student ID to delete: "))
        
        cursor.execute("DELETE FROM Enrollments WHERE StudentID = ?", (student_id,))
        
        cursor.execute("DELETE FROM Students WHERE StudentID = ?", (student_id,))
        
        if cursor.rowcount > 0:
            conn.commit()
            print(f"Student {student_id} and their enrollments were deleted.")
        else:
            print(f"No student found with ID {student_id}.")
    except ValueError:
        print("Error: Student ID must be an integer.")

def view_courses(cursor):
    print("\n--- Available Courses ---")
    cursor.execute("SELECT * FROM Courses;")
    for row in cursor.fetchall():
        print(f"Code: {row[0]} | Name: {row[1]} | Credits: {row[2]}")

def add_course(cursor, conn):
    print("\n--- Add New Course ---")
    try:
        course_code = input("Enter Course Code (e.g., CPE107): ").upper()
        course_name = input("Enter Course Name: ")
        credits = int(input("Enter Credits: "))
        
        cursor.execute('''
            INSERT INTO Courses (CourseCode, CourseName, Credits) 
            VALUES (?, ?, ?)
        ''', (course_code, course_name, credits))
        conn.commit()
        print(f"Course '{course_code}' added successfully!")
    except ValueError:
        print("Error: Credits must be an integer.")
    except sqlite3.IntegrityError:
        print(f"Error: Course {course_code} already exists.")

def view_enrollments(cursor):
    print("\n--- Full Enrollment List ---")
    cursor.execute('''
        SELECT 
            Students.StudentID,
            Students.FirstName || ' ' || Students.LastName AS FullName,
            Courses.CourseCode,
            Courses.CourseName,
            Enrollments.Semester
        FROM Students
        LEFT JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
        LEFT JOIN Courses ON Enrollments.CourseCode = Courses.CourseCode
        ORDER BY Students.StudentID;
    ''')
    rows = cursor.fetchall()
    if not rows:
        print("No students found in the database.")
    else:
        for row in rows:
            if row[2]:
                print(f"[{row[0]}] {row[1]} enrolled in {row[2]} ({row[3]}) - {row[4]}")
            else:
                print(f"[{row[0]}] {row[1]} is NOT enrolled in any courses.")

def enroll_student(cursor, conn):
    print("\n--- Enroll Student in Course ---")
    try:
        student_id = int(input("Enter Student ID: "))
        course_code = input("Enter Course Code (e.g., CPE106L): ").upper()
        semester = input("Enter Semester (e.g., Fall 2026): ")
        
        cursor.execute("SELECT * FROM Students WHERE StudentID = ?", (student_id,))
        if not cursor.fetchone():
            print("Error: Student ID does not exist.")
            return

        cursor.execute("SELECT * FROM Courses WHERE CourseCode = ?", (course_code,))
        if not cursor.fetchone():
            print("Error: Course Code does not exist.")
            return

        cursor.execute('''
            INSERT INTO Enrollments (StudentID, CourseCode, Semester) 
            VALUES (?, ?, ?)
        ''', (student_id, course_code, semester))
        conn.commit()
        print(f"Successfully enrolled Student {student_id} into {course_code}!")
    except ValueError:
        print("Error: Invalid input format.")

def main():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    
    setup_database(cursor, conn)
    
    while True:
        print("\n" + "="*30)
        print("  STUDENT ENROLLMENT SYSTEM")
        print("="*30)
        print("1. View all Students")
        print("2. Add a new Student")
        print("3. Delete a Student")
        print("4. View all Courses")
        print("5. View full enrollment list")
        print("6. Enroll a Student in a Course")
        print("7. Add a new Course")
        print("0. Exit")
        print("="*30)
        
        choice = input("Select an option (0-7): ")
        
        if choice == '1':
            view_students(cursor)
        elif choice == '2':
            add_student(cursor, conn)
        elif choice == '3':
            delete_student(cursor, conn)
        elif choice == '4':
            view_courses(cursor)
        elif choice == '5':
            view_enrollments(cursor)
        elif choice == '6':
            enroll_student(cursor, conn)
        elif choice == '7':
            add_course(cursor, conn)
        elif choice == '0':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 0 and 7.")

    conn.close()

if __name__ == '__main__':
    main()