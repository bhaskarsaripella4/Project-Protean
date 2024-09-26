

# find lowest common ancestor
# given p and q, a number between them must be a node of a binary tree and it must have children (at least 1)

def lowestCommonAncestor(root,p,q):

    cur = root
    while cur:

        if cur.val > p.val and cur.val>q.val:
            lowestCommonAncestor(root.left,p,q)
        elif cur.val<p.val and cur.val<q.val:
            lowestCommonAncestor(root.right,p,q)
        else:
            return cur
