# Visit www.neon.rip for more content!

# Given a directed acyclical graph, return a valid
# topological ordering of the graph.
def topological_sort(edges, n):
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []
    for src, dst in edges:
        adj[src].append(dst)

    top_sort = []
    visit = set()
    for i in range(1, n + 1):
        dfs(i, adj, visit, top_sort)
    top_sort.reverse()
    return top_sort


def dfs(src, adj, visit, top_sort):
    if src in visit:
        return
    visit.add(src)

    for neighbor in adj[src]:
        dfs(neighbor, adj, visit, top_sort)
    top_sort.append(src)
