from student_input import get_student_data
from grade_calculator import calculate_result


# Get student data
name, maths, physics, python, english = get_student_data()

# Calculate result
total, percentage, grade, result = calculate_result(
    maths, physics, python, english
)


# Display student result
print("========================================")
print("          STUDENT RESULT")
print("========================================")

print(f"Name       : {name}")
print(f"Maths      : {maths}")
print(f"Physics    : {physics}")
print(f"Python     : {python}")
print(f"English    : {english}")

print("----------------------------------------")

print(f"Total      : {total}/400")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")
print(f"Result     : {result}")

print("========================================")