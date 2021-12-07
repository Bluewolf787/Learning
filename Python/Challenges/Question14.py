sentence = input(': ')

upper_case = 0
lower_case = 0

for letter in sentence:
    if letter.isupper():
        upper_case += 1
    elif letter.islower():
        lower_case += 1

print(f'UPPER CASE: {upper_case}\nLOWER CASE: {lower_case}')