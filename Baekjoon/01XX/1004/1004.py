case = int(input())

for i in range(case):
    x1, y1, x2, y2 = map(int, input().split())
    a = int(input())
    total = 0
    for j in range(a):
        cx, cy, r = map(int, input().split())
        d1 = ((x1 - cx)**2 + (y1-cy)**2)**0.5
        d2 = ((x2 - cx)**2 + (y2-cy)**2)**0.5
        if(d1 < r and d2 > r) or (d1 > r and d2 < r):
            total += 1
   print(total)
