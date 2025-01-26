a, b = 1, 1
for _ in range(7):
    print(a, end=" ")
    a, b = b, a + b
