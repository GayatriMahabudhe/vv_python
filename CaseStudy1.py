
# -------------------------------
# Case Study 1: Student Grade Calculator
# -------------------------------

# 1) Store marks of 5 students (each with 3 subjects) in a dictionary
#    Keys: student names; Values: list of marks in 3 subjects
students_marks = {
    "Aarav":   [95, 88, 92],
    "Isha":    [78, 82, 80],
    "Neha":    [60, 65, 62],
    "Rohit":   [55, 58, 52],
    "Karan":   [89, 91, 87]
}

# 2) Function to calculate the average marks of a student
def calculate_average(marks):
    """Returns the average of a list of numeric marks."""
    return sum(marks) / len(marks)

# 3) Function to assign grade based on average
def assign_grade(avg):
    """Returns grade based on the average marks."""
    if avg >= 90:
        return "A"
    elif 75 <= avg <= 89:
        return "B"
    elif 60 <= avg <= 74:
        return "C"
    else:
        return "Fail"

# 4) Compute and print each student's name, average, and grade
print("=== Student Averages & Grades ===")
student_averages = {}  # to keep averages for top scorer calculation

for name, marks in students_marks.items():
    avg = calculate_average(marks)
    grade = assign_grade(avg)
    student_averages[name] = avg
    print(f"Name: {name:6s} | Average: {avg:.2f} | Grade: {grade}")

# 5) Find and display the top scorer's name and average marks
top_scorer = max(student_averages, key=student_averages.get)
top_avg = student_averages[top_scorer]

print("\n=== Top Scorer ===")
print(f"Top Scorer: {top_scorer} | Average: {top_avg:.2f}")
