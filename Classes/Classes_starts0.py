class Teacher():
    salary = 30000
    qualification = "Post Graduate"
    martial_status = "Married"
    experience = "8 years"
    def info(self,name):
        print(name,f"is a teacher qualified upto {self.qualification}, his salary is {self.salary} and having exprience of {self.experience}.Martial status -- {self.martial_status}")
        print()

a = Teacher()
b = Teacher()
c = Teacher()

b.salary = 45000
b.qualification = "Doctrate"
b.martial_status = "Married"
b.experience = "10 years"

c.salary = 50000
c.qualification = "Graduate"
c.martial_status = "Single"
c.experience = "2 years"


a.info("Pawan")
b.info("Aakash")
c.info("Satyam")