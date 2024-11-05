student_list = []

def add_student(student_id, student_name, student_grade):
    if check_duplicate_id(student_id):
        print(f"Cannot add student. A student with ID {student_id} already exists.")
    else:
        new_student = {
            'id': student_id,
            'name': student_name,
            'grade': student_grade
        }
        student_list.append(new_student)
        print(f"Student {student_name} added successfully.")

def check_duplicate_id(student_id):
    for student in student_list:
        if student['id'] == student_id:
            return True
    return False

n = int(input("Enter number of students: "))
print("Enter details of Students:")

for i in range(n):
    student_id = input(f"Enter ID for student {i+1}: ")
    student_name = input(f"Enter Name for student {i+1}: ")
    student_grade = input(f"Enter Grade for student {i+1}: ")
    
    add_student(student_id, student_name, student_grade)

print("\nList of Students:")
for i, student in enumerate(student_list, 1):
    print(f"Student {i}: ID={student['id']}, Name={student['name']}, Grade={student['grade']}")
