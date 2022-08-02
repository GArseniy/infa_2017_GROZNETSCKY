def leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("YES")
        return
    print("NO")
    return


leap_year(int(input()))
