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

while True:
    print("=====STUDENT MANAGEMENT SYSTEM=====")
    print("1. Add Student")
    print("2. Show Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("\nChoose (1-5): ")
    
    if choice == "1":
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
    
    elif choice == "2":
        print("\n--- SHOW STUDENT ---")
        
        if len(students) == 0:
            print("No students found!")
        else:
            for student in students:
                print(f"\nStudent Number: {student['number']}")
                print(f"  Name: {student['name']}")
                print(f"  Gender: {student['gender']}")
                print(f"  Age: {student['age']}")

    elif choice == "3":
        print("\n--- UPDATE STUDENT ---")
        
        if len(students) == 0:
            print("No students found!")
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
    
    elif choice == "4":
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
    
    elif choice == "5":
        print("\nThank you for using Student Management System!")
        print("Goodbye!")
        break
    
    else:
        print("Invalid option! Please choose 1-5.")