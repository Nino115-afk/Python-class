score_1 = int(input("Enter score 1: "))
score_2 = int(input("Enter score 2: "))
score_3 = int(input("Enter score 3: "))
score_4 = int(input("Enter score 4: "))
score_5 = int(input("Enter score 5: "))
Total = score_1 + score_2 + score_3 + score_4 + score_5
avg = Total / 5

if avg >=90 and avg <=100:
    Grade = "A"
elif avg >=80 and avg <90:
    Grade = "B"
elif avg >=70 and avg <80:
    Grade = "C"
elif avg >=60 and avg <70:
    Grade = "D"
elif avg <=50 and avg <60:
    Grade = "E"
elif avg <=0 and avg <50:
    Grade = "F"

print("==== OUTPUT ====")
print("Grade is : ", Grade)