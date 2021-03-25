import random

def bubble_sort(arr, show_steps=False, reversed=False):
	for i in range(len(arr)):
		for j in range(0, len(arr)-i-1):
			if reversed:
				if(arr[j] < arr[j+1]):
					arr[j], arr[j+1] = arr[j+1], arr[j]
			else:
				if(arr[j] > arr[j+1]):
					arr[j], arr[j+1] = arr[j+1], arr[j]


		if show_steps:
			print(arr)
	return arr

def insertion_sort(arr, show_steps=False, reversed=False): # reversed doesn't work yet

	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >=0 and key < arr[j] :
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key

		if show_steps:
			print(arr)
	return arr

def selection_sort(arr, show_steps=False, reversed=False):  # reversed doesn't work yet
	minn = 0
	t = 0
	while t < len(arr):
		for i in range(t+1, len(arr)):
			if arr[i] < arr[minn]:
				minn = i
		arr[t], arr[minn] = arr[minn], arr[t]

		if show_steps:
			print(arr)
		t+=1
		minn = t
	return arr

def _merge(arr1, arr2, show_steps, reversed):
	res = []
	i = j = 0
	while i<len(arr1) and j<len(arr2):
		if not reversed:
			if arr1[i] <= arr2[j]:
				res.append(arr1[i])
				i+=1
			else:
				res.append(arr2[j])
				j+=1
		else:
			if arr1[i] >= arr2[j]:
				res.append(arr1[i])
				i+=1
			else:
				res.append(arr2[j])
				j+=1

	if i < len(arr1):
		res += arr1[i:]
	if j < len(arr2):
		res += arr2[j:]

	if show_steps:
		print(res)
	return res

def merge_sort(arr, show_steps=False, reversed=False):
	if len(arr) <= 1:
		return arr

	mid = len(arr)//2

	left = merge_sort(arr[:mid], show_steps=show_steps, reversed=reversed)
	right = merge_sort(arr[mid:], show_steps=show_steps, reversed=reversed)
	return _merge(left, right, show_steps=show_steps, reversed=reversed)

def _partition(arr, l, r, show_steps, reversed):
	randPivot = random.randint(l,r)
	
	arr[randPivot], arr[r] = arr[r], arr[randPivot] 

	x = arr[r]
	i = l-1
	for j in range(l, r):
		if arr[j] <= x:
			i +=1 
			if j!=i:
				arr[j], arr[i] = arr[i], arr[j]

	arr[i+1], arr[r] = arr[r], arr[i+1]

	if show_steps:
		print(arr)

	return i+1

def quick_sort(arr, show_steps=False, reversed=False):
	try:
		temp = arr[2]
	except IndexError:
		return arr

	def _quick_sort(arr, l, r, show_steps, reversed):
		if l >= r:
			return

		m = _partition(arr, l, r, show_steps, reversed)
		_quick_sort(arr, l, m-1, show_steps, reversed)
		_quick_sort(arr, m+1, r, show_steps, reversed)

		return arr

	l = 0
	r = len(arr)-1
	return _quick_sort(arr, l, r, show_steps, reversed) # reverse doesn't work yet

def _partition_3way(arr, l, r, show_steps, reversed):
	x = arr[l]
	low = l
	high = l
	for j in range(l + 1 ,r+1):
		if arr[j] < x:
			y = arr[j]
			arr[j] = arr[high + 1]
			arr[high + 1] = arr[low]
			arr[low] = y
			low = low + 1
			high = high + 1
		elif arr[j] == x:
			arr[high + 1], arr[j] = arr[j], arr[high + 1]
			high = high + 1

		if show_steps:
			print(arr)
	return [low, high]

def quick_sort_3way(arr, show_steps=False, reversed=False):
	try:
		temp = arr[2]
	except IndexError:
		return arr

	def _quick_sort_3way(arr, l, r, show_steps, reversed):
		if l >= r:
			return

		m1,m2 = _partition_3way(arr, l, r, show_steps, reversed)
		_quick_sort_3way(arr, l, m1-1, show_steps, reversed)
		_quick_sort_3way(arr, m2+1, r, show_steps, reversed)

		return arr

	l = 0
	r = len(arr)-1
	return _quick_sort_3way(arr, l, r, show_steps=show_steps, reversed=reversed) # reversed doesn't work yet


if __name__ == '__main__':
	import time

	leng = 10
	arr = []
	for _ in range(leng):
		arr.append(random.randint(1, leng*(random.randint(1,4))))

	t = time.time()

	arr = merge_sort(arr, show_steps=False)
	print("Result array :", arri)
	t1 = time.time() - t
	print("Time Elapsed : ",t1, " seconds")






















