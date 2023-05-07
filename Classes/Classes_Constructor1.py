# program to calculate profit and loss of product using classes.
class product():
    def __init__(self,name,cp,sp) -> None:
        self.name = name
        self.cp = cp
        self.sp = sp
        self.status = sp - cp
        self.r = "Profit" if self.status >0 else "Loss"
    def info(self):
        print(f"{self.cp} is cost price of {self.name} and selling price is {self.sp} and makes {self.r} of {self.status}")

a = product("Pen",10000,20000)
a.info()