n = int(input())
max_number = n
while n:
    max_number = max(max_number, n)
    n = int(input())
print(max_number)
