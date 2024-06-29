x = float(input("x 좌표값 : "))
y = float(input("y 좌표값 : "))

r = (((x - 3) ** 2) + ((y - 4) ** 2)) ** (1 / 2)

if r <= 10:
    msg = "원의 내부에 있음"
else:
    msg = "원의 외부에 있음"

print(round(r, 3), ":", msg)