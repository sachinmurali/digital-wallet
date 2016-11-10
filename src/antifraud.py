import csv
import os
import paymo, paymo2, paymo3
import sys

""" Feature one implementation """
def feature_one(id1, id2, graph_one, unique_one):		

	""" Create a set to store unique transactions """
	if (id1, id2) in unique_one or (id2, id1) in unique_one:
		pass
	else:
		unique_one.add((id1, id2))

		""" Create a graph to store each user and the user's connections """
		payer = graph_one.add_nodes(id1)
		payee = graph_one.add_nodes(id2)

		payer.add_connection(payee)
		payee.add_connection(payer)		

def feature_two(id1, id2, graph_two, unique_two):
	unique = set()
	""" Create a set to store unique transactions """
	if (id1, id2) in unique_two or (id2, id1) in unique_two:
		pass
	else:
		""" Create a graph to store each user and the user's connections """
		unique_two.add((id1, id2))
		payer = graph_two.add_nodes(id1)
		payee = graph_two.add_nodes(id2)

		payer.add_connection(payee)
		payee.add_connection(payer)

def feature_three(id1, id2, graph_three, unique_three):
		""" Create a set to store unique transactions """
		if (id1, id2) in unique_three or (id2, id1) in unique_three:
			pass
		else:
			""" Create a graph to store each user and the user's connections """
			unique_three.add((id1, id2))
			payer = graph_three.add_nodes(id1)
			payee = graph_three.add_nodes(id2)

			graph_three.create_connection(payer, payee)
	
""" Read in the stream_payment data and write the 
	output to the corresponding file """
def write_output_to_file(graph, filename, stream_file):
		with open(stream_file,"rb") as f:
			try:
				os.remove(filename)
			except OSError:
				pass
			file1 = open(filename,"a")
			lines = f.readlines()
			for line in lines[1:]:
				line = line.split(',')
				id1 = line[1].strip()
				id2 = line[2].strip()
				
				status = graph.is_trusted(id1, id2)
				file1.write(status + "\n")
		file1.close()


if __name__ == '__main__':


	batch_file = sys.argv[1]
	stream_file = sys.argv[2]
	first = sys.argv[3]
	second = sys.argv[4]
	third = sys.argv[5]

	graph_one, unique_one = paymo.Graph(), set()
	graph_two, unique_two = paymo2.Graph(), set()
	graph_three, unique_three = paymo3.Graph(), set()

	graphs = {graph_one:first, graph_two:second, graph_three:third}

	# Read the modified batch payment file
	with open(batch_file,"rb") as f:
		""" Ignore the header using next """
		lines = f.readlines()
		for line in lines[1:]:
			line = line.split(',')
			id1 = line[1].strip()
			id2 = line[2].strip()

			feature_one(id1, id2, graph_one, unique_one) 
			feature_two(id1, id2, graph_two, unique_two) 
			feature_three(id1, id2, graph_three, unique_three)

	for graph, filename in graphs.iteritems():
		write_output_to_file(graph, filename, stream_file)

	
