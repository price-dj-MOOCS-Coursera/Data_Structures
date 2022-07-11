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

        def compute_height(self):
                tree = {}
                
                # Replace this code with a faster implementation
                maxHeight = 0
                for i in range(len(self.parent)):
                	if self.parent[i] = -1:
                		tree[i] = lst.append(i for self.parent == i)
                	
                        

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
