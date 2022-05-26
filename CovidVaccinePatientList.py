class Node:
	# constructor for Node class
	def __init__(self, id, name = None, number = None, next = None):
		self.id = id
		self.name = name
		self.number = number
		self.next = next

	# function to return name of patient
	def get_name(self):
		return self.name
	
	# function to return contact number of patient
	def get_number(self):
		return self.number
	
	# function to return patient ID 
	def get_id(self):
		return self.id
    
	# function to return next node
	def get_next(self):
		return self.next
    
	# function to set next node
	def set_next(self, next):
		self.next = next

class LinkedList:
	# constructor for LinkedList class
	def __init__(self, head = None):
		self.head = head

	# function to insert a new node to the Linked List
	def insert(self, id, name, number):

		# initialize a new node with given data
		newNode = Node(id, name, number)

		# set next of new node as head
		newNode.set_next(self.head)

		# let head point to the new node
		self.head = newNode

	# function to search for patient information using patient ID
	# and return the name and contact number
	def search(self, id):

		# initialize current to head
		current = self.head
		found = False

		# loop through the entire list 
		while found is False:
			if current.get_id() == id:
				found = True
            
			else:
				current = current.get_next()

			# raise error if data is not found in the list 
			if current is None:
				raise ValueError("Data not found.")

		# return the name and contact number
		return current.get_name(), current.get_number()

	# function to delete nodes from the Linked List
	def delete(self, id):

		# initialize current to head
		current = self.head

		# search for the node to be deleted 
		previous = None
		found = False
		while found is False:
			if current.get_id() == id:
				found = True
            
			# keep track of the nodes
			else:
				previous = current
				current = current.get_next()

		# raise error if data is not found in the list
		if current is None:
			raise ValueError("Data not found.")

		if previous is None:
			self.head = current.get_next()
        
		# set next to be the node following the node being deleted,
		# jumping over and disconnecting the node being deleted 
		else:
			previous.set_next(current.get_next())

class PriorityQueueNode:
    def __init__(self, pr, value, next = None):
        self.data = value
        self.priority = pr
        self.next = next

class PriorityQueue:
	# constructor for PriorityQueue class
	def __init__(self):
		self.head = None
		
	# function to check if Priority Queue is Empty or not
	def isEmpty(self):
		return True if self.head == None else False
	
	# function to insert a node based on their rating
	def push(self, priority, value):
		
		# check if Priority Queue is empty or not
		if self.isEmpty() == True:
			
			# initialize a new node with given data and assigning it to class variable
			self.head = PriorityQueueNode(priority, value)
			
		else:

			# compare the ratings of the nodes
			if self.head.priority < priority:
				
				# initialize a new node with given data
				newNode = PriorityQueueNode(priority, value)
				
				# set next of new node as head
				newNode.next = self.head
				
				# let head point to the new node
				self.head = newNode
				
			else:
				
				# traverse through Priority Queue until it
				# finds the next smaller rating
				temp = self.head
				
				while temp.next:
					
					# break loop if a smaller rating is found
					if priority >= temp.next.priority:
						break
					
					temp = temp.next

				# initialize a new node with given data
				newNode = PriorityQueueNode(priority, value)

				# set next of new node as temp.next
				newNode.next = temp.next

				# let temp.next point to the new node
				temp.next = newNode

	# function to remove highest rating node from the Priority Queue
	def pop(self):
		
		# check if Priority Queue is empty or not
		if self.isEmpty() == True:
			return
		
		else:
			
			# remove highest rating node from Priority Queue,
			# and update head to next node
			self.head = self.head.next
			
	# function to return rating of patient but not removing it
	def peek_priority(self):
		
		# check if Priority Queue is empty or not
		if self.isEmpty() == True:
			return
		else:
			return self.head.priority
	
	# function to return patient ID but not removing it
	def peek_data(self):
		
		# check if Priority Queue is empty or not
		if self.isEmpty() == True:
			return
		else:
			return self.head.data

# main function
def main():

	# read data from priority.txt
	with open('priority.txt', 'r') as f:
		testing = [x.rstrip('\n').split(',') for x in f.readlines()]

	# read data from patient_info.txt
	with open('patient_info.txt', 'r') as f:
		testing1 = [x.rstrip('\n').split(',') for x in f.readlines()]

	# initialize LinkedList  
	linkedlist = LinkedList()

	# store data into Linked List
	for x in testing1[1:]:
		linkedlist.insert(int(x[0]), x[1], x[2])
	
	# initialize PriorityQueue  
	pq = PriorityQueue()

	# store data into Priority Queue
	for x in testing[1:]:
		pq.push(int(x[0]), int(x[1]))
	
	# loop through Priority Queue until it's empty
	while not pq.isEmpty():

		# take each patient ID from Priority Queue and search in Linked List
		searchList = linkedlist.search(pq.peek_data())

		# print out the patient's information
		print(f'Patient ID: {pq.peek_data()}	Priority: {pq.peek_priority()}')
		print(f'Full Name: {searchList[0]}')
		print(f'Contact Number: {searchList[1]}\n')
		print('-------------------------------------------\n')

		# remove the printed node from the Linked List
		linkedlist.delete(pq.peek_data())

		# remove the printed node from the Priority Queue
		pq.pop()

		
# Driver code
if __name__ == "__main__":
	main()
