import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build(root_i):
	val,left_i,right_i = nodes[root_i - 1]
	tnode = TreeNode(val)
	if left_i > 0 and left_i <= n and left_i != root_i:
		tnode.left = build(left_i)
	if right_i > 0 and right_i <= n and right_i != root_i:
		tnode.right = build(right_i)
	return tnode

def search(root):
	if root == None:
		return True
	if (root.left != None and root.left.val >= root.val) or (root.right != None and root.right.val <= root.val):
		return False
	return search(root.left) and search(root.right)



# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()
n,root_i = map(int,lines[0].strip().split(' '))
nodes = [map(int,i.strip().split(' ')) for i in lines[1:]]
root = build(root_i)

if search(root):
	print('true')
else:
	print('false')

