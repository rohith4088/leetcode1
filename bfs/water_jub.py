from collections import deque
def water_jug(x,y,z):
    visited = set()
    q = deque([(0,0)])
    while q:
        a , b = q.popleft()
        if a == z or b == z or a+b == z:
            return True
        if (a,b) in visited:
            continue
        visited.add((a,b))
        if a < x:
            q.append((x,b))
        if b < y:
            q.append((a,y))
        if a > 0:
            q.append((0,b))

        if b > 0:
            q.append((a,0))
        if a+b >= x:
            q.append((x,b-(x-a)))
        else:
            q.append((a+b,0))
        if a+b >= y:
            q.append((a-(y-b),y))
        else:
            q.append((0,a+b))
        