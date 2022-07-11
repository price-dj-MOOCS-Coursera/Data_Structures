# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

class DisjSets(object):
    def __init__(self, n):
        self._parent = range(n)
        self._rank = [0] * n

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
            elif self._rank[root_i] > self._rank[root_j]:
                self._parent[root_j] = root_i
            else:
                self._parent[root_i] = root_j
                self._rank[root_j] += 1



def getParent(table):
    # find parent and compress path
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    
    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)
    
