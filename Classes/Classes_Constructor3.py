class function():
    def __init__(self,id,roll,name) -> None:
        self.id = id
        self.roll = roll
        self.name = name
    def info(self):
        print(f"""{self.id} ----Name--> {self.name} ----Roll No.--> {sel.roll} """)
    x = int(input("How many Entries? "))
    for i in range(x):
        id = int(input("Enter id"))
        name = input("Enter name")
        roll = input("Enter roll")
        a = function(id,roll,name)
        a.info()

        