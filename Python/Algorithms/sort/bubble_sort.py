#!/usr/bin/python3

def bubblesort(data):
    while True:
        is_sorted = True

        for i in range(0, len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i  + 1], data[i]

                is_sorted = False

        if is_sorted:
            break

if __name__ == '__main__':
    list_numbers = [3, 1, 0, 6, 2, 32, 12, 9, 10, 4, 16, 23, 54, 92]
    bubblesort(list_numbers)
    print(list_numbers)

    list_letters = ['p', 's', 'r', 'a', 'k', 'l', 'm', 'b', 'f', 'h', 'c', 'u', 'z']
    bubblesort(list_letters)
    print(list_letters)