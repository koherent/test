letter_list = [[' ', 0]]

while True:
    text = input('Введите слово: ')
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

        print(letter_list)