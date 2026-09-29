def calculate_result(maths, physics, python, english):
    # Calculate total marks
    total = maths + physics + python + english

    # Calculate percentage
    percentage = total / 4

    # Calculate grade
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Calculate result
    if percentage >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    return total, percentage, grade, result