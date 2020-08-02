class TreeNode():
    def __init__(self ,x):
        self.val = x
        self.right = None
        self.left = None


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left , a.right= b, c
b.left, b.right = d, e
c.left, c.right = f, g

#先序遍历(递归方法)
def pre_rec(node):
    if not node:
        return None
    print(node.val)
    pre_rec(node.left)
    pre_rec(node.right)
#非递归方法
def pre(node):
    stack = [node]
    while len(stack) > 0:
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        node = stack.pop()

#中序遍历(递归方法)
def mid(node):
    if not node:
        return None
    mid(node.left)
    print(node.val)
    mid(node.right)

#后序遍历(递归方法)
def post(node):
    if not node:
        return None
    post(node.left)
    post(node.right)
    print(node.val)
pre(a)
