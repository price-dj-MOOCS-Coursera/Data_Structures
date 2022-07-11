from sys import stdin


class Node:
	def __init__(self, key, sum, left, right, parent):
		(self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

	def equals(self, node):
		return self.key == node.key

class SplayTree:
	def __init__(self):
		self.root = None
		self.header = Node(None, None, None, None, None) #For splay()

	def insert(self, key):
		if (self.root == None):
			self.root = Node(key, None, None, None, None)
			return
            
	def update(self, v):
		if v == None:
			return
		v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
		if v.left != None:
			v.left.parent = v
		if v.right != None:
			v.right.parent = v

		self.splay(key)
		if self.root.key == key:
			# If the key is already there in the tree, don't do anything.
			return

		n = Node(key)
		if key < self.root.key:
			n.left = self.root.left
			n.right = self.root
			self.root.left = None
		else:
			n.right = self.root.right
			n.left = self.root
			self.root.right = None
		self.root = n

	def remove(self, key):
		self.splay(key)
		if key != self.root.key:
			raise 'key not found in tree'

        # Now delete the root.
		if self.root.left== None:
			self.root = self.root.right
		else:
			x = self.root.right
			self.root = self.root.left
			self.splay(key)
			self.root.right = x

	def findMin(self):
		if self.root == None:
			return None
		x = self.root
		while x.left != None:
			x = x.left
		self.splay(x.key)
		return x.key

	def findMax(self):
		if self.root == None:
			return None
		x = self.root
		while (x.right != None):
			x = x.right
		self.splay(x.key)
		return x.key

	def find(self, key):
		if self.root == None:
			return None
		self.splay(key)
		if self.root.key != key:
			return None
		return self.root.key

	def isEmpty(self):
		return self.root == None
    
	def splay(self, key):
		l = r = self.header
		t = self.root
		self.header.left = self.header.right = None
		while True:
			if key < t.key:
				if t.left == None:
					break
				if key < t.left.key:
					y = t.left
					t.left = y.right
					y.right = t
					t = y
					if t.left == None:
						break
				r.left = t
				r = t
				t = t.left
			elif key > t.key:
				if t.right == None:
					break
				if key > t.right.key:
					y = t.right
					t.right = y.left
					y.left = t
					t = y
					if t.right == None:
						break
				l.right = t
				l = t
				t = t.right
			else:
				break
		l.right = t.left
		r.left = t.right
		t.left = self.header.right
		t.right = self.header.left
		self.root = t
		return self.root


	# Searches for the given key in the tree with the given root
	# and calls splay for the deepest visited node after that.
	# Returns pair of the result and the new root.
	# If found, result is a pointer to the node with the given key.
	# Otherwise, result is a pointer to the node with the smallest
	# bigger key (next value in the order).
	# If the key is bigger than all keys in the tree,
	# then result is None.
	def find1(self, key): 
		v = self.root
		last = self.root
		next = None
		while v != None:
			if v.key >= key and (next == None or v.key < next.key):
				next = v    
			last = v
			if v.key == key:
				break    
			if v.key < key:
				v = v.right
			else: 
				v = v.left      
		root = splay(last)
		return (next, root)

        
	def split(self, root, key):  
		(result, root) = find1(root, key)  
		if result == None:    
			return (root, None)  
		right = splay(result)
		left = right.left
		right.left = None
		if left != None:
			left.parent = None
		update(left)
		update(right)
		return (left, right)

  
	def merge(self, left, right):
		if left == None:
			return right
		if right == None:
			return left
		while right.left != None:
			right = right.left
		right = splay(right)
		right.left = left
		update(right)
		return right	
	
	
	
	def sum(self, fr, to): 
		
		(left, middle) = split(self.root, fr)
		(middle, right) = split(middle, to + 1)
		ans = 0
		# Complete the implementation of sum        
        
st = SplayTree()        
MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
	line = stdin.readline().split()
	if line[0] == '+':
		x = int(line[1])
		st.insert((x + last_sum_result) % MODULO)
	elif line[0] == '-':
		x = int(line[1])
		st.remove((x + last_sum_result) % MODULO)
	elif line[0] == '?':
		x = int(line[1])
		print('Found' if st.find((x + last_sum_result) % MODULO) else 'Not found')
	elif line[0] == 's':
		l = int(line[1])
		r = int(line[2])
		res = st.sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
		print(res)
		last_sum_result = res % MODULO
