from cs50 import get_int

# to get desired input
while True:
    a = get_int("Height: ")
    if a < 9 and a > 0:
        break

# to loop through starting from 1 and go height times
for i in range(1, a + 1):
    # to print space a - i timems as in col = row times
    print(" " * (a - i), end="")
    print("#" * (i), end="")
    print("  ", end="")
    print("#"*(i), end="")
    print("")