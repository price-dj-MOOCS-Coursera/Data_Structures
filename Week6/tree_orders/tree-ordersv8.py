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
		self.nodes = {}

	def getRoot(self):
		return self.root

	def add_root(self, val):
		if(self.root is None):
			self.root = Node(val)
			self.nodes[val] = [self.root,-1,-1]
    		
	def add_left(self, val, node):
		if(node.l is None):
			node.l = Node(val)
			self.nodes[node.v][1] = node.l
			
	def add_right(self, val, node):
		if(node.r is None):
			node.r = Node(val)
			self.nodes[node.v][2] = node.r
    
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
		if(node is not None):
			try:
				self._inOrder(self.nodes[node.v][1], self.result)
			except (IndexError, AttributeError):
				pass
			self.result.append(node.v)
			try:
				self._inOrder(self.nodes[node.v][2], self.result)
			except (IndexError, AttributeError):
				pass
				
	def preOrder(self):
		self.result = []
		if(self.root is not None):
			self._preOrder(self.root, self.result)
			return self.result
		else:
			print('root is None')

	def _preOrder(self, node, result):
		if(node is not None):
			self.result.append(node.v)
			try:
				self._preOrder(self.nodes[node.v][1], self.result)
			except (IndexError, AttributeError):
				pass
			try:
				self._preOrder(self.nodes[node.v][2], self.result)
			except (IndexError, AttributeError):
				pass
				
	def postOrder(self):
		self.result = []
		if(self.root is not None):
			self._postOrder(self.root, self.result)
			return self.result
		else:
			print('root is None')

	def _postOrder(self, node, result):
		if(node is not None):
			try:
				self._postOrder(self.nodes[node.v][1], self.result)
			except (IndexError, AttributeError):
				pass
			try:
				self._postOrder(self.nodes[node.v][2], self.result)
			except (IndexError, AttributeError):
				pass
			self.result.append(node.v)

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
		
		#adding root
		self.add_root(self.key[0])
		
		for i in range(1, self.n):
			self.nodes[self.key[i]] = [Node(self.key[i]),-1,-1]
			
		for i in range(0, self.n):
			if self.left[i] != -1:
				# adding the other left nodes
				self.add_left(self.key[self.left[i]], self.nodes[self.key[i]][0])
			if self.right[i] != -1:
				# adding the other right nodes
				self.add_right(self.key[self.right[i]], self.nodes[self.key[i]][0])
		

def main():
	tree = Tree()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
