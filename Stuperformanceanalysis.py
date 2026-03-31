import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the student performance dataset 
df = pd.read_csv("student_performance.csv")
print("Dataset Preview:")
print(df.head()) #df = data frame

# Step 3: To Calculate average score per student
df["average_score"] = np.mean(
    df[["math_score", "science_score", "english_score"]], axis=1
)

print("\nAverage Score per Student:")
print(df[["student_id", "average_score"]])

# Step 4: Subject-wise statistics
subjects = ["math_score", "science_score", "english_score"]

print("\nSubject-wise Statistics:")
for subject in subjects:
    print(f"\n{subject}")
    print("Mean:", df[subject].mean())
    print("Median:", df[subject].median())
    print("Standard Deviation:", df[subject].std())

# Step 5: Identify students with attendance below 75%
low_attendance = df[df["attendance_percentage"] < 75]

print("\nStudents with Attendance Below 75%:")
print(low_attendance[["student_id", "attendance_percentage"]])

# Step 6: Visualization - Score Distribution (Histograms)
plt.figure()
plt.hist(df["average_score"], bins=5)
plt.title("Average Score Distribution")
plt.xlabel("Average Score")
plt.ylabel("Number of Students")
plt.show()

# Step 7: Visualization - Subject-wise Boxplot
plt.figure()
df[subjects].boxplot()
plt.title("Subject-wise Score Comparison")
plt.ylabel("Scores")
plt.show()

# Step 8: Correlation between attendance and scores (Seaborn)
plt.figure()
sns.heatmap(
    df[["attendance_percentage", "math_score", "science_score", "english_score"]].corr(),
    annot=True
)
plt.title("Correlation Between Attendance and Scores")
plt.show()
 