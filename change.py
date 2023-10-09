cents = int(input("Please enter an amount in cents less than a dollar "))

Q = cents // 25
cents %= 25
D = cents // 10
cents %= 10
N = cents // 5
cents %= 5

P = cents


print("Your change will be:")
print("Quarters:",Q)
print("Dimes:",D)
print("Nickels:",N)
print("Pennies:",P)