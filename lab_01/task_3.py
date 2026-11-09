from math import *
x = 17
y = 5
print("x + y =", x + y, "| тип:", type(x + y))
print("x - y =", x - y, "| тип:", type(x - y))
print("x * y =", x * y, "| тип:", type(x * y))
print("x / y =", x / y, "| тип:", type(x / y))
print("x // y =", x // y, "| тип:", type(x // y))
print("x % y =", x % y, "| тип:", type(x % y)) 
print("x ** y =", x ** y, "| тип:", type(x ** y))

print("2 ** 1000 =", 2 ** 1000)

result = 0.1 + 0.2
print("result =", result)
print("result == 0.3:", result == 0.3)
print("result - 0.3:", result - 0.3)
print("math.isclose(result, 0.3):", isclose(result, 0.3))

print('int("42") =', int("42"), "| тип:", type(int("42")))
print('float("3.14") =', float("3.14"), "| тип:", type(float("3.14")))
print("str(2026) =", str(2026), "| тип:", type(str(2026)))
print("bool(0) =", bool(0), "| тип:", type(bool(0)))
print("bool(-1) =", bool(-1), "| тип:", type(bool(-1)))
print('bool("") =', bool(""), "| тип:", type(bool("")))
print('bool("False") =', bool("False"), "| тип:", type(bool("False")))
print("complex(2, -3) =", complex(2, -3), "| тип:", type(complex(2, -3)))
print("Действительная часть:", complex(2, -3).real)
print("Мнимая часть:", complex(2, -3).imag)