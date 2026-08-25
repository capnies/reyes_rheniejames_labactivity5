import sqlite3

def setup_database(cursor, conn):
    # Create tables only if they don't already exist
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS Students (
            StudentID INTEGER PRIMARY KEY,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,
            Major TEXT
        );

        CREATE TABLE IF NOT EXISTS Courses (
            CourseCode TEXT PRIMARY KEY,
            CourseName TEXT NOT NULL,
            Credits INTEGER
        );

        CREATE TABLE IF NOT EXISTS Enrollments (
            EnrollmentID INTEGER PRIMARY KEY AUTOINCREMENT,
            StudentID INTEGER,
            CourseCode TEXT,
            Semester TEXT,
            FOREIGN KEY(StudentID) REFERENCES Students(StudentID),
            FOREIGN KEY(CourseCode) REFERENCES Courses(CourseCode)
        );
    ''')
    
    # Insert default courses if the Courses table is empty
    cursor.execute("SELECT COUNT(*) FROM Courses")
    if cursor.fetchone()[0] == 0:
        cursor.executescript('''
            INSERT INTO Courses (CourseCode, CourseName, Credits) VALUES 
            ('CPE106L', 'Software Design Laboratory', 2),
            ('CPE105', 'Computer Architecture', 3),
            ('MTH101', 'Calculus I', 4);
        ''')
        conn.commit()