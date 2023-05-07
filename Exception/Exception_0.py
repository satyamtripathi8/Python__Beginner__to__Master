try:
    x = int(input("Enter number from 10 is divide: "))
    num = 10/x
    print(num)
except ZeroDivisionError as e:
    print("Number can't be divided by zero! ")
except ValueError as e:
    print("You doesn't enter valid number! ")
    print(e)
finally:
    print("Code always run")