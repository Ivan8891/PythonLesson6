def input_number (text):
	n = int(input(text))
	return n


n = input_number("Введите число начала прогрессии: ")
a = input_number("Введите шаг прогресии: ")
d = input_number("Введите количество чисел в прогоессии: ")
list_number = [n]
for i in range (d - 1):
	n += a
	list_number.append(n)
print(list_number)
