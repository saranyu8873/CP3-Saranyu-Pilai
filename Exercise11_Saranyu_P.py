x = int(input("x : "))

for i in range(1, x + 1):
    print(" " * (x - i) + "*" * (2 * i - 1))
