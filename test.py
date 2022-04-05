letter_list = [[' ', 0]]
count = 0
while True:
    text = input('Введите текст: ')
    if text == 'end':
        break
    else:
        for letter in text:
            for i in range(len(letter_list)):
                if letter_list[i][0] == letter:
                    letter_list[i][1] += 1
                    break
            else:
                letter_list.append(list(range(2)))
                letter_list[i + 1][0] = letter

    for index in range(len(letter_list)):
        count += letter_list[index][1]

    for lett in range(len(letter_list)):
        print(letter_list[lett][0], '-', round(
            letter_list[lett][1] / count * 100, 2), '%')