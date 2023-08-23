import heapq


# Given a list of edges of a connected undirected graph,
# with nodes numbered from 1 to n,
# return a list edges making up the minimum spanning tree.
def minimum_spanning_tree(edges, n):
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []
    for n1, n2, weight in edges:
        adj[n1].append([n2, weight])
        adj[n2].append([n1, weight])

    # Initialize the heap by choosing a single node
    # (in this case 1) and pushing all its neighbors.
    min_heap = []
    for neighbor, weight in adj[1]:
        heapq.heappush(min_heap, [weight, 1, neighbor])

    mst = []
    visit = set()
    visit.add(1)
    while len(visit) < n:
        weight, n1, n2 = heapq.heappop(min_heap)
        if n2 in visit:
            continue

        mst.append([n1, n2])
        visit.add(n2)
        for neighbor, weight in adj[n2]:
            if neighbor not in visit:
                heapq.heappush(min_heap, [weight, n2, neighbor])
    return mst
