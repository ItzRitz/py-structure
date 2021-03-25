# from ..linear_structure.lists import SinglyLinkedList, DoublyLinkedList


class _Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


class BinarySearchTree:

	def __init__(self, arr=None):
		self.root = None
		self.arr = arr
		if arr is not None:
			self._to_bst()

	def insert(self, val):
		node = _Node(val)

		if self.root is None:
			self.root = node
			return
		else:
			self._insert(self.root, node)

	def _insert(self, curr, node):
		if node.val > curr.val:
			if curr.right:
				self._insert(curr.right, node)
			else:
				curr.right = node
		elif node.val < curr.val:
			if curr.left:
				self._insert(curr.left, node)
			else:
				curr.left = node

	def preorder(self):
		if self.root is None:
			print('Empty Tree')
			return
		res = []

		def _preorder(node):
			if node:
				res.append(node.val)
				_preorder(node.left)
				_preorder(node.right)
		_preorder(self.root)
		return res

	def inorder(self):
		if self.root is None:
			print('Empty Tree')
			return
		res = []

		def _inorder(node):
			if node:
				_inorder(node.left)
				res.append(node.val)
				_inorder(node.right)
		_inorder(self.root)
		return res

	def postorder(self):
		if self.root is None:
			print('Empty Tree')
			return
		res = []

		def _postorder(node):
			if node:
				_postorder(node.left)
				_postorder(node.right)
				res.append(node.val)
		_postorder(self.root)
		return res

	def delete(self, element):
		if self.root is None:
			return None
		if element == self.root.val and not self.root.right and not self.root.left:
			self.root = None

		def _delete(root, element):
			if not root:
				return None

			if element > root.val:
				root.right = _delete(root.right, element)
			elif element < root.val:
				root.left = _delete(root.left, element)
			else:
				# if root->right is None
				if not root.right:
					return root.left

				# if root->left is None
				if not root.left:
					return root.right

				# find the inorder successor
				temp = root.right
				while temp.left:
					temp = temp.left

				root.val = temp.val
				root.right = _delete(root.right, root.val)

			return root
		_delete(self.root, element)

	def search(self, element):
		if element == self.root:
			return self.root

		def _search(node, element):
			if node is None:
				return None

			if node.val == element:
				return node

			if node.val < element:
				return _search(node.right, element)
			else:
				return _search(node.right, element)

		node = _search(self.root, element)
		return node if node else "Node Not Found"

	def _to_bst(self):
		for element in self.arr:
			self.insert(element)

	def leaf_order(self):
		if self.root is None:
			return None
		stack = [self.root]
		res = []
		while stack:
			l = len(stack)
			temp = []
			for _ in range(l):
				node = stack.pop(0)
				if node:
					temp.append(node.val)
				else:
					if stack != []:
						temp.append(None)
					continue

				if node.left:
					stack.append(node.left)
				elif len(stack) > 0:
					stack.append(None)
				if node.right:
					stack.append(node.right)
				elif len(stack) > 0:
					stack.append(None)
			if temp != []:
				res.append(temp)
		return res

	def max(self):
		if self.root is None:
			return None
		
		def _max(node):
			if node.right is None:
				return node
			else:
				return _max(node.right)
			
		return _max(self.root).val

	def min(self):
		if self.root is None:
			return None
		
		def _min(node):
			if node.left is None:
				return node
			else:
				return _min(node.left)

		return _min(self.root).val


if __name__ == '__main__':
	t = BinarySearchTree([5,2,6,7,3,1,5,7,10])
	print(t.min())
	print(t.postorder())
	