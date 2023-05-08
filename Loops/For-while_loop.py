x=0
while (x==0):
    x= int(input("Press 0 to continue and 1 to exit. "))
    if x==1:
        break
    else:
        a = int(input("Enter Number to check given number is armstrong or not:"))
        cnt =0
        ans = 0
        b = d = a 
        while(a!=0):
            a = a//10
            cnt = cnt+1
        for i in range(cnt):
            c = b%10
            b = b//10
            ans += c**cnt
        if ans==d:
            print("Armstrong NUmber")
        else:
            print("Not Armstrong Number")

