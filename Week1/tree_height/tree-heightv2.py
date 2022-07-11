# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

n = 5

parent = [4, -1, 4, 1, 1]

class TreeHeight:
		def read(self, n, parent):
				self.n = n
				self.parent = parent
				 
				
		def compute_height(self):
				#if len(self.parent) == 0:
					#return 0
				#else:
					#return max(self.compute_height() for i in self.parent[i]) + 1 
				
				#Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;
                

def main():
	tree = TreeHeight()
	tree.read(n, parent)
	print(tree.compute_height())

threading.Thread(target=main).start()
