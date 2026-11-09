import gc
import sys
import tracemalloc
from dataclasses import dataclass

@dataclass
class Measurement:
    name: str
    n_items: int
    object_size_bytes: int
    current_kb: float
    peak_kb: float

def measure_container(name, numbers):
    gc.collect()
    tracemalloc.start()
    obj = numbers()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    try:
        n_items = len(obj)
    except TypeError:
        n_items = 1
    return Measurement(
        name=name,
        n_items=n_items,
        object_size_bytes=sys.getsizeof(obj),
        current_kb=current / 1024,
        peak_kb=peak / 1024,
    )

def collect_measurements():
    return [
        measure_container("Empty list", lambda: []),
        measure_container("List (10 ints)", lambda: list(range(10))),
        measure_container("Tuple (10 ints)", lambda: tuple(range(10))),
        measure_container("String (10 chars)", lambda: "0123456789"),
        measure_container("Int (10)", lambda: 10),
        measure_container("None", lambda: None),
        measure_container("list(range(100_000))", lambda: list(range(100_000))),
        measure_container("range(100_000)", lambda: range(100_000)),
    ]

def print_report(measurements):
    headline = f"{'Сценарий':<24}{'N':>8}{'sizeof, Б':>12}{'current, КБ':>14}{'peak, КБ':>12}"
    print(headline)
    print("-" * len(headline))
    for m in measurements:
        print(
            f"{m.name:<24}{m.n_items:>8}{m.object_size_bytes:>12}"
            f"{m.current_kb:>14.3f}{m.peak_kb:>12.3f}"
        )
    list = next(m for m in measurements if m.name == "list(range(100_000))")
    range = next(m for m in measurements if m.name == "range(100_000)")
    ratio_peak = list.peak_kb / range.peak_kb
    print(f"Отношение peak(list) / peak(range): {ratio_peak:.2f}x")

data = collect_measurements()
print_report(data)