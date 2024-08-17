CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    class TEXT,
    gender TEXT,
    type TEXT,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    password TEXT
);


CREATE TABLE announcements (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS modules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    lessons_completed INTEGER NOT NULL,
    isactive char(1),
    total_lessons INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_id INTEGER,
    assignment_title TEXT NOT NULL,
    description TEXT,
    due_date TEXT,
    FOREIGN KEY (module_id) REFERENCES modules (id)
);

INSERT INTO modules (title, lessons_completed, total_lessons) VALUES
('Mathematics', 5, 15),
('Science', 8, 15),
('Computer Science', 6, 15),
('History', 3, 10),
('Geography', 4, 12);

INSERT INTO assignments (module_id, assignment_title, description, due_date) VALUES
(1, 'Algebra Homework', 'Complete exercises 1 to 10 on algebra.', '2024-08-30'),
(1, 'Calculus Quiz', 'Solve the calculus problems provided in class.', '2024-09-05'),
(2, 'Physics Lab Report', 'Submit your report on the recent lab experiment.', '2024-08-25'),
(2, 'Chemistry Worksheet', 'Complete the worksheet on chemical reactions.', '2024-09-01'),
(3, 'Programming Assignment', 'Develop a small project using Python.', '2024-09-10'),
(3, 'Database Exercise', 'Design a simple database schema for a given problem.', '2024-09-15'),
(4, 'Essay on Ancient Civilizations', 'Write a 2000-word essay on ancient civilizations.', '2024-09-20'),
(4, 'Timeline Project', 'Create a timeline of historical events.', '2024-09-25'),
(5, 'Map Creation', 'Draw a detailed map of your country.', '2024-08-28'),
(5, 'Geographical Survey', 'Submit a report on geographical features of your region.', '2024-09-02');

CREATE TABLE attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    month TEXT NOT NULL,
    total_days INTEGER NOT NULL,
    present_days INTEGER NOT NULL,
    percentage TEXT NOT NULL,
    color TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE attendance ADD COLUMN date TEXT;
