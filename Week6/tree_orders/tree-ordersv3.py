# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size



class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
	def __init__(self):
		self.root = None

	def getRoot(self):
		return self.root

	def add(self, val):
		if(self.root is None):
			self.root = Node(val)
		else:
			self._add(val, self.root)

	def add_root(self, val):
		if(self.root is None):
			self.root = Node(val)
    		
	def add_left(self, val, node):
		if(node.l is None):
			node.l = Node(val)
			
	def add_right(self, val, node):
		if(node.r is None):
			node.r = Node(val)
    
    
	def _add(self, val, node):
		if(val < node.v):
			if(node.l is not None):
				self._add(val, node.l)
			else:
				node.l = Node(val)
		else:
			if(node.r is not None):
				self._add(val, node.r)
			else:
				node.r = Node(val)

	def find(self, val):
		if(self.root is not None):
			return self._find(val, self.root)
		else:
			return None

	def _find(self, val, node):
		if(val == node.v):
			return node
		elif(val < node.v and node.l != None):
			self._find(val, node.l)
		elif(val > node.v and node.r != None):
			self._find(val, node.r)

	def deleteTree(self):
        # garbage collector will do this for us. 
		self.root = None

	def inOrder(self):
		self.result = []
		if(self.root is not None):
			self._inOrder(self.root, self.result)
			return self.result
		else:
			print('root is None')

	def _inOrder(self, node, result):
		if(node != None):
			self._inOrder(node.l, self.result)
			self.result.append(node.v)
			self._inOrder(node.r, self.result)

	def read(self):
		self.n = int(sys.stdin.readline())
		self.key = [0 for i in range(self.n)]
		self.left = [0 for i in range(self.n)]
		self.right = [0 for i in range(self.n)]
		for i in range(self.n):
			[a, b, c] = map(int, sys.stdin.readline().split())
			self.key[i] = a
			self.left[i] = b
			self.right[i] = c
		
		
		
		self.add_root(self.key[0])
		if self.left[0] != -1: 
			self.add_left(self.key[self.left[0]], self.root)
		if self.right[0] != -1:
			self.add_right(self.key[self.right[0]], self.root)
				
		for i in range(1, self.n):
			if self.left[i] != -1:
				self.add_left(self.key[self.left[i]], Node(self.key[i]))
			if self.right[i] != -1:
				self.add_right(self.key[self.right[i]], Node(self.key[i]))



def main():
	tree = Tree()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	#print(" ".join(str(x) for x in tree.preOrder()))
	#print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
