# Student Enrollment System
##### Created by: Reyes, Rhenie James C.
###### Disclaimer: This README file is assisted by AI to smoothen the flow of the words
This is a simple command-line program where it involves student enrollment system with an integration of **SQLite** as database (`sqlite3` standard library).

## 1. Data Model

Three tables, related through a junction table (`Enrollments`) that resolves
the many-to-many relationship between students and courses:

| Table | Description | Key columns |
|---|---|---|
| `Students` | One row per student | `StudentID` (PK), `FirstName`, `LastName`, `Major` |
| `Courses` | One row per course offering | `CourseCode` (PK), `CourseName`, `Credits` |
| `Enrollments` | Links a student to a course for a given semester | `EnrollmentID` (PK, autoincrement), `StudentID` (FK), `CourseCode` (FK), `Semester` |

The database (`university.db`) and tables are created automatically the first time the program runs, via `setup_database()` in `dbInit.py`. Three sample courses (`CPE106L`, `CPE105`, `MTH101`) are seeded automatically if the `Courses` table is empty.

## 2. Files

| File | Purpose |
|---|---|
| `main.py` | Entry point — CLI menu and all CRUD operations (add/view/delete students, add/view courses, enroll students, view enrollment list) |
| `dbInit.py` | `setup_database()` — creates tables if they don't exist and seeds default courses |
| `university.db` | SQLite database file — created automatically on first run |

## 3. Requirements

- Python 3.7+
- No external libraries. We only use the built-in `sqlite3` module

## 4. How to Run

```bash
python3 main.py
```

On first run, `university.db` is created in the same folder and populated
with the `Students`, `Courses`, and `Enrollments` tables plus the default
course list.

## 5. Menu Options

```
1. View all Students
2. Add a new Student
3. Delete a Student
4. View all Courses
5. View full enrollment list
6. Enroll a Student in a Course
7. Add a new Course
0. Exit
```

- **Add a Student (2)** — prompts for Student ID, first/last name, and
  major. Fails gracefully with a clear message if the ID is not an integer
  or already exists.
- **Delete a Student (3)** — removes the student and cascades the delete
  to their enrollment records first, avoiding orphaned rows.
- **Add a Course (7)** — prompts for course code (auto-uppercased), name,
  and credits. Rejects duplicate course codes.
- **Enroll a Student (6)** — validates that both the Student ID and Course
  Code already exist before creating the enrollment record.
- **View full enrollment list (5)** — uses a `LEFT JOIN` across all three
  tables so students with no enrollments still show up (labeled "NOT
  enrolled in any courses"), instead of just being omitted.

## 6. Example Session

```
==============================
  STUDENT ENROLLMENT SYSTEM
==============================
1. View all Students
2. Add a new Student
3. Delete a Student
4. View all Courses
5. View full enrollment list
6. Enroll a Student in a Course
7. Add a new Course
0. Exit
==============================
Select an option (0-7): 2

--- Add New Student ---
Enter Student ID: 101
Enter First Name: Juan
Enter Last Name: Dela Cruz
Enter Major: Computer Engineering
Student added successfully!

Select an option (0-7): 6

--- Enroll Student in Course ---
Enter Student ID: 101
Enter Course Code (e.g., CPE106L): CPE106L
Enter Semester (e.g., Fall 2026): Fall 2026
Successfully enrolled Student 101 into CPE106L!

Select an option (0-7): 5

--- Full Enrollment List ---
[101] Juan Dela Cruz enrolled in CPE106L (Software Design Laboratory) - Fall 2026
```

## 7. Notes

- Re-running `main.py` does **not** wipe existing data — `setup_database()`
  uses `CREATE TABLE IF NOT EXISTS`, so `university.db` persists between
  runs. Delete `university.db` if you want a completely fresh start.
- `StudentID` and `CourseCode` are primary keys, so duplicate entries are
  rejected automatically by SQLite (`sqlite3.IntegrityError`), which the
  program catches and reports without crashing.