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