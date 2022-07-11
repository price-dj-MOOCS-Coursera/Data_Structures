# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))

class DisjSets(object):
	def __init__(self, n, lines):
		self.parent = list(range(0,n))
		self.rank = [1] * n
		self.lines = lines
		
		
	def ans(self):
		return max(self.lines)

	def find(self, i):
		if self.parent[i] != i:
			self.parent[i] = self.find(self.parent[i])
		return self.parent[i]

	def union(self, i, j, k):
		root_i = self.find(i)
		root_j = self.find(j)
		#root_k = self.find(k)
		if root_i != root_j:
			if self.rank[root_i] < self.rank[root_j]:
				self.parent[root_i] = root_j
				self.lines[root_i] += self.lines[root_j]
				self.lines[root_j] = 0
			elif self.rank[root_i] > self.rank[root_j]:
				self.parent[root_j] = root_i
				self.lines[root_j] += self.lines[root_i]
				self.lines[root_i] = 0
				k = root_j
				
			else:
				self.parent[root_j] = root_i
				self.rank[root_i] += 1
				self.lines[root_i] += self.lines[root_j]
				self.lines[root_j] = 0
		
		return self.lines, k

def merge(destination, source):
	#find function get's parent and compresses path.
    realDestination, realSource = disjointSet.find(destination), disjointSet.find(source)

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    
    disjointSet.lines, k = disjointSet.union(realDestination, realSource, k=-1)
    print(disjointSet.lines, k)
    return True

if __name__ == '__main__':
	disjointSet = DisjSets(n, lines)
	for i in range(m):
		destination, source = map(int, sys.stdin.readline().split())
		merge(destination - 1, source - 1)
		print(disjointSet.ans())
    
