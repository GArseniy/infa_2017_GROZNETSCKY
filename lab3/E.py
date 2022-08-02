number = int(input())
answer = 1
is_degree_of_2 = True
while number > 1:
    if number % 2:
        is_degree_of_2 = False
    answer += 1
    number //= 2
print(answer - is_degree_of_2)
