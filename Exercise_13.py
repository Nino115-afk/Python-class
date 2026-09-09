#class Employee
#data member : id, name, gender, position, salary
#consturactor with parameter
#function member : input(), output()

class Employee:
    __id=""
    __name=""
    __gender=""
    __position=""
    __salary=""
    def __init__(self, id, name, gender, position, salary):
        self.__id=id
        self.__name=name
        self.__gender=gender
        self.__position=position
        self.__salary=salary
    def input(self):
        self.__id=input("Enter id: ")
        self.__name=input("Enter name: ")
        self.__gender=input("Enter gender: ")
        self.__position=input("Enter position: ")
        self.__salary=float(input("Enter salary: "))
    def output(self):
        print(self.__id)
        print(self.__name)
        print(self.__gender)
        print(self.__position)
        print(self.__salary)
employee=Employee()
employee.input()
employee.output()