# Прогноз до запуска:
# 1)a==b  -> True
# 2)a is b  -> True
# 3)a==c  -> True
# 4)a is c  -> False
a = 1000
b = a
c = int("1000")
print("Типы:", type(a), type(b), type(c))
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b)
print("a is b:", a is b)
print("a == c:", a == c)
print("a is c:", a is c)

c = None
print("c после присваивания None:", c)
print("Корректная проверка c is None:", c is None)

first = "python"
second = "py" + "thon"

print("first == second:", first == second)
print("first is second:", first is second)