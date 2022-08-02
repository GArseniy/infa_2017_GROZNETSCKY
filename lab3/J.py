n = int(input())
max_number = n
counter = 1
while n:
    if n > max_number:
        max_number = n
        counter = 1
    elif n == max_number:
        counter += 1
    n = int(input())
print(counter)
