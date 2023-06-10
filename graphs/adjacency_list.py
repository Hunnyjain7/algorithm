class GraphNode:
    """GraphNode used for adjacency list"""

    def __init__(self, val):
        self.val = val
        self.neighbors = []


# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

adj_list = {}

for first, second in edges:
    if first not in adj_list:
        adj_list[first] = []
    if second not in adj_list:
        adj_list[second] = []
    adj_list[first].append(second)

print(adj_list)
