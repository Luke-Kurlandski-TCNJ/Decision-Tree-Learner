#Authors: Lana Abdelmohsen, Luke Kurlandski, Gordon Petry, Jason Swick

"""
A basic decision tree that uses the iterative dichotomiser 3 algorithm,
	and entropy.

Notes:
	The variable examples if frequently referenced throughout this file.

	Examples should be a list of the following form for some string attr
		[
			(
				{attr_1 : val_1, attr_2 : val_2},
				bool
			)
		]

	This does make it easier to do some things, but we have to change 
		from set to list because dictionaries are not hashable. 
"""


import math

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

	def __init__(self):
		"""
		Construct an empty decision tree.
		"""

		self.root = None

	def fit(self, examples, attrs):
		"""
		Fit the training data to learn the decision tree.

		Arugments:
			examples : [({attr : val}, bool)] : list of examples to 
				compute the information gain for
			target_attr : str : attribute whose value is to be predicted
			attrs : [str,] : list of attributes that may be tested by
				the decision tree
		"""

		self.root = self.iterative_dichotomiser_3(
			examples, 
			attrs
		)

	def iterative_dichotomiser_3(self, examples, attrs):
		"""
		Learn the decision tree using the ID3 algorithm.

		Arugments:
			examples : [({attr : val}, bool)] : list of examples to 
				compute the information gain for
			target_attr : str : attribute whose value is to be predicted
			attrs : [str,] : list of attributes that may be tested by
				the decision tree

		Returns:
			root : Node : a subcomponent of the tree learned
		"""

		# Check for all positive or negative examples
		allPosOrNeg = 0
		for ex in examples:
			if ex[1] and (allPosOrNeg == 1 or allPosOrNeg == 0):
				allPosOrNeg = 1
			elif not ex[1] and (allPosOrNeg == -1 or allPosOrNeg == 0):
				allPosOrNeg = -1
			else:
				allPosOrNeg = 2

		# Return root with value True or False if all examples
		# are positive or negative respectively
		if (allPosOrNeg == 1):
			root = Node("Yes")
			return root
		elif (allPosOrNeg == -1):
			root = Node("No")
			return root
		
		# Check size of attributes for an empty array and return
		# most common target attr value (if equal, returns "Yes")
		totPos = 0
		totNeg = 0
		if len(attrs) == 0:
			for ex in examples:
				if ex[1] is True:
					totPos += 1
				else:
					totNeg += 1
			if totPos >= totNeg:
				root = Node("Yes")
				return root
			else:
				root = Node("No")
				return root

		# Check every attribute for the attribute that "best" classifies
		# examples using information gain
		bestFitAttr = ""
		highestVal = -1
		for attr in attrs:
			val = self.information_gain(examples, attr)
			if val > highestVal:
				highestVal = val
				bestFitAttr = attr

		# Label the current node with the attribute that best classifies
		# examples
		root = Node(bestFitAttr)

		# Determine all v_i for the successors
		v_i = {e[0][bestFitAttr] for e in examples}

		# For each value in v_i create successor nodes
		for i in v_i:
			subset = []
			for ex in examples:
				if i == ex[0][bestFitAttr]:
					subset.append(ex)
			# If the subset is empty, the successor will be Yes or No based on
			# the total positive and negatives in examples as well as the leaf
			if len(subset) == 0:
				if totPos >= totNeg:
					newNode = Node("Yes")
					root.add_successor(newNode, i)
				else:
					newNode = Node("No")
					root.add_successor(newNode, i)
			# Copy the arrays and remove this attribute from the arrays
			# to prevent subsequent duplicates in recursive ID3 calls
			else:
				attrCopy = attrs.copy()
				attrCopy.remove(bestFitAttr)
				newNode = self.iterative_dichotomiser_3(subset, attrs)
				root.add_successor(newNode, i)

		return root

	def information_gain(self, examples, attr):
		"""
		Compute the potentional information gain for a given attribute.

		Arguments:
			attr : str : the attribute to compute information gain for 
				relative to some set of training examples
			examples : [({attr : val}, bool)] : list of examples to 
				compute the information gain for

		Returns:
			gain : float : the information gain computed
		"""

		gain = self.entropy(examples)

		possible_values_for_attr = {e[0][attr] for e in examples}

		for v in possible_values_for_attr:
			examples_v = [e for e in examples if e[0][attr] == v]
			gain -= len(examples_v) / len(examples) * self.entropy(examples_v)

		return gain

	def entropy(self, examples):
		"""
		Compute the entropy of a set.

		Arguments:
			examples : [({attr_i, val_i}, bool)] : set of examples to 
				compute the entropy for

		Returns:
			entropy : float : the entropy of the set
		"""

		entropy = 0

		possible_values_for_target_concept = {e[1] for e in examples}

		for v in possible_values_for_target_concept:
			examples_v = [e for e in examples if e[1] == v]
			p_v = len(examples_v) / len(examples)
			entropy -= p_v * math.log(p_v, 2)

		return entropy

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
