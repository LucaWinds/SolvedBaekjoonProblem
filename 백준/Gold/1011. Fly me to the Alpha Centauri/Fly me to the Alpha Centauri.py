import math

TC = int(input())

for i in range(TC):
    x, y = map(int, input().split())
    length = y - x
    d = int(math.sqrt(length))
    if d**2 == length:
        move_count = 2*d - 1
    else:
        move_count = 2*d
        if length > d*(d+1):
            move_count += 1
    print(move_count)
