from collections import deque

def inside(x, y):
    return 0 <= x < 8 and 0 <= y < 8

with open("in.txt") as f:
    knight = f.readline().strip()
    pawn = f.readline().strip()

kx, ky = ord(knight[0]) - 97, ord(knight[1]) - 49
px, py = ord(pawn[0]) - 97, ord(pawn[1]) - 49
moves = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1),
         (-2, 1)]

danger = set()
if inside(px - 1, py - 1):
    danger.add((px - 1, py - 1))
if inside(px + 1, py - 1):
    danger.add((px + 1, py - 1))

used = [[False] * 8 for _ in range(8)]
parent = [[None] * 8 for _ in range(8)]
q = deque([(kx, ky)])
used[kx][ky] = True
while q:
    x, y = q.popleft()
    if (x, y) == (px, py):
        break

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if inside(nx, ny) and not used[nx][ny]:
            if (nx, ny) in danger and (nx, ny) != (px, py):
                continue
            used[nx][ny] = True
            parent[nx][ny] = (x, y)
            q.append((nx, ny))
path = []
cur = (px, py)
while cur != (kx, ky):
    path.append(cur)
    cur = parent[cur[0]][cur[1]]
path.append((kx, ky))
path.reverse()
with open("out.txt", "w") as f:
    for x, y in path:
        f.write(chr(x + 97) + chr(y + 49) + "\n")