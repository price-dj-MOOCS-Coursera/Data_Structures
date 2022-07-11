# python3

from sys import stdin
from wx import NullAcceleratorTable

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
    if v == None:
        return
    v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v

def smallRotation(v):
    parent = v.parent
    if parent == None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
    parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
    else: 
        grandparent.right = v

def bigRotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)    
    else: 
    # Zig-zag
        smallRotation(v)
        smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            smallRotation(v)
        break
    bigRotation(v)
    return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key): 
    v = root
    last = root
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
    update(root)
    return (next, root)

def split(root, key):  
    (result, root) = find(root, key)  
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

  
def merge(left, right):
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

  
# Code that uses splay tree to solve the problem
                                    
root = None

# def insert(x):
#     global root
#     (left, right) = split(root, x)
#     new_vertex = None
#     if right == None or right.key != x:
#         new_vertex = Vertex(x, x, None, None, None)  
#     root = merge(merge(left, new_vertex), right)

def insert(key):
        global root
        if (root == None):
            root = Vertex(key, key, None, None, None)
            return
            
        root, next = find(root, key)
        #self.update(self.root)
        if root.key == key:
            # If the key is already there in the tree, don't do anything.
            return

        v = Vertex(key, key, None, None, None)
        if key < root.key:
            v.left = root.left
            v.right = root
            root.left = None
        else:
            v.right = root.right
            v.left = root
            root.right = None
        root = v
        #self.update(self.root)
  
def erase(x): 
    global root
    # Implement erase yourself
    # Splay(Next(x))
    # Splay(x)
    # Delete(x)
    splay(nextNode(x))
    splay(x)
    delete(x)

def search(x): 
    global root
    # Implement find yourself
  
    return False
  
def sum(fr, to): 
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    ans = 0
    # Complete the implementation of sum

    return ans

def nextNode(x):
    if x.right != None:
        return leftDescendant(x.right)
    else:
        return rightAncestor(x)
     
def leftDescendant(x):
    if x.left == None:
        return x
    else:
        return leftDescendant(x.left)
     
def rightAncestor(x):
    if x.key < x.parent.key:
        return x.parent
    else:
        return rightAncestor(x.parent)
 
def delete(x):
    global root
    if x.left == None:
        root = x.right
    else:
        righttree = x.right
        root = splay(x.left)
        root.right = righttree
            
    
# def delete(self):
#         
#     """
#     Remove value of self from BinaryTree. Works in conjunction with remove
#     method in BinaryTree
#     """
# 
#     if self.left == self.right == None:
#         return None
#     if self.left == None:
#         return self.right
#     if self.right == None:
#         return self.left
# 
#     child = self.left
#     grandchild = child.right
#     if grandchild:
#         while grandchild.right:
#             child = grandchild
#             grandchild = child.right
#         self.key = grandchild.key
#         child.right = grandchild.left
#     else:
#         self.left = child.left
#         self.key = child.key
# 
#     return self    
# 
# def remove(x, key):
#     global root
#     if root and root.key == key:  # special case for removing the root
#         root = root.delete()
#         return
# 
#     else:                        # general case, removing a child node of some parent
#         parent = x.root
#         while parent:
#             if key < parent.key:
#                 child = parent.left
#                 if child and child.value == key:
#                     parent.left = child.delete()
#                     return
#                 parent = child
#             else:
#                 child = parent.right
#                 if child and child.value == key:
#                     parent.right = child.delete()
#                     return
#                 parent = child
# 
#     # if we get here, value was never found, perhaps raise an exception?
#     

MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
    line = stdin.readline().split()
    if line[0] == '+':
        x = int(line[1])
        insert((x + last_sum_result) % MODULO)
    elif line[0] == '-':
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
    elif line[0] == '?':
        x = int(line[1])
        print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO
