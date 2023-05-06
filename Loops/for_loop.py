#program to print wheather given number is palindrome or not using for loop.
# x = int(input("Enter Number: "))
# ans = 0
# a = x
# for i in range(len(str(x))): # Here string function is used beacuse len() function  can't use with integer value.
#     y = x%10
#     x = x//10
#     ans = ans*10 + y
# print(ans)
# print("Palindrome") if (a == ans) else print("Not Palindrome")


#program to print wheather given String is palindrome or not using for loop.

b = input("Enter String")
c = " "
for i in range(1,len(b)+1):
    c[i-1] = b[-i]
    print(b[-i])

print(c)