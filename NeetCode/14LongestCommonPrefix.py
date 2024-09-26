"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix amongst the input strings.
"""

# using a trie data structure to solve this
# alternate is to use in-built function os.path.commonprefix(ListOfStrings)

NUM_ALPHABETS = 26
indexs = 0
class TrieNode:
    def __init__(self):
        self.isLeaf = False
        self.children = [None]*NUM_ALPHABETS

# If node is not in trie, insert
def insert(key, root):

    temp = root
    for i in range(len(key)):
        index = ord(key[i]) - ord('a') # ascii values
        if temp.children[index] == None:
            temp.children[index] = TrieNode()
        temp = temp.children[index]
    temp.isLeaf = True



def createTrie(arr, n, root):
    for i in range(n):
        insert(arr[i],root)

def countChildren(node):
    count = 0
    for i in range(NUM_ALPHABETS):
        if node.children[i] != None:
            count+=1
            global indexs
            indexs = i
    return count


def longestCommonPrefix(arr, root):
    temp = root
    prefix = ""
    while (countChildren(temp) ==1 and temp.isLeaf == False):
        temp = temp.children[indexs]
        prefix += chr(97 + indexs)

    return prefix or "No common Prefix"


arr = ["cartoon", "referee", "carzole", "carbonate"]
arr = ["flower","flow","flight"]
arr = ["dog","racecar","car"]
n= len(arr)
print("size of array",n)
root = TrieNode()
createTrie(arr,n,root)
print(longestCommonPrefix(arr,root))

