t = int(input("NO. of test cases"))
for i in range(t):
    x,y,a = map(int, input("Enter value of minimum , maximum age limit and current age: ").split())
    if a>=x and a<y:
        print("YES")
    else:
        print("No")