import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

import weakref


class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

class Record:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Record({self.name})"


registry = weakref.WeakValueDictionary()
r1 = Record("Potter")
r2 = Record("Granger")
temp = Record("Weasley")
registry["Potter"] = r1
registry["Granger"] = r2
registry["Weasley"] = temp
print("Реестр сразу после создания:", list(registry.items()))

del temp
print("\nПосле удаления временной ссылки temp (Weasley):")
print("Реестр:", list(registry.items())) 

del r2
print("\nПосле удаления сильной ссылки r2 (Granger):")
print("Реестр:", list(registry.items())) 

print("\nr1 жив благодаря сильной ссылке:", registry.get("Potter"))