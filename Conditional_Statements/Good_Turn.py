
t = int(input())
li=[]
for i in range(t):
    x,y= input().split()
    x =int(x)
    y= int(y)
    z = x+y
    li.append(z)
    z=0
for i in li:
     if i>6:
         print("YES")
     else:
        print("NO")