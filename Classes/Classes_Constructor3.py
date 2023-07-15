class function():
    def __init__(self,**kw) -> None:
        self.id = kw.get("id")
        self.roll = kw.get("roll")
        self.name = kw.get("name")
    def info(self):
        print(f"""{self.id} ----Name--> {self.name} ----Roll No.--> {self.roll} """)
    x = int(input("How many Entries? "))
    for i in range(x):
        id = int(input("Enter id"))
        roll = input("Enter roll")
        name = input("Enter name")
        a = function(id,roll,name)
        a.info()

        