# python3

class HeapBuilder:
	def __init__(self):
		self._swaps = []
		self._data = []
    
	def size(self):
		return len(self._data)

	def ReadData(self):
		n = int(input())
		self._data = [int(s) for s in input().split()]
		assert n == len(self._data)

	def WriteResponse(self):
		print(len(self._swaps))
		for swap in self._swaps:
			print(swap[0], swap[1])
		
	def leftChildIndex(self, i):
		left_child_i = 2*i + 1
		if left_child_i >= self.size():
			return -1
		return left_child_i
		
	def rightChildIndex(self, i):
		right_child_i = 2*i + 2
		if right_child_i >= self.size():
			return -1
		return right_child_i
		
	def siftDown(self, i):
		"""
		Sifts down - follows Build heap algorithm in lecture but min heap properties
		"""
		minIndex = i
		l = self.leftChildIndex(i)
		r = self.rightChildIndex(i)
		if l != -1 and self._data[l] < self._data[minIndex]:
			minIndex = l
		if r != -1 and self._data[r] < self._data[minIndex]:
			minIndex = r
		if i != minIndex:
			#swap elements
			self._swaps.append((i, minIndex))
			self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
			self.siftDown(minIndex)
		

	def GenerateSwaps(self):
		
		for i in range(self.size()//2, -1, -1):
			self.siftDown(i)
    

	def Solve(self):
		self.ReadData()
		self.GenerateSwaps()
		self.WriteResponse()

if __name__ == '__main__':
	heap_builder = HeapBuilder()
	heap_builder.Solve()
