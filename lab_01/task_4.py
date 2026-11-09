student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print("Первый символ имени:", student[0])
print("Последний символ имени:", student[3])

first_name = student[:4]
last_name = student[5:]
print("Имя:", first_name)
print("Фамилия:", last_name)

print("Верхний регистр:", student.upper())
print("Нижний регистр:", student.lower())

initials = student[0] + "." + student[5] + "."
print("Инициалы:", initials)

reversed_course = course[::-1]
print("Курс в обратном порядке:", reversed_course)

percent = completed / total * 100
line_percent = "%s - %s: %d/%d (%.1f%%)" % (student, course, completed, total, percent)
line_format = "{} - {}: {}/{} ({:.1f}%)".format(student, course, completed, total, percent)
line_fstring = f"{student} - {course}: {completed}/{total} ({percent}%)"
print("Форматирование через %:", line_percent)
print("Форматирование через .format():", line_format)
print("Форматирование через f-строку:", line_fstring)

symbol = "Я"
decoded_symbol = chr(ord(symbol))
encoded_symbol = symbol.encode("utf-8")
print("Символ:", symbol)
print("ord(symbol):", ord(symbol))
print("chr(ord(symbol)):", decoded_symbol)
print("symbol.encode('utf-8'):", encoded_symbol)
print("Длина UTF-8 последовательности:", len(encoded_symbol))
# student[0] = "Б"