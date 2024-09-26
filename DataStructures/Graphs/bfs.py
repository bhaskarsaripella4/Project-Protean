import collections


def BFS(graph,root):

    visited, queue = set(), collections.deque()
    # add the first node to visited to start
    visited.add(root)
    queue.append(root) #add the root as a graph entry

    # loop through graph and add to visited if not visited before. also add unvisited to queue and pop
    while queue:

        # obtain a node from the queue.
        vertex = queue.popleft()
        print(str(vertex)+ " ", end = "")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)




if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    BFS(graph, 0)
