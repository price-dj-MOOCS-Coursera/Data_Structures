# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
	def __init__(self):
		self.n = 0
		self.parent = []
		self.nodes = []
		
	
	def read(self):
		self.n = int(sys.stdin.readline())
		self.parent = list(map(int, sys.stdin.readline().split()))
		self.nodes = [0] * self.n
	
	def pathLength(self, nodeName, memo = {}):
		#Returns path length from given node to the root
		parent = self.parent[nodeName]
		if parent == -1:
			return 1

		if self.nodes[nodeName]:
			return self.nodes[nodeName]
		
		if self.parent[nodeName] in memo:
			return memo[self.parent[nodeName]]
		else:
			self.nodes[nodeName] = 1 + self.pathLength(self.parent[nodeName], memo)
			memo[self.parent[nodeName]] = self.nodes[nodeName]
		return self.nodes[nodeName]
        
	def compute_height(self):
		#Computes the tree height
		return max([self.pathLength(i) for i in range(self.n)])

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
