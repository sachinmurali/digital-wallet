class Node(object):

	def __init__(self, user_id):
		self.user_id = user_id
		self.connections = set()

	def add_connection(self, node):
		self.connections.add(node.user_id)
		
class Graph(object):

	"""
	Data Structure to store all the nodes/users who have been involved in transactions
	"""
	def __init__(self):
		self.nodes = dict()

	def add_nodes(self, user_id):
		""" Check if a node is already created for a user. If yes, return 
		the node. Else, create a new node, store the user_id as key and 
		node as the value """
		try:
			node = self.nodes[user_id]
		except:
			node = Node(user_id)
			self.nodes[user_id] = node

		return self.nodes[user_id]

	def is_trusted(self, user_id1, user_id2):
		""" To check for a second degree connection, I retrieve the user_id's 
		from the nodes data structure above. Then, I perform an intersection 
		operation on their respective first degree connections. If an empty set
		is returned, then I say that the connection is untrusted. Else,
		the connection is trusted """
		try:
			node1 = self.nodes[user_id1]
			node2 = self.nodes[user_id2]

			if user_id1 in node2.connections or user_id2 in node1.connections:
				return "trusted"
				
			if len(node1.connections.intersection(node2.connections)) == 0:
				return "unverified"
			else:
				return "trusted"	
		except:
			return "unverified"
