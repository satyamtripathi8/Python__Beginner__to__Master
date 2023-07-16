t = int(input("No. of test cases: "))
for i in range(t):
    a,b = map(int, input("Enter No. of buna and patty").split())
    d = min(a,b)
    #to make one need one bun and one patty
    print(d, "No. of burgers")