class Node:

	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None
	
	def setValue(self, value):
		self.value = value
	def setNext(self, next):
		self.next = next
	def setPrev(self, prev):
		self.prev = prev
	def getValue(self):
		return self.value
	def getNext(self):
		return self.next
	def getPrev(self):
		return self.prev

class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def add(self, new_data):
		temp = Node(new_data)
		if(self.head == None):
			self.head = temp
		else:
			node = Node(new_data)
			node = self.head
			while(node.getNext() != None):
				node = node.getNext()
			node.setNext(temp)
		self.length += 1


	def swapping(self, index1, index2):
		if index1 >= self.length or index2 >= self.length:
			print('out of bounds')
		if index1 == index2:
			return
		if index2 < index1:
			self.swapping(index)

		prev1 = None
		curr1 = self.head
		z = 0
		while z < index1:
			prev1 = curr1
			curr1 = curr1.getNext()
			z += 1
		
		prev2 = curr1
		curr2 = curr1.getNext()
		i = index1 + 1
		while i < index2:
			prev2 = curr2
			curr2 = curr2.getNext()
			i += 1
		
		if prev1 == None:
			self.head = curr2
		else:
			prev1.setNext(curr2)
		
		yNext = curr2.getNext()
		if prev2 == curr1:
			curr2.setNext(curr1)
		else:
			curr2.setNext(curr1.getNext())

		if prev2 == curr1:
			curr2.setNext(curr1)
		else:
			prev2.setNext(curr1)
		curr1.setNext(yNext)

		
	def swap(self, x, y):
		if(x==y):
			return
		prevX = None
		currX = self.head
		while currX != None and currX.getValue() != x:
			prevX = currX
			currX = currX.getNext()
		prevY = None
		currY = self.head
		while currY != None and currY.getValue() != y:
			prevY = currY
			currY = currY.getNext()

		if currX == None or currY == None:
			return
		if prevX != None:
			prevX.setNext(currY)
		else:
			self.head = currY
		if prevY != None:
			prevY.setNext(currX)
		else:
			self.head = currX
		
		temp = currX.getNext()
		currX.setNext(currY.getNext())
		currY.setNext(temp)

	def removeIndex(self, index):
		if(index == 0):
			self.head = head.next
		else:
			n = Node(index)
			n = self.head
			n1 = Node(index)
			i = 0
			for i in range(i < index - 1):
				n = n.next
				i += 1
			n1 = n.next
			n.next = n1.next
		self.length -= 1


	def removeValue(self, val):
		temp = self.head
		if(temp != None):
			if(temp.getValue() == val):
				self.head = temp.getNext()
				temp = None
				return
				
		while(temp != None):
			if temp.getValue() == val:
				break
			prev = temp
			temp = temp.getNext()
				
		if temp == None:
			print(f'Value {val} Not Found')
			return
		
		prev.setNext(temp.getNext())
		temp = None
		self.length -= 1

		

	def removeDuplicate(self):
		current = self.head
		index = None
		temp = None

		if self.head == None:
			return
		else:
			while current != None:
				temp = current
				index = current.getNext()
				while index != None:
					if(current.getValue() == index.getValue()):
						temp.setNext(index.getNext())
					else:
						temp = index
					index = index.getNext()
				current = current.getNext()
			self.length -= 1
				


	def swapHT(self):
		self.swapping(0, self.length-1)

	def printList(self):
		temp = self.head
		while(temp):
			print(temp.getValue() , end=" --> ")
			temp = temp.getNext()
		print(" null")


# Main
ll = LinkedList()
ll.add(1)
ll.add(5)
ll.add(3)
ll.add(5)
ll.add(10)
ll.add(17)
ll.add(20)

print("Before : ", end="")
ll.printList()

print("\nRemove Value : 10")
print("After : ", end="")
ll.removeValue(10)
ll.printList()

print("\nRemove Duplicate")
print("After : ", end="")
ll.removeDuplicate()
ll.printList()

print("\nSwap Head To Tail")
print("After : ", end="")
ll.swapHT()
ll.printList()
