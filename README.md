# Exam Result Management System

A beginner-friendly Python Data Science project for managing student exam marks and analyzing academic performance.

## Features
- Load student marks from a CSV file
- Calculate total, average, grade, and pass/fail status
- Display an individual student's result
- Summarize class performance
- Create a subject-wise average chart
- Export processed results to a CSV file

## Requirements
- Python 3.9+
- pandas
- matplotlib

## Setup

```bash
python -m venv .venv
```

Activate the environment:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

From the project folder:

```bash
python main.py
```

The sample data is in `data/students.csv`. Each subject is marked out of 100. A student passes when they score at least 35 in every subject.

## Project structure

```text
exam_result_management_system/
├── data/
│   └── students.csv
├── reports/
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## Customize
Replace `data/students.csv` with your own student records. Keep the columns `student_id`, `name`, `mathematics`, `science`, and `english`.

## GitHub upload

```bash
git init
git add .
git commit -m "Initial commit: Exam Result Management System"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the URL with your own GitHub repository URL.

## Note
This is a learning/demo project. Use fictional or anonymized student data when sharing publicly.
