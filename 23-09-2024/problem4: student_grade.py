students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 88),
    ("Eve", 95)
]

def calculate_grades_info(students):
    if not students:
        return None, None, None
    
    total_grades = 0
    highest_grade = float('-inf')
    lowest_grade = float('inf')
    
    for student in students:
        name, grade = student
        total_grades += grade
        
        if grade > highest_grade:
            highest_grade = grade
        if grade < lowest_grade:
            lowest_grade = grade
            
    average_grade = total_grades / len(students)
    return average_grade, highest_grade, lowest_grade

average, highest, lowest = calculate_grades_info(students)
print(f"Average Grade: {average:.2f}")
print(f"Highest Grade: {highest}")
print(f"Lowest Grade: {lowest}")
