#program to print wheather given number is palindrome or not using while loop.
x=int(input("Enter number"))
a = x
ans = 0
while(x>0):
    y = x%10
    x = x//10
    ans = ans*10 + y
print(ans)
print("Palindrome") if (a == ans) else print("Not Palindrome")