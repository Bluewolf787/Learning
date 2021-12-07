sequence = input(': ')

nums = []
for num in sequence.split(','):
    if int(num) % 2 != 0:
        nums.append(num)

print(nums)
