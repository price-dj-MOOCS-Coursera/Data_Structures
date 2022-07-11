# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

n = 5

parent = [4, -1, 4, 1, 1]
class TreeHeight:
	def read(self):
		self.n = int(sys.stdin.readline())
		self.parent = list(map(int, sys.stdin.readline().split()))

class Tree(object):
    def __init__(self, root, key):
    	self.root = root
    	self.key = key
    	self.child = None
    
    
    def insert_child(self, newNode):
    	if self.child == None:
        	#Parent node is the one the insert_rc method is called on,
        	#so we pass self as the root parameter
        	self.child = Tree(self, newNode)
    	else:
        	t = Tree(self, newNode)
        	self.child = t
        
def buildTree(n, parent):        
	
	tree = Tree()
	for vertex in range(n):
		i = vertex
		while i != -1:
			i = parent[i]
			tree.append(i)
	return tree

print(buildTree(n, parent))

