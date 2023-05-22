# BOH

n = int(input())

b = bin(n)
b = b[2:]
print(b)

o = oct(n)
o = o[2:]
print(o)

h = hex(n)
h = h[2:].upper()
print(h)