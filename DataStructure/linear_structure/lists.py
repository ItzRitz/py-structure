class _Singly_Node:

	def __init__(self, val):
		self.val = val
		self.next = None

class _Doubly_Node:

	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None

class SinglyLinkedList:

	def __init__(self, arr=None):
		self.head = None
		self.tail = None
		self.internal_stack = []
		self.list_size = 0
		self.arr = arr
		self._to_sll()
	
	def _add_to_stack(self, node, index=-1):
		if index>-1:
			self.internal_stack.insert(index, node)
		else:
			self.internal_stack.append(node)
		self.list_size += 1

	def _del_from_stack(self, index=-1):
		if index>-2 and self.internal_stack != []:
			self.internal_stack.pop(index)
			self.list_size -= 1

	def _get_element_from_stack(self, index):
		if self.internal_stack != []:
			return self.internal_stack[index]

	# Add a value to the list
	def append(self, val):
		node = _Singly_Node(val)
		if self.head is None:
			self.head = node
			self.tail = self.head
			self._add_to_stack(node)
			return

		self.tail.next = node
		self.tail = node
		self._add_to_stack(node)

	# Insert a value to the list at specific index, index in this list starts from 0
	def insert(self, val, index):
		node = _Singly_Node(val)
		if self.head is None:
			self.head = node
			self.tail = self.head
			self._add_to_stack(node)
			return

		if index == 0:
			node.next = self.head
			self.head = node
			self._add_to_stack(node, index)
			return 

		counter = 1
		pointer = self.head

		while pointer.next and counter!=index:
			pointer = pointer.next
			counter+=1

		node.next = pointer.next
		pointer.next = node
		self._add_to_stack(node, index)


		if pointer == self.tail:
			self.tail = node

	def display(self):
		pointer = self.head

		if pointer is None:
			print("Empty List")
			return

		while pointer!=self.tail:
			print(pointer.val,end="->")
			pointer = pointer.next
		print(pointer.val)

	def pop(self):
		if self.head is None or self.internal_stack == []:
			return

		self._del_from_stack()

		if self.internal_stack == []:
			self.head.next = None
			self.head = None
			self.tail = None
			return

		last_node = self._get_element_from_stack(-1)
		last_node = None
		self.tail = self._get_element_from_stack(-1)

	def delete(self, index):
		if self.head is None or self.internal_stack == []:
			return

		if index >= self.list_size or index <0:
			index = self.list_size-1


		if self.internal_stack != []:
			if index == 0:
				self._del_from_stack(index)
				temp_node = self.head.next
				self.head = None
				self.head = temp_node
				return

			item = self._get_element_from_stack(index)
			if item.next:
				item.val = item.next.val
				item.next = item.next.next
			else:
				new_tail = self._get_element_from_stack(index-1)
				self.tail = new_tail
				item = None
			self._del_from_stack(index)
			return

	def len(self):
		return self.list_size

	def is_there(self, item):
		return list(filter(lambda x: x.val==item, self.internal_stack))

	def _to_sll(self):
		if self.arr is None:
			return
		for element in self.arr:
			self.append(element)

	def to_dbll(self):
		lst = self.to_list()
		dll = DoublyLinkedList()
		dll.to_dbll(lst)

		return dll

	def to_list(self, head=None):
		lst = []
		pointer = self.head if head is None else head
		while pointer:
			lst.append(pointer.val)
			pointer = pointer.next
		return lst

	def reverse(self):
		pointer = self.head
		previous = None
		temp_tail = self.head
		while pointer:
			temp = pointer.next
			pointer.next = previous
			previous = pointer
			pointer = temp
		self.tail = temp_tail
		self.head = previous

		start,end = 0, len(self)-1
		while start < end:
			self.internal_stack[start], self.internal_stack[end] = self.internal_stack[end], self.internal_stack[start]
			start+=1
			end-=1

	def sort(self, reverse=False):
		if self.head is None:
			return None

		sort = sorted(self.internal_stack, key=lambda x:x.val, reverse=reverse)

		for i in range(len(sort)-1):
			sort[i].next = sort[i+1]

		self.head = sort[0]
		self.tail = sort[-1]

		return self.head

	def __len__(self):
		return self.list_size

	def __str__(self):
		message = f"Head : {self.head.val}\nTail : {self.tail.val}\nLength : {self.len()}"
		# message = f''' 
		# 			    _______________
		# 			   | Head   --> {self.head.val}  |
		# 			   | Tail   --> {self.tail.val}  |
		# 			   | Length --> {self.len()}  |
		# 			   -----------------'''
		return message

	def __add__(self, other):
		if other == self:
			return
		self.tail.next = other.head
		self.tail = other.tail
		self.internal_stack += other.internal_stack

	# Methods to add --> sort, to_bst, to_dbll
	def __reversed__(self):
		self.reverse()



	def __eq__(self, other):
		return len(self) == len(other)

	def __lt__(self, other):
		return len(self) < len(other) 

	def __dir__(self):
		pass

	def help(self):
		print('''
			_______________________________________________________________________________________
				1. append(val) -> Appends value at the end of the list
				2. insert(val, index) -> Inserts value at index i in the list
				3. display() -> Displays the entire list
				4. pop() -> pops the last element of the list
				5. delete(index) -> deletes an element from the list at index i
				6. len() -> returns the length of the list
				7. is_there() -> checks if an element is present in the list or not
				8. to_sll(array) -> takes a python list and converts it into a SinglyLinkedList
				9. to_list(head=None) -> takes a sll list and converts it into a python list
				10. help() -> provides description of all member methods
			_______________________________________________________________________________________
			''')

