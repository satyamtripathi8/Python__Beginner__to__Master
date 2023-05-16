class character():
    def __init__(self,**kw):
        self.name= kw.get("Name")
        self.intelligence= kw.get("intelligence")
        self.strength = kw.get("strength")
        self.speed = kw.get("speed")
        self.flying_speed = kw.get("flying_speed")
        self.superpower = kw.get("superpower")
    def info(self):
        print(f'''
        Name = {self.name}
        Intelligence: {self.intelligence}
        strength: {self.strength}
        speed: {self.speed}
        flying_speed: {self.flying_speed}
        superpower: {self.superpower}
        ''')
    def input_details(self):
        self.name = input("enter name")
        self.intelligence=input("enter intelligence level")
        self.strength=input("enter strength")
        self.speed=input("enter speed")
        self.flying_speed=input("enter flying_speed")
        self.superpower=input("enter superpower")
spiderman=character()
spiderman.input_details()
spiderman.info()