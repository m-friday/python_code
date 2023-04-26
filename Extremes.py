numbers = [3, 30, 5, 16, 6]
input("Enter a max number: ")
input("Enter a min number: ")
max = numbers[1]
min = numbers[0]
for number in numbers:
    if number <= max:
        sum = max + min
print(sum)
