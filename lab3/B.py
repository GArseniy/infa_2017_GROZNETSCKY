def is_motion(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return True
    if abs(x1 - x2) == abs(y1 - y2):
        return True
    return False


if is_motion(int(input()), int(input()), int(input()), int(input())):
    print("YES")
else:
    print("NO")