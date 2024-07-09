
### 2. `main.py`

#python
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

# def longest_path(graph: list) -> int:
#     # Your implementation goes here
#     pass

# # Helper function to perform topological sort
# def topological_sort(graph):
#     # Your implementation goes here
#     pass

# # Function to calculate longest path using topological sort
# def calculate_longest_path(graph, topo_order):
#     # Your implementation goes here
#     pass


# def longest_path(graph):
#     # Helper function to perform topological sort
#     def topological_sort(graph):
#         n = len(graph)
#         visited = [False] * n
#         topo_stack = []
        
#         def dfs(node):
#             visited[node] = True
#             for neighbor, weight in graph[node]:
#                 if not visited[neighbor]:
#                     dfs(neighbor)
#             topo_stack.append(node)
        
#         for i in range(n):
#             if not visited[i]:
#                 dfs(i)
        
#         return topo_stack[::-1]
    
#     # Function to calculate longest path using topological sort
#     def calculate_longest_path(graph, topo_order):
#         n = len(graph)
#         dist = [-float('inf')] * n
        
#         # Initialize distances of nodes with no incoming edges
#         for node in topo_order:
#             if dist[node] == -float('inf'):
#                 dist[node] = 0
        
#         for node in topo_order:
#             if dist[node] != -float('inf'):
#                 for neighbor, weight in graph[node]:
#                     if dist[neighbor] < dist[node] + weight:
#                         dist[neighbor] = dist[node] + weight
        
#         return max(dist)
    
#     topo_order = topological_sort(graph)
#     return calculate_longest_path(graph, topo_order)

# # Example usage (you can remove or comment this part when using the function in a testing setup)
# if __name__ == "__main__":
#     graph = [
#         [(1, 3), (2, 2)],
#         [(3, 4)],
#         [(3, 1)],
#         []
#     ]

#     print(longest_path(graph))  # Output: 7

# from collections import deque

# def longest_path(graph: list) -> int:
#     topo_order = topological_sort(graph)
#     return calculate_longest_path(graph, topo_order)

# def topological_sort(graph):
#     n = len(graph)
#     in_degree = [0] * n
#     for u in range(n):
#         for v, _ in graph[u]:
#             in_degree[v] += 1
    
#     queue = deque([u for u in range(n) if in_degree[u] == 0])
#     topo_order = []
    
#     while queue:
#         u = queue.popleft()
#         topo_order.append(u)
#         for v, _ in graph[u]:
#             in_degree[v] -= 1
#             if in_degree[v] == 0:
#                 queue.append(v)
    
#     return topo_order

# def calculate_longest_path(graph, topo_order):
#     n = len(graph)
#     dp = [0] * n
#     max_path = 0
    
#     for u in topo_order:
#         for v, w in graph[u]:
#             dp[v] = max(dp[v], dp[u] + w)
#         max_path = max(max_path, dp[u])
    
#     return max_path



from collections import deque

def longest_path(graph: list) -> int:
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)

def topological_sort(graph):
    n = len(graph)
    in_degree = [0] * n
    for u in range(n):
        for v, _ in graph[u]:
            in_degree[v] += 1
    
    queue = deque([u for u in range(n) if in_degree[u] == 0])
    topo_order = []
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, _ in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    return topo_order

def calculate_longest_path(graph, topo_order):
    n = len(graph)
    dp = [0] * n
    
    for u in topo_order:
        for v, w in graph[u]:
            dp[v] = max(dp[v], dp[u] + w)
    
    return max(dp)




# from collections import deque

# def longest_path(graph: list):
#     topo_order = topological_sort(graph)
#     length, path = calculate_longest_path(graph, topo_order)
#     print("Longest Path Length:", length)
#     print("Path:", path)

# def topological_sort(graph):
#     n = len(graph)
#     in_degree = [0] * n
#     for u in range(n):
#         for v, _ in graph[u]:
#             in_degree[v] += 1
    
#     queue = deque([u for u in range(n) if in_degree[u] == 0])
#     topo_order = []
    
#     while queue:
#         u = queue.popleft()
#         topo_order.append(u)
#         for v, _ in graph[u]:
#             in_degree[v] -= 1
#             if in_degree[v] == 0:
#                 queue.append(v)
    
#     return topo_order

# def calculate_longest_path(graph, topo_order):
#     n = len(graph)
#     dp = [0] * n
#     prev = [-1] * n  # To keep track of the path
    
#     for u in topo_order:
#         for v, w in graph[u]:
#             if dp[v] < dp[u] + w:
#                 dp[v] = dp[u] + w
#                 prev[v] = u
    
#     # Find the node with the maximum distance
#     max_length = max(dp)
#     end_node = dp.index(max_length)
    
#     # Reconstruct the path
#     path = []
#     while end_node != -1:
#         path.append(end_node)
#         end_node = prev[end_node]
    
#     path.reverse()
    
#     return max_length, path

# # Example graph represented as an adjacency list
# # Each pair (v, w) in graph[u] represents an edge u -> v with weight w
# graph = [
#         [(1, 3), (2, 2)],
#         [(3, 4)],
#         [(3, 1)],
#         []
#     ]

# longest_path(graph)
