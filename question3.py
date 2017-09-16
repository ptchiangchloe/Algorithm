# Question 3
# Given an undirected graph G, find the minimum spanning tree within G. A minimum
# spanning tree connects all vertices in a graph with the smallest possible total
# weight of edges. Your function should take in and return an adjacency list
# structured like this:

# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)],
#  'C': [('B', 5)]}

# Vertices are represented as unique strings. The function definition should be question3(G)

class Weighted_graph:
	"""
	Implement a weighted graph with a 2rd list and corresponding weight list
	Vertices are represented by elements(eg. A, B, C) in the graph list and edges are represented
	by a list collection of each 2 vertices (eg. [A, B])
	"""

	edges = []
	weight = []
	vertices = []

	def __init__(self, edge_list, weight):
		self.edges.append(edge_list)
		self.weight.append(weight)

	def __sort(self):
		"""
		Sorts both edges and weight lists in nondecreasing order of weight list elements
		"""
		if len(self.edges) != len(self.weight):
			return;
		for i in range(1, len(self.weight)):
			temp_weight = self.weight[i]
			temp_edge = self.edges[i]
			current = i - 1
			while current >= 0 and temp_weight < self.weight[current]:
				self.weight[current+1] = self.weight[current]
				self.edges[current+1] = self.edges[current]
				current -= 1
				self.weight[current+1] = temp_weight
				self.edges[current+1] = temp_edge

	def __makeset(self):
		"""
		Initialize each vertex to its own component
		"""
		for i in range(len(self.edges)):
			# i has [[a,a],[b,b],[c,c]]
			for j in range(len(self.edges[i])):
				# j has [a, b]
				if self.edges[i][j] not in self.vertices:
					self.vertices.append(self.edges[i][j])

		# Use nested loop to find the unique elements

		for k in range(len(self.vertices)):
			self.vertices[k] = [self.vertices[k]]

		# make each vertex one single component, for later union purpose

	def __findset(self, vertex):
		"""
		Find and return the index to which vertice belongs in vertices list
		"""
		for i in range(len(self.vertices)):
			for element in self.vertices[i]:
				if element == vertex:
					return i
		return None

		# union function
	def __union(self, vertex1, vertex2):
		"""
		Joins 2 vertex together
		"""
		print vertex1
		print vertex2
		index1 = self.__findset(vertex1)
		index2 = self.__findset(vertex2)
		print index1
		print index2
		for element in self.vertices[index2]:
			self.vertices[index1].append(element)
		self.vertices.pop(index2)
		print self.vertices

	def __makeadjacencylist(self, adjacency_list, current_edge_from, current_edge_to, weight):
		if current_edge_from in adjacency_list:
			if current_edge_to not in adjacency_list[current_edge_from]:
				adjacency_list[current_edge_from].append((current_edge_to, weight))
		else:
			adjacency_list[current_edge_from] = [(current_edge_to, weight)]

	def add(self, edge_list, weight):
		"""
		Add an edge(defined by 2 vertices in a list) and ites corresponding weight to edges
		"""
		self.edges.append(edge_list)
		self.weight.append(weight)

	def question3(self):
			self.__sort()
			# sorting the edges list into a nondecreasing list
			self.__makeset()
			# make each vertice as a single component
			i = 0
			adjacency_list = {}
			while len(self.vertices) > 1:
				print 'this time the edge is {0}'.format(self.edges[i])
				if self.__findset(self.edges[i][0]) != self.__findset(self.edges[i][1]):
					# if the two vertices are in different subset in the vertices set, that means they
					# still can be unioned together.
					# if the two vertices are already in the same subset in the vertices set, that means
					# they have already been unioned together with the minimum spanning
					print "({0}, {0}) edge selected.".format(self.edges[i][0], self.edges[i][1])
					print "the edge weight is {0}".format(self.weight[i])
					weight = self.weight[i]
					current_edge_from = self.edges[i][0]
					print "current edge from is {0}".format(current_edge_from)
					current_edge_to = self.edges[i][1]
					self.__makeadjacencylist(adjacency_list, current_edge_from, current_edge_to, weight)

					current_edge_from = self.edges[i][1]
					print "current edge from is {0}".format(current_edge_from)
					current_edge_to = self.edges[i][0]
					self.__makeadjacencylist(adjacency_list, current_edge_from, current_edge_to, weight)

					print "current adjacency_list is {0}".format(adjacency_list)

					self.__union(self.edges[i][0], self.edges[i][1])

				i += 1
			return adjacency_list


	def print_graph(self):
		"""
		Print each set of edges in a graph and its corresponding edges
		"""
		print "{0} is the edges list".format(self.edges)
		print "{0} is the weight list".format(self.weight)
		print "{0} is the vertices list".format(self.vertices)

# Teat cases
# Each time test one test case.

# Test 1
test_graph = Weighted_graph(["A","D"], 0)
test_graph.add(["A","B"], 100)
test_graph.add(["A","C"], 6)
test_graph.add(["B","C"], 1)
test_graph.add(["B","D"], 1)
test_graph.add(["C","D"], 0)
test_graph.question3()
# {
# 'A': [('D', 0)],
# 'C': [('D', 0), ('B', 1)],
# 'B': [('C', 1)],
# 'D': [('A', 0), ('C', 0)]
# }

# Test 1
# test_graph = Weighted_graph([1,2], 4)
# test_graph.add([1,3], 2)
# test_graph.add([1,5], 3)
# test_graph.add([2,4], 5)
# test_graph.add([3,4], 1)
# test_graph.add([3,5], 6)
# test_graph.add([3,6], 3)
# test_graph.add([4,6], 6)
# test_graph.add([5,6], 2)
# test_graph.question3()
# {
# 	1: [(3, 2), (5, 3), (2, 4)],
# 	2: [(1, 4)],
# 	3: [(4, 1), (1, 2)],
# 	4: [(3, 1)],
# 	5: [(6, 2), (1, 3)],
# 	6: [(5, 2)]
# }

# Test 2
# test_graph = Weighted_graph(["A","D"], 1)
# test_graph.add(["A","B"], 3)
# test_graph.add(["B","D"], 8)
# test_graph.add(["B","C"], 1)
# test_graph.add(["C","D"], 1)
# test_graph.add(["C","E"], 5)
# test_graph.add(["C","F"], 4)
# test_graph.add(["D","E"], 6)
# test_graph.add(["E","F"], 2)
# test_graph.question3()
# {
# 'A': [('D', 1)],
# 'C': [('B', 1), ('D', 1), ('F', 4)],
# 'B': [('C', 1)],
# 'E': [('F', 2)],
# 'D': [('A', 1), ('C', 1)],
# 'F': [('E', 2), ('C', 4)]
# }
