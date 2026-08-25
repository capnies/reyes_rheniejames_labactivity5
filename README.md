# Student Enrollment System
##### Disclaimer: This README file is assisted by AI to smoothen the flow of the words
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
- No external libraries — only the built-in `sqlite3` module

## 4. How to Run

```bash
python3 main.py
```

On first run, `university.db` is created in the same folder and populated
with the `Students`, `Courses`, and `Enrollments` tables plus the default
course list.# reyes_rheniejames_labactivity5
# reyes_rheniejames_labactivity5
