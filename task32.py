import random

def random_list(len, min, max):
	list = []
	for i in range(len):
		list.append(random.randint(min, max))
	return list

def input_number (text):
	n = int(input(text))
	return n

def list_index_min_max(list):
	min_index = 0
	max_index = 0
	for i in range(1, len(list)):
		if list[min_index] > list[i]:
			min_index = i
		elif list[max_index] < list[i]:
			max_index = i
	return f"Индекс минирмального значения: {min_index}.\nИндекс максимального значения: {max_index}."
	
list = random_list(input_number("Введите длину массива: "), input_number("Введите минимальное значение: "), input_number("Введите максимальное значение: "))
print(list)
print(list_index_min_max(list))



