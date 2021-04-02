class MaxHeap:
	def __init__(self):
		self.heapq = [0]
		self.heap_size = 0

	def insert(self, val):
		if self.heapq == [0]:
			self.heapq.append(val)
		else:
			self.heapq.append(val)
			self._buildHeap(self.heap_size-1)
		self.heap_size +=1

	def _buildHeap(self, size):
		temp = self.heapq[size]

		i = size

		while i > 1 and temp > self.heapq[i//2]:
			self.heapq[i] = self.heapq[i//2]

			i = i//2
		self.heapq[i] = temp

	def display(self):
		if self.heapq != [0]:
			print(self.heapq[1:])
		else:
			print("Empty HEAP")

	def make_heap(self, arr):
		arr.insert(0,0)
		self.heapq = arr
		for i in range(2,len(self.heapq)):
			self._buildHeap(i)

	def heapify(self):
		for i in range(2,len(self.heapq)):
			self._buildHeap(i)

	def heap_pop(self):
		if self.heapq == [0]:
			return
		self.heapq[1], self.heapq[-1] = self.heapq[-1], self.heapq[1] # as heapq[0] = 0
		s = self.heapq.pop()
		self.heapify()
		return s	

	def heap_sort(self):
		arr = [0] # as heapq[0] must be 0
		while self.heapq != [0]:
			arr.append(self.heap_pop())
		self.heapq = arr 
		self.display()

class MinHeap:
	def __init__(self):
		self.heapq = [0]

	def insert(self, val):
		if self.heapq == [0]:
			self.heapq.append(val)
		else:
			self.heapq.append(val)
			self._buildHeap(len(self.heapq)-1)

	def _buildHeap(self, size):
		temp = self.heapq[size]
		i = size

		while i > 1 and temp < self.heapq[i//2]:
			self.heapq[i] = self.heapq[i//2]

			i = i//2
		self.heapq[i] = temp

	def display(self):
		if self.heapq != [0]:
			print(self.heapq[1:])
		else:
			print("Empty HEAP")

	def make_heap(self, arr):
		arr.insert(0,0)
		self.heapq = arr
		for i in range(2,len(self.heapq)):
			self._buildHeap(i)

	def heapify(self):
		for i in range(2,len(self.heapq)):
			self._buildHeap(i)

	def heap_pop(self):
		if self.heapq == [0]:
			return
		self.heapq[1], self.heapq[-1] = self.heapq[-1], self.heapq[1] # as heapq[0] = 0
		s = self.heapq.pop()
		self.heapify()
		return s	

	def heap_sort(self):
		arr = [0] # as heapq[0] must be 0
		while self.heapq != [0]:
			arr.append(self.heap_pop())
		self.heapq = arr 
		self.display()


if __name__ == '__main__':
	h = MinHeap()
	arr = [10,20,30,25,5,40,35]
	h.make_heap(arr)
	h.heapify()
	h.display()
	h.heap_sort()
	# print(h.heap_pop())
	# print(h.heap_pop())
	# h.display()




