from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "data" / "students.csv"
REPORT_DIR = PROJECT_DIR / "reports"

SUBJECTS = ["mathematics", "science", "english"]


def calculate_results(data: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of the student data with totals, averages, grades and status."""
    results = data.copy()

    for subject in SUBJECTS:
        results[subject] = pd.to_numeric(results[subject], errors="coerce")

    if results[SUBJECTS].isna().any().any():
        raise ValueError("Every subject mark must be a valid number.")

    if ((results[SUBJECTS] < 0) | (results[SUBJECTS] > 100)).any().any():
        raise ValueError("Marks must be between 0 and 100.")

    results["total"] = results[SUBJECTS].sum(axis=1)
    results["average"] = results[SUBJECTS].mean(axis=1).round(2)
    results["status"] = results[SUBJECTS].ge(35).all(axis=1).map(
        {True: "PASS", False: "FAIL"}
    )

    results["grade"] = results["average"].apply(assign_grade)
    return results


def assign_grade(average: float) -> str:
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    if average >= 35:
        return "E"
    return "F"


def show_student_result(results: pd.DataFrame) -> None:
    student_id = input("Enter student ID: ").strip()
    match = results[results["student_id"].astype(str) == student_id]

    if match.empty:
        print("No student found with that ID.")
        return

    columns = ["student_id", "name", *SUBJECTS, "total", "average", "grade", "status"]
    print("\nSTUDENT RESULT")
    print(match[columns].to_string(index=False))


def show_class_summary(results: pd.DataFrame) -> None:
    pass_count = int((results["status"] == "PASS").sum())
    fail_count = int((results["status"] == "FAIL").sum())
    pass_rate = (pass_count / len(results) * 100) if len(results) else 0

    print("\nCLASS SUMMARY")
    print(f"Number of students : {len(results)}")
    print(f"Passed             : {pass_count}")
    print(f"Failed             : {fail_count}")
    print(f"Pass percentage    : {pass_rate:.1f}%")
    print(f"Class average      : {results['average'].mean():.2f}")

    print("\nSubject averages")
    print(results[SUBJECTS].mean().round(2).to_string())


def save_subject_chart(results: pd.DataFrame) -> None:
    REPORT_DIR.mkdir(exist_ok=True)
    averages = results[SUBJECTS].mean()

    ax = averages.plot(kind="bar", title="Average Marks by Subject", rot=0)
    ax.set_xlabel("Subject")
    ax.set_ylabel("Average mark (out of 100)")
    ax.set_ylim(0, 100)
    plt.tight_layout()

    chart_path = REPORT_DIR / "subject_averages.png"
    plt.savefig(chart_path)
    plt.close()
    print(f"Chart saved to: {chart_path}")


def main() -> None:
    if not DATA_FILE.exists():
        print(f"Dataset not found: {DATA_FILE}")
        return

    data = pd.read_csv(DATA_FILE)
    required_columns = {"student_id", "name", *SUBJECTS}
    missing = required_columns.difference(data.columns)

    if missing:
        print("Dataset is missing columns:", ", ".join(sorted(missing)))
        return

    try:
        results = calculate_results(data)
    except ValueError as error:
        print("Could not process marks:", error)
        return

    while True:
        print("\n=== EXAM RESULT MANAGEMENT SYSTEM ===")
        print("1. View all results")
        print("2. Search student result")
        print("3. View class performance summary")
        print("4. Save results to CSV")
        print("5. Create subject average chart")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print(results.to_string(index=False))
        elif choice == "2":
            show_student_result(results)
        elif choice == "3":
            show_class_summary(results)
        elif choice == "4":
            REPORT_DIR.mkdir(exist_ok=True)
            output_file = REPORT_DIR / "processed_results.csv"
            results.to_csv(output_file, index=False)
            print(f"Processed results saved to: {output_file}")
        elif choice == "5":
            save_subject_chart(results)
        elif choice == "0":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
