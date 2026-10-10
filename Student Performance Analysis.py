import pandas as pd
import numpy as np

df = pd.read_csv("student.csv")
print(df)
print()

# Average Marks

average_marks = np.mean(df["Marks"])
print("Average Marks:",average_marks)

#Top Students

top_students = df.sort_values("Marks", ascending=False).head(5)
print("\nTop Students:")
print(top_students[["Name","Marks"]])

#Pass / Fail

df["Result"] = np.where(df["Marks"] >= 40, "Pass", "Fail")
print("\nStudent Results")
print(df[["Name", "Marks", "Result"]])

#Pass percentage

pass_percentage = np.mean(df["Result"] == "Pass") * 100
print("Pass Percentage:",pass_percentage)

#Fail percentage

fail_percentage = np.mean(df["Result"] == "Fail") * 100
print("Fail Percentage:", fail_percentage)

#Subject-wise Performance

subject_marks = df.groupby("Subject")["Marks"].mean()
print("\nSubject Wise Average Marks:")
print(subject_marks)

#Attendance vs Marks

print("\nAttendance vs Marks")
print(df[["Name", "Attendance", "Marks"]])