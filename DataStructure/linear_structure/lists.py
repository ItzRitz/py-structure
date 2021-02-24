class _Singly_Node:

	def __init__(self, val):
		self.val = val
		self.next = None

class SinglyLinkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.internal_stack = []
		self.list_size = 0
	
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
				item = None
			self._del_from_stack(index)
			return

	def len(self):
		return self.list_size

	def is_there(self, item):
		isFound = filter(lambda x: x.val==item, self.internal_stack)
		return True if isFound else False

	def to_sll(self, array):
		for element in array:
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
		self.tail.next = other.head
		self.tail = other.tail
		self.internal_stack += other.internal_stack

	# Methods to add --> sort, to_bst, to_dbll, reverse aka __reversed__
	def __reversed__(self):
		pass

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

if __name__ == '__main__':
	c = SinglyLinkedList()
	lst = [1,2,3,4,5,6]
	c.to_sll(lst)
	c.display()
	print([i.val for i in c.internal_stack])
	c.reverse()
	c.display()
	print([i.val for i in c.internal_stack])






























