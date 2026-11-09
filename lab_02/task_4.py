import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print("\nАвтоматический сборщик включён:", gc.isenabled())
print("Пороги поколений:", gc.get_threshold())
print("Статистика поколений:", gc.get_stats())

id_first, id_second = id(first), id(second)

del first
del second

collected = gc.collect()
print(f"\ngc.collect() вернул: {collected} собранных объектов")
print("Цикл из first/second больше не достижим ни по одному имени,")
print("но до вызова gc.collect() подсчёт ссылок не мог его освободить,")
print(f"т.к. оба списка (id={id_first}, id={id_second}) ссылались друг на друга.")

gc.disable()
print("Автосборка отключена:", not gc.isenabled())

garbage_ids = []
for _ in range(3):
    a, b = [], []
    a.append(b)
    b.append(a)
    garbage_ids.append((id(a), id(b)))
    del a, b

print("Создано 3 циклических пары, внешние ссылки удалены.")
print("Без ручного вызова gc.collect() эти объекты остаются в памяти.")

collected = gc.collect()
print(f"Ручной gc.collect() собрал: {collected} объектов")

gc.enable()
print("Автосборка снова включена:", gc.isenabled())

node_a = {"name": "Американец","links": []}
node_b = {"name": "Немец","links": []}
node_c = {"name": "Француз","links": []}
independent = {"name": "Русский (независимый)", "links": []}

node_a["links"].append(node_b)
node_b["links"].append(node_c)
node_c["links"].append(node_a)

print("\nСвязи в графе")
for n in node_a,node_b,node_c,independent:
    targets = [t["name"] for t in n["links"]]
    print(f"{n['name']} -> {targets if targets else '[]'}")

before = gc.collect()
print(f"\nСобрано мусора до удаления графа: {before}")

del node_a, node_b, node_c
after = gc.collect()
print(f"Собрано мусора после удаления графа: {after}")

print("\nНезависимый узел по-прежнему доступен:", independent)
assert independent["name"] == "Русский (независимый)"