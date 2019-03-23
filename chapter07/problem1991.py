import sys
f = sys.stdin
n = int(f.readline())
tree = {}
for i in range(n):
    branch = [ i for i in f.readline().split() ]
    tree[branch[0]]= [branch[1], branch[2]]

start = [i for i in tree.keys()][0]

#  preOrder
def preOrder(startNode):
    print(startNode, end = "")
    [preOrder(i) for i in tree[startNode] if not i == '.' ]
    return ""

def inOrder(startNode):
    tmp = [i for i in tree[startNode] ]
    if not tmp[0] == '.': inOrder(tmp[0])
    print(startNode, end = "")
    if not tmp[1] == '.': inOrder(tmp[1])

def postOrder(startNode):
    tmp = [i for i in tree[startNode]]
    if not tmp[0] == '.': postOrder(tmp[0])
    if not tmp[1] == '.': postOrder(tmp[1])
    print(startNode, end="")

preOrder(start)
print("")
inOrder(start)
print("")
postOrder(start)