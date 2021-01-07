x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(f'y= {k}x {b}')