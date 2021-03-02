# PATH = '/Users/ritvarun/Developer/My Projects/py_stl/linear_structure/lists.py'
# import importlib.util
# spec = importlib.util.spec_from_file_location("py_stl.linear_structure.lists", PATH)
# foo = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(foo)
# l = foo.SinglyLinkedList()
# print(type(l))


class _Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BinarySearchTree:
	def __init__(self):
		self.root = None

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
		print(res)

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
		print(res)

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
		print(res)

	def delete(self, element):
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

				root.data = temp.data
				root.right = self.delete(root.right, root.val)
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

	def to_bst(self, arr):
		for element in arr:
			self.insert(element)

	def leaf_order(self):
		if self.root is None:
			return None
		stack = [self.root]
		res = [self.root.val]
		while stack:
			pass


if __name__ == '__main__':
	t = BinarySearchTree()
	t.insert(5)
	t.insert(1)
	t.insert(3)
	t.insert(7)
	t.insert(4)
	t.insert(8)
	t.preorder()
	t.inorder()
	t.postorder()
	t.delete(-4)
	t.inorder()
	# print(t.search(8))