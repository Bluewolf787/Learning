def binary_search(numbers, lowest, highest, numberToFind):
    if highest >= lowest:
        middleOfList = (highest + lowest) // 2
        if numbers[middleOfList] == numberToFind:
            return middleOfList
        elif numbers[middleOfList] > numberToFind:
            return binary_search(numbers, lowest, middleOfList - 1, numberToFind)
        else:
            return binary_search(numbers, middleOfList + 1, highest, numberToFind)
    else:
        return -1


startNumber = int(input("Enter a start number: "))
endNumber = int(input("Enter a end number: "))
numberToFind = int(input("Enter a number to find: "))

numberList = list(range(startNumber, endNumber + 1, 1))

result = binary_search(numberList, 0, len(numberList) - 1, numberToFind)

if result == -1:
    print("The number " + str(numberToFind) + " is not a element of the list.")
else:
    print("The number " + str(numberToFind) + " is a element of the list at the index " + str(result))