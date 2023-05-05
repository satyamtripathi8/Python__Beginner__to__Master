x=int(input("Enter value"))
match x:
    case 1:
        r="MONDAY"
    case 2:
        r="TUESDAY"
    case 3:
        r="WEDNESDAY"
    case 4:
        r="THRUSDAY"
    case 5:
        r="FRIDAY"
    case 6:
        r="SATURDAY"
    case 7:
        r="SUNDAY"
    case _:
        r="Wronggg Numberrrr"
print(r)