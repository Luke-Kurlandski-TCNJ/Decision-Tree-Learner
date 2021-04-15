"""
A basic decision tree that uses the iterative dichotomiser 3 algorithm,
	and entropy.

Notes:
	The variable examples if frequently referenced throughout this file.
	Examples should be a set of the following form for some string attr
		{
			(
				[attr_1, attr_2, ...., attr_1], 
				bool
			)
		}
"""

class Node:
	"""
	Node component of a basic tree.

	Attributes:
		label : str : this node's label
		successors : [(Node, str)] : list of tuples of node, edge_label 
			pairs
	"""

	def __init__(self, label):
		"""
		Construct this node.

		Arguments:
			label : str : this node's label
		"""

		self.label = label
		self.successors = []

	def add_successor(self, node, edge_label):
		"""
		Add a child node to this node.

		Arguments:
			node : Node : the Node object that will become a successor
			edge_label : str : the label to apply to this edge
		"""

		self.successors.append((node, edge_label))

	def __str__(self, node=None, incomming_edge_label="", tree="", prefix="", last=True):
		"""
		Return string representation of this node and its successors.

		Arguments:
			node : Node : the node or leaf of the tree at this depth
				of recursion
			incomming_edge_label : str : the edge label that produced
				the node at this depth of recursion
			tree : str : recursively built string representation
			prefix : str : an increasingly long string of indentation
			last : bool : indicates if a node is the last successor of 
				its parent and thus should be printed slightly different

		Returns:
			tree : str : string representation of the tree
		"""
		
		if node is None:
			node = self
			tree = "".join(['[', node.label, ']\n'])
		else:
			tree += "".join([
				prefix, "|-{", incomming_edge_label, 
				"}-[", node.label, ']\n'
			])

		prefix += "       " if last else "|      "

		for i, child in enumerate(node.successors):
			tree = self.__str__(child[0], child[1], tree, 
									prefix, i == len(node.successors)-1)

		return tree

class DecisionTree:
	"""
	Decision tree learner.

	Attributes:
		root : Node : the root of the decision tree
	"""

	def __init__(self, examples, target_attr, attrs):
		"""
		Fit the training data to learn the decision tree.

		Arugments:
			examples : {([str,], bool)} : set of examples to learn from
			target_attr : str : attribute whose value is to be predicted
			attrs : [str,] : list of attributes that may be tested by
				the decision tree
		"""

		self.root = \
			self.iterative_dichotomiser_3(examples, target_attr, attrs)

	def iterative_dichotomiser_3(self, examples, target_attr, attrs):
		"""
		Learn the decision tree using the ID3 algorithm.

		Arugments:
			examples : {([str,], bool)} : set of examples to learn from
			target_attr : str : attribute whose value is to be predicted
			attrs : [str,] : list of attributes that may be tested by
				the decision tree

		Returns:
			root : Node : a subcomponent of the tree learned
		"""

		pass

	def information_gain(self, examples, attr):
		"""
		Compute the potentional information gain for a given attribute.

		Arguments:
			attr : str : the attribute to compute information gain for 
				relative to some set of training examples
			examples : {([str,], bool)} : set of examples to compute
				the information gain for

		Returns:
			gain : float : the information gain computed
		"""

		pass

	def entropy(self, examples):
		"""
		Compute the entropy of a set.

		Arguments:
			examples : {([str,], bool)} : set of examples to compute the
				entropy for
		"""

		pass

	def __str__(self):
		"""
		Represent this tree as a string.

		This is an overload of the base python str() type cast. To use:
			DT = DecisionTree()
			s = str(DT)
			print(s)

		Returns:
			s : str : the string representation of this decsision tree
		"""

		return str(self.root)

	def save(self, path):
		"""
		Save this decision tree to a file.

		Arguments:
			path : str : the .txt file to save this decision tree to
		"""

		with open(path, 'w') as f:
			f.write(str(self))