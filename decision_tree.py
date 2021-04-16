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

from numpy import *

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

		# Check for all positive or negative examples
		allPosOrNeg = 0
		for ex in examples:
			if ex[1] is True and \
					allPosOrNeg is 1 or allPosOrNeg is 0:
				allPosOrNeg = 1
			else if ex[1] is False and \
					allPosOrNeg is -1 or allPosOrNeg is 0:
				allPosOrNeg = -1
			else:
				allPosOrNeg = 2

		# Return root with value True or False if all examples
		# are positive or negative respectively
		if (allPosOrNeg == 1):
			root = Node("Yes")
			return root
		else if (allPosOrNeg == -1):
			root = Node("No")
			return root
		
		# Check size of attributes for an empty array and return
		# most common target attr value (if equal, returns "Yes")
		totPos = 0
		totNeg = 0
		if attrs.size == 0:
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
		index = -1
		highestVal = 0.0
		for i in range(len(attrs)):
			val = information_gain(examples, i)
			if val > highestVal:
				highestVal = val
				index = i

		# Label the current node with the attribute that best classifies
		# examples
		root = Node(attrs[index])

		# Determine all v_i for the successors
		v_i = []
		for ex in examples:
			if v_i.size == 0:
				v_i.insert(ex[index])
			else:
				if ex[index] in v_i:
					continue
				else:
					v_i.insert(ex[index])

		# For each value in v_i create successor nodes
		for i in v_i:
			subset = []
			for ex in examples:
				if i == ex[index]:
					subset.insert(ex)
			# If the subset is empty, the successor will be Yes or No based on
			# the total positive and negatives in examples as well as the leaf
			if subset.size == 0:
				if totPos >= totNeg:
					newNode = Node("Yes")
					root.add_successor(newNode, i)
				else:
					newNode = Node("No")
					root.add_successor(newNode, i)
			# Copy the arrays and remove this attribute from the arrays
			# to prevent subsequent duplicates in recursive ID3 calls
			else:
				attrCopy = attrs.view()
				del attrCopy[index]
				newNode = iterative_dichotomiser_3(subset, target_attr, attrs)
				root.add_successor(newNode, i)

		return root

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

		pass

	def save(self, path):
		"""
		Save this decision tree to a file.

		Arguments:
			path : str : the .txt file to save this decision tree to
		"""

		pass