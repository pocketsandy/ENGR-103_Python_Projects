hailstone = 1000
while hailstone != 1:
        if hailstone % 2 == 0:
            hailstone = hailstone/2
        else:
            hailstone = (hailstone * 3 + 1)
        print(hailstone)