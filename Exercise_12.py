#dictionary
#---Menu---
#1. Add student
#2. show student
#3. update student
    #number
    #name
    #gender
    #age
#4. delete student
#5. exit

students = []

# FUNCTION 1: Add Student
def add_student():
    print("\n--- ADD STUDENT ---")
    
    size = int(input("How many students do you want to add? "))
    
    for i in range(size):
        print(f"\n--- Student {i+1} ---")
        
        student_number = input("Student Number: ")
        
        if next((s for s in students if s['number'] == student_number), None):
            print("Student number already exists!")
            continue
        
        name = input("Name: ")
        gender = input("Gender: ")
        age = input("Age: ")
        
        students.append({
            "number": student_number,
            "name": name,
            "gender": gender,
            "age": age
        })
        
        print("Student added successfully!")
    
    print(f"\nAdded {size} student(s)!")


def show_student():
    print("\n--- SHOW STUDENT ---")
    
    if len(students) == 0:
        print("NO STUDENT FOUND!")
    else:
        for student in students:
            print(f"\nStudent Number: {student['number']}")
            print(f"  Name: {student['name']}")
            print(f"  Gender: {student['gender']}")
            print(f"  Age: {student['age']}")


def update_student():
    print("\n--- UPDATE STUDENT ---")
    
    if len(students) == 0:
        print("NO STUDENT FOUND!")
    else:
        print("\nAvailable students:")
        for student in students:
            print(f"  {student['number']}: {student['name']}")
        
        student_number = input("\nEnter student number to update: ")
        
        student = next((s for s in students if s['number'] == student_number), None)
        if not student:
            print("Student not found!")
        else:
            print(f"\nCurrent information:")
            print(f"  Name: {student['name']}")
            print(f"  Gender: {student['gender']}")
            print(f"  Age: {student['age']}")
            
            print("\nEnter new information:")
            new_name = input("Name: ")
            new_gender = input("Gender: ")
            new_age = input("Age: ")
            
            student["name"] = new_name
            student["gender"] = new_gender
            student["age"] = new_age
            
            print("Student information updated!")

def delete_student():
    print("\n--- DELETE STUDENT ---")
    
    if len(students) == 0:
        print("No students found!")
    else:
        print("\nAvailable students:")
        for student in students:
            print(f"  {student['number']}: {student['name']}")
        
        student_number = input("\nEnter student number to delete: ")
        
        student = next((s for s in students if s['number'] == student_number), None)
        if not student:
            print("Student not found!")
        else:
            deleted_name = student["name"]
            
            students.remove(student)
            
            print(f"{deleted_name} deleted successfully!")

    return True


def exit_program():
    print("\nThank you for using Student Management System!")
    print("Goodbye!")
    return False


def show_menu():
    print("="*40)
    print("STUDENT MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Add Student")
    print("2. Show Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    print("="*40)


menu_options = {
    "1": add_student,
    "2": show_student,
    "3": update_student,
    "4": delete_student,
    "5": exit_program
}


def main():
    running = True
    
    while running:
        show_menu()
        choice = input("\nChoose (1-5): ")
        
        if choice in menu_options:
            if choice == "5":
                running = menu_options[choice]()
            else:
                menu_options[choice]()
        else:
            print("Invalid option! Please choose 1-5.")


if __name__ == "__main__":
    main()