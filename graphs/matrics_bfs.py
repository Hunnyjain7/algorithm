from collections import deque


def bfs(grid):
    rows, cols = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == rows - 1 or c == cols - 1:
                return length
            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(dr + r, dc + c) < 0 or r + dr == rows or c + dc == cols or (r + dr, c + dc) in visit or
                        grid[r + dr][c + dc] == 1):
                    continue
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1


matrics = [[0, 0, 0, 0],
           [1, 1, 0, 0],
           [0, 0, 0, 1],
           [0, 1, 0, 0]]
print(bfs(matrics))
