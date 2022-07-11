# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

	def binary_insert(root, node):
		if root is None:
		    root = node
		else:
		    if root.data > node.data:
		        if root.l_child is None:
		            root.l_child = node
		        else:
		            binary_insert(root.l_child, node)
		    else:
		        if root.r_child is None:
		            root.r_child = node
		        else:
		            binary_insert(root.r_child, node)
	
	def left_insert(root, node):
			            
		            

	def in_order_print(root):
		if not root:
		    return
		in_order_print(root.l_child)
		print root.data
		in_order_print(root.r_child)

	def pre_order_print(root):
		if not root:
		    return        
		print root.data
		pre_order_print(root.l_child)
		pre_order_print(root.r_child) 

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


#class TreeOrders:
  

  #def inOrder(self):
    #self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
                
    #return self.result

  #def preOrder(self):
    #self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
                
    #return self.result

  #def postOrder(self):
    #self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
                
    #return self.result

def main():
	tree = TreeOrders()
	tree.read()
	#print(" ".join(str(x) for x in tree.inOrder()))
	#print(" ".join(str(x) for x in tree.preOrder()))
	#print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
