#name
#age
#gender
#score1
#score2
#score3
#total
#average
#def check_grade(average)
#average 90-100 grade A
#average 80-89 grade B
#average 70-79 grade c
#average 60-69 grade d
#average 50-59 grade E
#average <50 grade F
#return grade
#output
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")

score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))

total = score1 + score2 + score3
average = total / 3


def check_grade(average):
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    elif average >= 50:
        grade = "E"
    else:
        grade = "F"

    return grade


grade = check_grade(average)

print("\n===== Output =====")
print("Name:", name)
print("Age:", age)
print("Gender", gender)
print("score 1", score1)
print("Score 2:", score2)
print("Score 3:", score3)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)