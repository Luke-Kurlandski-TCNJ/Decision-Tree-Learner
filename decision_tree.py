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
		if attrs.size == 0:
			totPos = 0
			totNeg = 0
			for ex in examples:
				if ex[2] is True:
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

			# TODO: Talk about this question:
			# 		Instead of passing in attribute string, pass index?

			val = information_gain(examples, attrs[i])
			if val > highestVal:
				highestVal = val
				index = i

		# Label the current node with the attribute that best classifies
		# examples
		root = Node(attrs[i])

		# TODO: Work out the remainder of the algorithm
		#
		#	 	// The decision attr for Root is A.
		# 		For each possible value v_i of A {
		# 			Add a new tree branch below Root, corresponding to the test A=v_i;
		# 			Let Examples_{v_i} be the subset of Examples that have value v_i for A;
		# 			If (Examples_{v_i} is empty {
		# 				Below the new branch add a leaf node with label = most common value of Target_Attr in Examples;
		# 			} else {
		# 				Below the new branch add the subtree ID3(Examples_{v_i}, Target_Attr, Attributes - {A});
		# 			}
		# 		}
		#
		# TODO: Work out the remainder of the algorithm

		return root

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

		pass

	def save(self, path):
		"""
		Save this decision tree to a file.

		Arguments:
			path : str : the .txt file to save this decision tree to
		"""

		pass