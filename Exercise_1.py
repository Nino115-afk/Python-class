code = int(input("Enter code: "))
name = input("Enter name: ")
price = float(input("Enter price: "))
qty = int(input("Enter quantity: "))

total = price * qty


if total >=1 and total <= 10:
    discount = 10
elif total > 10 and total <= 20:
    discount = 20
elif total > 20 and total <= 30:
    discount = 30
elif total > 30 and total <= 40:
    discount = 40
elif total > 40 and total <= 50:
    discount = 50
elif total > 50 and total <= 60:
    discount =60
elif total > 60:
    discount = 70

payment = total - total * discount / 100

print("==== OUTPUT ====")
print("code is : ", code)
print("name is : ", name)
print("price is : ", price)
print("quantity is : ", qty)
print("total is : ", total)
print("discount is : ", discount)
print("payment is : ", payment)