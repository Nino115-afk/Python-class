def grade_student(name, score):
    print("Name: " + name)
    print("Score: ", (score))
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
grade_student("Sokha", 30)
