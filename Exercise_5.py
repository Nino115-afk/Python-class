#create function
#grade_student(name, gender, age, score1, score2, score3)
#output name, gender, age, average score1, score2, score3, and grade
# avg 90=100 A
# avg 80=89 B
# avg 70=79 C
# avg 60=69 D
# avg < 60 F
def grade_student(name, gender, age, score1, score2, score3):
    print("Name: " + name)
    print("Gender: " + gender)
    print("Age:", age)
    print("Score 1:", score1)
    print("Score 2:", score2)
    print("Score 3:", score3)
    average_score = (score1 + score2 + score3) / 3
    print("Average Score: ", average_score)
    print("Total Score: ", score1 + score2 + score3)
    if average_score >= 90:
        print("Grade: A")
    elif average_score >= 80:
        print("Grade: B")
    elif average_score >= 70:
        print("Grade: C")
    elif average_score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
grade_student("Sokha", "Male", 20, 85, 90, 75)
