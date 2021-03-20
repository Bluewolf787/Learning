#!/usr/bin/python3

def linear_search(data, value):
    for i in range(0, len(data) - 1):
        if data[i] == value:
            return i
    
    return -1

if __name__ == '__main__':
    value = int(input('> '))

    list_numbers = [1, 5, 2, 14, 23, 32, 12, 8, 3, 9, 0, 6]
    index = linear_search(list_numbers, value)
    print('The value is in the list at index %d' % index)