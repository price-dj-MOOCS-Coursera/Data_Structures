# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

class DisjSets(object):
	def __init__(self, n, lines):
		self._parent = list(range(0,n))
		self._rank = [1] * n
		self._lines = lines
		self._ans = max(self._lines)

	def find(self, i):
		if self._parent[i] == i:
			return i
		else:
			self._parent[i] = self.find(self._parent[i])
			return self._parent[i]

	def union(self, i, j):
		root_i = self.find(i)
		root_j = self.find(j)
		if root_i != root_j:
			if self._rank[root_i] < self._rank[root_j]:
				self._parent[root_i] = root_j
				self._lines[root_i] += self._lines[root_j]
				self._lines[root_j] = 0
			elif self._rank[root_i] > self._rank[root_j]:
				self._parent[root_j] = root_i
				self._lines[root_j] += self._lines[root_i]
				self._lines[root_i] = 0
			else:
				self._parent[root_i] = root_j
				self._rank[root_j] += 1
				self._lines[root_j] += self._lines[root_i]
				self._lines[root_i] = 0
		
			return self._lines



#def getParent(table):
    # find parent and compress path
    #return parent[table]

def merge(destination, source):
	#find function get's parent and compresses path.
    realDestination, realSource = disjointSet.find(destination), disjointSet.find(source)

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    
    disjointSet._lines = disjointSet.union(realSource, realDestination)
    print(disjointSet._lines)
    return True

#if __name__ == '__main__':
disjointSet = DisjSets(n, lines)
for i in range(m):
	destination, source = map(int, sys.stdin.readline().split())
	merge(destination - 1, source - 1)
	print(max(disjointSet._lines))
    
