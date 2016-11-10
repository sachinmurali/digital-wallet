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
		""" Retrieve the user_id1 and Check
		if the user_id2 is in user_id1's connections.
		If true, return it as a trusted transaction """ 
		try:
			node1 = self.nodes[user_id1]
			if user_id2 in node1.connections:
				return "trusted"
			else:
				return "unverified"	
		except:
			return "unverified"
