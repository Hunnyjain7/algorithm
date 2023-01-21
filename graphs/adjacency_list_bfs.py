# Shortest path from node to target
from collections import deque

from graphs.adjacency_list import adj_list


def bfs(node, target, adja_list):
    length = 0
    visit = set()
    queue = deque()
    queue.append(node)
    visit.add(node)

    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length

            for neighbour in adja_list[curr]:
                if neighbour not in visit:
                    queue.append(neighbour)
                    visit.add(neighbour)
        length += 1
    return length


print(bfs("A", "E", adj_list))
