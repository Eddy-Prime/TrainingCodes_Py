number_list = [89, 78, 6, 5, 4, 1]

for i in range(0, len(number_list)):
    for j in range(i + 1, len(number_list)):
        if number_list[i] > number_list[j]:
            number_list[i], number_list[j] = number_list[j], number_list[i]

print(number_list)