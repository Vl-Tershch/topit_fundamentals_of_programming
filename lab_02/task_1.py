a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))


first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

second = [10, 20, 30]

print("first  ==", first, "id:", id(first))
print("second ==", second, "id:", id(second))
print("first == second:", first == second) 
print("first is second:", first is second)

second.append(40)
print("После изменения нового second:")
print("first  ==", first)
print("second ==", second)

from copy import *

config_a ={
        "name": "Проект_1",
        "members": ["Романенко", "Лобанов"],
        "run_args": ["--debug", "--port=8000"], 
    }

config_b = config_a

print("=== До изменений (присваивание) ===")
print("config_a:", config_a)
print("config_b:", config_b)

config_b["name"] = "Проект_2 (копия)"
config_b["members"].append("Быков")
config_b["run_args"].append("--verbose")

print("=== После изменений config_b ===")
print("config_a:", config_a) 
print("config_b:", config_b)
print("config_a is config_b -", config_a is config_b)

config_c = deepcopy(config_a)
config_c["name"] = "Проект_2 (независимый)"
config_c["members"].append("Купитман")
config_c["run_args"].append("--release")

print("=== После изменений config_c (глубокая копия) ===")
print("config_a:", config_a)
print("config_c:", config_c)

print("config_a is config_c -", config_a is config_c)

assert config_c is not config_a
assert config_c["members"] is not config_a["members"]
assert config_c["run_args"] is not config_a["run_args"]
assert "Купитман" not in config_a["members"]

print("\nИтог:")
print("- config_a и config_b — один и тот же объект (включая вложенные списки)")
print("- config_a и config_c — полностью независимые объекты на всех уровнях")