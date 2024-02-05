palamdrom

y = x
r = 0

while y != 0:
    a = y % 10
    r = r * 10 + a
    y = y // 10
print(r)
