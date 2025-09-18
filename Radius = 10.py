radius = 10
x = int(radius)
e = int(radius*-1)
y = 0

while x <= y:
    e += 2*y + 1
    y += 1

    if e >= 0:
        x -= 1
        e -= 2*x - 1

print(radius)