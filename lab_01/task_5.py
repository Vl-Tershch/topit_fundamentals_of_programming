"""Программа формирует информационную карточку вычислительного эксперимента.
Запрашивает у пользователя параметры эксперимента, выполняет вычисления
и выводит оформленный результат с диагностической строкой типов.
"""
researcher_name = input("Введите имя исследователя: ")
experiment_name = input("Введите название эксперимента: ")
runs_count = int(input("Введите количество запусков: "))
run_duration_seconds = float(input("Введите длительность одного запуска (сек): "))
real_part = float(input("Введите действительную часть коэффициента: "))
imag_part = float(input("Введите мнимую часть коэффициента: "))

total_duration_seconds = runs_count * run_duration_seconds
total_duration_minutes = total_duration_seconds / 60
coefficient = complex(real_part, imag_part)
modulus_squared = real_part ** 2 + imag_part ** 2
has_runs = bool(runs_count)

print("=" * 40)
print(f"ЭКСПЕРИМЕНТ: {experiment_name}")
print(f"Исследователь: {researcher_name}")
print(f"Запуски: {runs_count}")
print(f"Общее время: {total_duration_seconds:.2f} с ({total_duration_minutes:.2f} мин)")
print(f"Коэффициент: {coefficient}")
print(f"Квадрат модуля: {modulus_squared:.2f}")
print(f"Есть выполненные запуски: {has_runs}")
print("=" * 40)

print(
    "Типы:"
    f" researcher_name = {type(researcher_name).__name__},"
    f" experiment_name = {type(experiment_name).__name__},"
    f" runs_count = {type(runs_count).__name__},"
    f" run_duration_seconds = {type(run_duration_seconds).__name__},"
    f" real_part = {type(real_part).__name__},"
    f" imag_part = {type(imag_part).__name__}"
)
