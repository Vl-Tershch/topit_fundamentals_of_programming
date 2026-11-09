import sys
import tracemalloc
import gc

samples = {
    "пустой список": [],
    "список из 10 int": list(range(10)),
    "кортеж из 10 int": tuple(range(10)),
    "строка из 10 символов": "0123456789",
    "целое число": 10,
    "None": None,
}

for name, obj in samples.items():
    print(f"{name}: {sys.getsizeof(obj)} байт")

grow = []
last_size = sys.getsizeof(grow)
print(f"len={len(grow)} size={last_size} байт (начальное выделение)")

for i in range(100):
    grow.append(i)
    size = sys.getsizeof(grow)
    if size != last_size:
        print(f"len={len(grow)} size={size} байт (выделение изменилось)")
        last_size = size

def measure(name, numbers_func):
    gc.collect()
    tracemalloc.start()
    
    obj = numbers_func()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    size = sys.getsizeof(obj)
    print(f"{name}: текущее={current / 1024:.3f} КБ, пиковое={peak / 1024:.3f} КБ, size={size} байт")
    
    return current, peak, size

list_curr, list_peak, list_size = measure("list(range(100_000))", lambda: list(range(100_000)))
range_curr, range_peak, range_size = measure("range(100_000)", lambda: range(100_000))