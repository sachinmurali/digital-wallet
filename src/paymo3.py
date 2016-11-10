class Node(object):

	def __init__(self, user_id):
		self.user_id = user_id
		self.connections = set()
		self.second_connections = set()

	""" Function to store the first degree connections """
	def add_connection(self, node):
		self.connections.add(node.user_id)

	""" Function to store the second degree connections """
	def add_second_connection(self, user_id):
		self.second_connections.add(user_id)

	""" Function to remove the connection
		from the second degree if the user 
		is involved in a direct transaction """
	def delete_second_connection(self, user_id):
		if user_id in self.second_connections:
			self.second_connections.remove(user_id)
		
class Graph(object):

	"""
	Data Structure to store all the nodes/users who have been involved in transactions
	"""
	def __init__(self):
		""" Stores user_id as the key and node as the value """
		self.nodes = dict() 

	""" Function to add the node to the dictionary """
	def add_nodes(self, user_id):
		try:
			node = self.nodes[user_id]
		except:
			node = Node(user_id)
			self.nodes[user_id] = node

		return self.nodes[user_id]

	""" Establishes a the first and second 
		degree connections between payer and payee """
	def create_connection(self, payer, payee):
		payer.add_connection(payee)
		payee.add_connection(payer)

		payer.delete_second_connection(payee.user_id)
		payee.delete_second_connection(payer.user_id)

		""" Create second degree connections between the payer's
			connections and the payee """ 
		for connection in payer.connections:
			self.nodes[connection].add_second_connection(payee.user_id)
			payee.add_second_connection(self.nodes[connection].user_id)

		""" Create second degree connections between the payee's
			connections and the payer """
		for connection in payee.connections:
			self.nodes[connection].add_second_connection(payer.user_id)
			payer.add_second_connection(self.nodes[connection].user_id)

	""" Function to determine whether the transaction is trusted
		or not: Checks upto four degrees"""
	def is_trusted(self, user_id1, user_id2):
		try:
			node1 = self.nodes[user_id1]
			node2 = self.nodes[user_id2]

			""" To check for the fourth degree connection,
				I perform an intersection operation between the
				payer's second degree connections and the payee's
				second degree connections. If the set has at least
				one element after the intersection operation, I 
				conclude the transaction is a trusted transaction.
				If the intersection returns an empty set, I return a 
				null """
			if user_id2 in node1.second_connections or user_id2 in node1.connections:			
				return "trusted"
			elif len(node1.second_connections.intersection(node2.second_connections)) > 0:
				return "trusted"
			else:
				return "unverified"
		except Exception as e:	
			return "unverified"
