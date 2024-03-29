from graphs.adjacency_list import adj_list


# Count path of back_tracking
def dfs(node, target, adja_list, visit):
    if node in visit:
        return 0
    if node == target:
        return 1

    count = 0
    visit.add(node)
    for neighbour in adja_list[node]:
        count += dfs(neighbour, target, adja_list, visit)
    visit.remove(node)

    return count


print(dfs("A", "D", adj_list, set()))
