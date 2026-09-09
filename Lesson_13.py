#constructor with parameter
class Person:
    __name=""
    __gender=""
    __age=""
    def __init__(self, name, gender, age):
        self.__name=name
        self.__gender=gender
        self.__age=age
    def output(self):
        print(self.__name)
        print(self.__gender)
        print(self.__age)
person=Person("dara", "male", 20)
person.output()
person=Person("sokha", "male", 21)
person.output()