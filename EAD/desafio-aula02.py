matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

a, b = 0, 0

for y, x in enumerate(matriz):
    a += x[y]
    b += (x[-(y+1)])

print(a + b)