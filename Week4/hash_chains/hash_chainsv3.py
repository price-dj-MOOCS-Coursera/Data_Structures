#python3

import collections

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

class MapBase(collections.MutableMapping):
	"""
	Our own abstract base class that includes a nonpublic Item class.
	"""

	#------------------------------- nested Item class -------------------------------
	class _Item:
		"""
		Lightweight composite to store key-value pairs as map items.
		"""
		__slots__ = '_key'

		def __init__(self, k):
			self._key = k
			


		def __eq__(self, other):
			return self._key == other._key 	# compare items based on their keys

		def __ne__(self, other):
			return not (self == other) 		# opposite of eq

		def __lt__(self, other):
			return self._key < other._key 	# compare items based on their keys



class UnsortedTableMap(MapBase):
	"""
	Map implementation using an unordered list.
	"""

	def __init__(self):
		"""
		Create an empty map.
		"""
		self._table = [] 	# list of Items

	def __getitem__(self, k):
		"""
		Return value associated with key k (raise KeyError if not found).
		"""
		for item in self._table:
			if k == item._key:
				return item._key
		raise KeyError('Key Error: '+ repr(k))

	def __setitem__(self, k):
		"""
		Assign value v to key k, overwriting existing value if present.
		"""
		for item in self._table:
			if k == item._key: 						# Found a match:
				item._key = k
				return							# and quit
		self._table.insert(0, self._Item(k))	# did not find match for key
		 										



	def __delitem__(self, k):
		"""
		Remove item associated with key k (raise KeyError if not found).
		"""
		for j in range(len(self._table)):
			if k == self._table[j]._key: 	# Found a match:
				self._table.pop(j) 			# remove item
				return 						# and quit
		raise KeyError('Key Error: '+ repr(k))

	def __len__(self):
		"""
		Return number of items in the map.
		"""
		return len(self._table)

	def __iter__(self):
		"""
		Generate iteration of the map s keys.
		"""
		for item in self._table:
			yield item._key 			# yield the KEY


class HashMapBase(MapBase):
	"""
	Abstract base class for map using hash-table with MAD compression.
	"""

	def __init__(self, bucket_count):
		"""
		Create an empty hash-table map.
		"""
		self._table = bucket_count * [None]
		self._multiplier = 263
		#self._n = 0 	# number of entries in the map
		self._prime = 1000000007
		self.bucket_count = bucket_count

	def _hash_function(self, s):
		ans = 0
		for c in reversed(s):
			ans = (ans * self._multiplier + ord(c)) % self._prime
		return ans % self.bucket_count

	#def __len__(self):
		#return self._n

	def __getitem__(self, k):
		j = self._hash_function(k)
		return self._bucket_getitem(j, k) 	# may raise KeyError

	def __setitem__(self, k):
		j = self._hash_function(k)
		self._bucket_setitem(j, k) 				# subroutine maintains self. n
		#if self._n > len(self._table) // 2: 	# keep load factor <= 0.5
			#self._resize(2*len(self._table) - 1) 	# number 2ˆx - 1 is often prime

	def __delitem__(self, k):
		j = self._hash_function(k)
		self._bucket_delitem(j, k) 				# may raise KeyError
		#self._n -= 1

	#def _resize(self, c): 						# resize bucket array to capacity c
		#old = list(self.items()) # use iteration to record existing items
		#self._table = c * [None] # then reset table to desired capacity
		#self._n = 0 # n recomputed during subsequent adds
		#for k in old:
			#self[k] = k # reinsert old key-value pair


class ChainHashMap(HashMapBase):
	"""
	Hash map implemented with separate chaining for collision resolution.
	"""


	def _bucket_getitem(self, j, k):
		bucket = self._table[j]
		if bucket is None:
			return -1									# no match found
		if k in bucket:
			return k								# may raise KeyError

	def _bucket_check(self, j):
		if self._table[j] is None:
			return []
		return self._table[j]
	

	def _bucket_setitem(self, j, k):
		if self._table[j] is None:
			self._table[j] = UnsortedTableMap()		# bucket is new to the table
		#oldsize = len(self._table[j])
		self._table[j].__setitem__(k)
		#if len(self._table[j]) > oldsize:		# key was new to the table
			#self._n += 1 						# increase overall map size

	def _bucket_delitem(self, j, k):
		bucket = self._table[j]
		if bucket is None:
			return -1									# no match found
		if k in bucket:
			bucket.__delitem__(k)									# may raise KeyError


	def __iter__(self):
		for bucket in self._table:
			if bucket is not None:						# a nonempty slot
				for key in bucket:
					yield key
					
	def write_chain(self, chain):
		print(' '.join(chain))
	
	
	def read_query(self):
		return Query(input().split())
        
	def write_search_result(self, was_found):
		print('yes' if was_found else 'no')    
	
	def process_query(self, query):
		if query.type == "check":
			chain = self._bucket_check(query.ind)
			self.write_chain(cur for cur in chain)
			
		else:
			if query.type == 'find':
				hash_s = self._hash_function(query.s)
				return_string = self._bucket_getitem(hash_s, query.s)
				if return_string == query.s:
					self.write_search_result(True)
				else:
					self.write_search_result(False)
			
			elif query.type == 'add':
				hash_s = self._hash_function(query.s)
				self._bucket_setitem(hash_s, query.s)
				
			else:
				hash_s = self._hash_function(query.s)
				self._bucket_delitem(hash_s, query.s)
	
		
		
	def process_queries(self):
		n = int(input())
		for i in range(n):
			self.process_query(self.read_query())
					
					
if __name__ == '__main__':
	bucket_count = int(input())
	proc = ChainHashMap(bucket_count)
	proc.process_queries()
