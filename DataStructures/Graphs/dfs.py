


def dfs(graph, start, visited = None):

    if visited is None:
        visited = set()
    visited.add(start)
    # print(start)
    for node in graph[start] - visited:
        print(node)
        # if node in visited:
        #     print(node, visited)
        #     continue
        dfs(graph,node,visited)

    return visited



graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')