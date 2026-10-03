import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """Load student performance data from a CSV file."""
    return pd.read_csv(file_path)


def prepare_data(df):
    """Calculate the average score for each student."""
    subjects = ["Math", "Science", "English"]
    df["Average_Score"] = df[subjects].mean(axis=1)
    return df


def analyze_performance(df):
    """Display basic student performance analysis."""

    print("Student Performance Analysis")
    print("-" * 35)

    print("\nFirst 5 Records:")
    print(df.head())

    print("\nAverage Score by Study Hours:")
    study_hours = df.groupby("Study_Hours")["Average_Score"].mean()
    print(study_hours)

    print("\nAverage Score by Attendance:")
    attendance = df.groupby("Attendance")["Average_Score"].mean()
    print(attendance)

    print("\nSubject Average Scores:")
    print(df[["Math", "Science", "English"]].mean())

    print("\nCorrelation Matrix:")
    print(
        df[
            ["Study_Hours", "Attendance", "Math",
             "Science", "English", "Average_Score"]
        ].corr()
    )

    return study_hours, attendance


def create_visualizations(df):
    """Create charts to visualize student performance."""

    # Study Hours vs Average Score
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Study_Hours"], df["Average_Score"])
    plt.title("Study Hours vs Average Score")
    plt.xlabel("Study Hours")
    plt.ylabel("Average Score")
    plt.tight_layout()
    plt.savefig("study_hours_vs_score.png")
    plt.show()

    # Attendance vs Average Score
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Attendance"], df["Average_Score"])
    plt.title("Attendance vs Average Score")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Average Score")
    plt.tight_layout()
    plt.savefig("attendance_vs_score.png")
    plt.show()


def main():
    """Run the complete student performance analysis."""

    file_path = "student_performance.csv"

    df = load_data(file_path)
    df = prepare_data(df)

    analyze_performance(df)
    create_visualizations(df)


if __name__ == "__main__":
    main()