# loop
# for loop
# while loop

for i in range(5):
    print(i, "hello world")
    # 0, 1, 2, 3, 4

print("=========")
for i in range(2, 5):
    print(i, "hello world")
    # 2, 3, 4

print("=========")
for i in range(2, 10, 2):
    print(i, "hello world")
    # 2, 4, 6, 8

# 1 + 2 + 3 + 4 + ... + n
n = int(input("Enter n: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i 
    if i == n:
        print(i, end=" = ")
    else:
        print(i, end=" + ")
print(sum)

# 5 * 10 * 15 * ... * n
n = int(input("Enter n: "))
product = 1
for i in range(5, n + 1, 5 ):
    product = product * i 
    if i == n:
        print(i, end=" = ")
    else:
        print(i, end=" * ")
print(product)

username = "dara"
balance = 1000
while True:
    print("1, view balance")
    print("2, deposit")
    print("3, withdraw")
    print("0, exit")
    op = int(input("Enter your option: "))

    if op == 1:
        print("your balance is:", balance)
    elif op == 2:
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
    elif op == 3:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance")
        else:
            balance = balance - amount
    elif op == 0:
        break