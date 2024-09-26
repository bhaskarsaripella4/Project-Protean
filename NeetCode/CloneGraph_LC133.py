


class Node:
    def __init__(self, val = 0, neighbours = None):
        self.val = val
        self.neighbours = neighbours if neighbours is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node': #it is a return annotation.
        # oldToNew = {}
        #
        # def dfsClone(node):
        #     if node in oldToNew:
        #         return oldToNew[node]
        #
        #     copy = Node(node.val)
        #     oldToNew[node] = copy
        #     for nei in node.neighbours:
        #         copy.neighbours.append(dfsClone(nei))
        #     return copy
        #
        # return dfsClone(node) if node else None

        oldToNew = {} #this is empty hashmap

        def dfsClone(node):
            if node in oldToNew[node]:
                return oldToNew[node] #node exists in hashmap, hence no need to create another copy

            copy = Node(node.val)
            oldToNew[node] = copy #assign the copy node to hashmap
            for nei in node.neighbours:
                copy.neighbours.append(dfsClone(node))
            return copy

        return dfsClone(node) if node else None

tests = [
    ([[2,4],[1,3],[2,4],[1,3]]),
    ([[2,4],[1,3],[2,4],[1,3]])
]

Solution.cloneGraph("",Node([[2,4],[1,3],[2,4],[1,3]]))