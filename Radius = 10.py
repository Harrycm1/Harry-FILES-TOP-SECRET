radius = 10
y = 0
x = int(radius)
e = int(radius*-1)


while x > y:
    e += 2*y + 1
    y += 1

    if e >= 0:
        x -= 1
        e -= 2*x - 1
        print(f"{x, y}")

    elif e < 0:
        x -= 0
        print(f"{x, y}")
