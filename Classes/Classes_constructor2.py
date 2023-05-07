class product():
    def __init__(self,name,cp,sp) -> None:
        self.name = name
        self.cp = cp
        self.sp = sp
        self.status = sp - cp
        self.r = "Profit" if self.status >0 else "Loss"
    def info(self):
        print(f"{self.cp} is cost price of {self.name} and selling price is {self.sp} and makes {self.r} of {self.status}")

x = int(input("How many products you have? "))

for i in range(x):
    name =input("Enter product name: ")
    cp = int(input("Enter cost price: "))
    sp = int(input("Enter selling price: "))
    a = product(name,cp,sp)
    a.info()