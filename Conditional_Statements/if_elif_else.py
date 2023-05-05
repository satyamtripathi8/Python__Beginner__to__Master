# find largest among three numbers
x=int(input("Enter first number"))
y=int(input("Enter second number"))
z=int(input("Enter third number"))
if x>y and x>z:
    print(x,"is Largest")
elif y>z:
    print(y,"is Largest")
else:
    print(z,"is Largest")