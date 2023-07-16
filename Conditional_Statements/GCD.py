#Taking Input numbers
x,y = map(int, input().split())
l=[]
li=[]
#Finding factors of first number
for i in range(1,x+1):
    if x%i==0:
        li.append(i)
#Finding factors of second number
for i in range(1, y+1):
    if y%i==0:
        l.append(i)
lis=[]
#Finding common factors 
for i in li:
    for j in  l:
        if i==j:
            lis.append(i)
#Finding largest one
print("GCD: ",max(lis))
            