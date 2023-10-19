user_integer = int(input("How many integers would you like to enter? "))

if user_integer < 2:
    print("Please input an integer >=2")
else:
    first_integer = int(input("Please enter the first integer: "))
    min_integer = first_integer
    max_integer = first_integer

    for i in range(2, user_integer +1):
        integer = int(input(f"Please enter integer {i}:"))
        min_integer = min(min_integer, integer)
        max_integer = max(max_integer, integer)

    print("min:", min_integer)
    print("max:", max_integer)