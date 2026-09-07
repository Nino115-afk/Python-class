employee=[
    {
        "id":1,
        "name":"dara",
        "position":"web frontend",
        "salary":400
    },
    {
        "id":2,
        "name":"seyha",
        "position":"web backend",
        "salary":500
    },
    {
        "id":3,
        "name":"makara",
        "position":"web fullstack",
        "salary":800
    },
]
print("=====before add data=====")
for emp in employee:
    print(emp['id'])
    print(emp['name'])
    print(emp['position'])
    print(emp['salary'])

employee.append({
    "id":4,
    "name":"thida",
    "position":"python developer",
    "salary":600
})

print("=====after add data=====")
for emp in employee:
    print(emp['id'])
    print(emp['name'])
    print(emp['position'])
    print(emp['salary'])

employee.pop(1)

print("=====after delete data=====")
for emp in employee:
    print(emp['id'])
    print(emp['name'])
    print(emp['position'])
    print(emp['salary'])

for emp in employee:
    if emp["id"] == 4:
        emp["name"] = "sokha"
        emp["position"] = "C++ developer"
        emp["salary"] = 700
        break

print("=====after update data=====")
for emp in employee:
    print(emp["id"])
    print(emp["name"])
    print(emp["position"])
    print(emp["salary"])