# Multiple Inheritance
class Father:
    _id=""
    _name=""
    def __init__(self,id,name):
        self._id=id
        self._name=name
    def output(self):
        print(self._id)
        print(self._name)
class Mother:
    _Hair="Black"
    def output(self):
        print(self._Hair)
class Son(Father, Mother):
    pass
son=Son("001","Dara")
son.output()