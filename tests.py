"""
Test all aspects of the application.

Run from command line using 
	> python tests.py
"""

import unittest

from decision_tree import Node, DecisionTree
from main import main

class NodeTest(unittest.TestCase):

	def test___init__(self):

		n = Node("node")
		assert n.label == "node"
		assert n.successors == []

	def test_add_successor(self):

		n1 = Node("n1")
		n2 = Node("n2")
		n3 = Node("n3")
		n4 = Node("n4")

		n1.add_successor(n2, "edge 1 to 2")
		n1.add_successor(n3, "edge 1 to 3")
		n3.add_successor(n4, "edge 3 to 4")

		for n_e, l in zip(n1.successors, ["edge 1 to 2", "edge 1 to 3"]):
			assert n_e[1] == l

		for n_e, l in zip(n3.successors, ["edge 3 to 4"]):
			assert n_e[1] == l

	def test___str__(self):

		n1 = Node("n1")
		n2 = Node("n2")
		n3 = Node("n3")
		n4 = Node("n4")
		n5 = Node("n5")
		n6 = Node("n6")
		n7 = Node("n7")
		n8 = Node("n8")
		
		print(str(n1), '\n\n')

		n1.add_successor(n2, "edge 1 to 2")
		print(str(n1), '\n\n')

		n1.add_successor(n3, "edge 1 to 3")
		print(str(n1), '\n\n')

		n3.add_successor(n4, "edge 3 to 4")
		print(str(n1), '\n\n')

		n3.add_successor(n5, "edge 3 to 5")
		print(str(n1), '\n\n')

		n4.add_successor(n6, "edge 4 to 6")
		print(str(n1), '\n\n')
		
		n4.add_successor(n7, "edge 4 to 7")
		print(str(n1), '\n\n')

class DecisionTreeTest(unittest.TestCase):

	def test___init__(self):
		pass

	def test_iterative_dichotomiser_3(self):
		pass

	def test_information_gain(self):
		pass

	def test_entropy(self):
		pass

	def test___str__(self):

		examples = None
		target_attr = None
		attrs = None
		dt = DecisionTree(examples, target_attr, attrs)

		assert isinstance(str, str(dt))

	def test_save(self):
		
		examples = None
		target_attr = None
		attrs = None
		dt = DecisionTree(examples, target_attr, attrs)
		
		dt.save("test_path.txt")

class mainTest(unittest.TestCase):

	def test_main(self):
		main()

if __name__ == '__main__':
	unittest.main()