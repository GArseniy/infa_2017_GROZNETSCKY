counter = 0
n = int(input())
while n:
    counter += not (n % 2)
    n = int(input())
print(counter)
