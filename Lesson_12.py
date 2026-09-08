class Person:
    __id=""
    __name=""
    __gender=""
    def __init__(self):
        self.__id="001"
        self.__name="dara"
        self.__gender="male"
    def output(self):
        print(self.__id)
        print(self.__name)
        print(self.__gender)
p=Person()
p.output()