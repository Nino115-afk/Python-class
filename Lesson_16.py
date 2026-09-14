# Hierarchical Inheritance
class Person:
    _id=""
    _name=""
    _gender=""
    _subject=""
    def __init__(self, id, name, gender, subject):
        self._id=id
        self._name=name
        self._gender=gender
        self._subject=subject
    def output(self):
        print(self._id)
        print(self._name)
        print(self._gender)
        print(self._subject)
class Teacher(Person):
    pass
class Student(Person):
    pass
stu=Student("001","Sokha","male","English")
stu.output()