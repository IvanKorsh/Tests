
numbers = []

n1, n2 = 0, 1
i = 0
limit = int(input('How much numbers do you want?'))

while i <= limit:
    numbers.append(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    i += 1

number = int(input("What`s number should be display?"))
print(numbers[numbers[number]])