class DoublyLinkedList:

	def __init__(self, arr=None):
		self.head = None
		self.tail = None
		self.internal_stack = []
		self.list_size = 0
		self.arr = arr
		self._to_dbll()
	
	def _add_to_stack(self, node, index=-1):
		if index>-1:
			self.internal_stack.insert(index, node)
		else:
			self.internal_stack.append(node)
		self.list_size += 1

	def _del_from_stack(self, index=-1):
		if index>-2 and self.internal_stack != []:
			self.internal_stack.pop(index)
			self.list_size -= 1

	def _get_element_from_stack(self, index):
		if self.internal_stack != []:
			return self.internal_stack[index]

	# Add a value to the list
	def append(self, val):
		node = _Doubly_Node(val)
		if self.head is None:
			self.head = node
			self.tail = self.head
			self._add_to_stack(node)
			return

		self.tail.next = node
		node.prev = self.tail
		self.tail = node
		self._add_to_stack(node)

	# Insert a value to the list at specific index, index in this list starts from 0
	def insert(self, val, index):
		node = _Singly_Node(val)
		if self.head is None:
			self.head = node
			self.tail = self.head
			self._add_to_stack(node)
			return

		if index == 0:
			node.next = self.head
			self.head.prev = node
			self.head = node
			self._add_to_stack(node, index)
			return 

		counter = 1
		pointer = self.head

		while pointer.next and counter!=index:
			pointer = pointer.next
			counter+=1

		node.next = pointer.next
		if pointer.next:
			pointer.next.prev = node
		node.prev = pointer
		pointer.next = node
		self._add_to_stack(node, index)


		if pointer == self.tail:
			self.tail = node

	def display(self, order='f'):
		if order == 'f':
			pointer = self.head
			if pointer is None:
				print("Empty List")
				return

			while pointer!=self.tail:
				print(pointer.val,end="->")
				pointer = pointer.next
			print(pointer.val)
		elif order == 'b':
			pointer = self.tail
			if pointer is None:
				print("Empty List")
				return

			while pointer!=self.head:
				print(pointer.val,end="->")
				pointer = pointer.prev
			print(pointer.val)


	def pop(self):
		if self.head is None or self.internal_stack == []:
			return

		self._del_from_stack()

		if self.internal_stack == []:
			self.head.next = None
			self.head.prev = None
			self.head = None
			self.tail = None
			return

		last_node = self._get_element_from_stack(-1)
		last_node.prev, last_node = None, None
		self.tail = self._get_element_from_stack(-1)

	def delete(self, index):
		if self.head is None or self.internal_stack == []:
			return

		if index >= self.list_size or index <0:
			index = self.list_size-1


		if self.internal_stack != []:
			if index == 0:
				self._del_from_stack(index)
				temp_node = self.head.next
				self.head.next = None
				self.head = None
				self.head = temp_node
				if temp_node:
					self.head.prev = None
				return

			item = self._get_element_from_stack(index)
			if item.next:
				item.next.prev = item.prev
				item.val = item.next.val
				item.next = item.next.next
			else:
				self.tail = item.prev
				item.prev, item = None, None

			self._del_from_stack(index)
			return

	def len(self):
		return self.list_size

	def is_there(self, item):
		return list(filter(lambda x: x.val==item, self.internal_stack))

	def to_sll(self):
		lst = self.to_list()
		sll = SinglyLinkedList()
		sll.to_sll(lst)

		return sll

	def _to_dbll(self):
		if self.arr is None:
			return
		for element in self.arr:
			self.append(element)

	def to_list(self, head=None):
		lst = []
		pointer = self.head if head is None else head
		while pointer:
			lst.append(pointer.val)
			pointer = pointer.next
		return lst

	def index(self, item):
		pass

	def reverse(self):
		self.head, self.tail = self.tail, self.head
		self.internal_stack = self.internal_stack[::-1]

	def __len__(self):
		return self.list_size

	def __str__(self):
		message = f"Head : {self.head.val}\nTail : {self.tail.val}\nLength : {self.len()}"
		# message = f''' 
		# 			    _______________
		# 			   | Head   --> {self.head.val}  |
		# 			   | Tail   --> {self.tail.val}  |
		# 			   | Length --> {self.len()}  |
		# 			   -----------------'''
		return message

	def __add__(self, other):
		if other == self:
			return
		self.tail.next = other.head
		other.head.prev = self.tail
		self.tail = other.tail
		self.internal_stack += other.internal_stack

	def sort(self, reverse=False):
		temp = sorted(self.internal_stack, key=lambda x:x.val, reverse=reverse)

		for i in range(len(temp)-1):
			temp[i].next = temp[i+1]
			temp[i+1].prev = temp[i]
		self.head = temp[0]
		self.tail = temp[-1]

		return self.head

	# Methods to add --> to_bst
	def __reversed__(self):
		self.reverse()

if __name__ == '__main__':
	l = SinglyLinkedList(['h'])
	l.sort(reverse=False)
	l.pop()
	print(l.sort(reverse=False))
	l.display()



	






















