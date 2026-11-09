import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

def report(article):
    print(f"--- {article} ---")
    print("original:", original, "id:", id(original))
    print("alias:   ", alias, "id:", id(alias))
    print("shallow: ", shallow, "id:", id(shallow))
    print("deep:    ", deep, "id:", id(deep))
    print("id(original[0]):", id(original[0]),
          "id(shallow[0]):", id(shallow[0]),
          "id(deep[0]):", id(deep[0]))
    print("id(original[0][1]):", id(original[0][1]),
          "id(shallow[0][1]):", id(shallow[0][1]),
          "id(deep[0][1]):", id(deep[0][1]))

report("Начальное состояние")

original.append(["Databases", 5])
report("После original.append([Databases, 5])")

original[0][1] = 3
report("После original[0][1] = 3")

wrong_matrix = [[0] * 3] * 3
print("До изменения:", wrong_matrix)

wrong_matrix[0][0] = 1
print("После wrong_matrix[0][0] = 1:", wrong_matrix)
print("Все строки — один и тот же объект:", wrong_matrix[0] is wrong_matrix[1] is wrong_matrix[2])

correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1
print("Корректная матрица:", correct_matrix)
print("Строки независимы:",correct_matrix[0] is not correct_matrix[1])