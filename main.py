#Authors: Lana Abdelmohsen, Luke Kurlandski, Gordon Petry, Jason Swick
"""
Run the program using this file

	> python3 main.py input_path output_path

	where 
		input_path : the .csv input path to learn a decision tree from
		output_path : the .txt output path to save the tree to
"""

from collections import OrderedDict
import csv
import sys

from decision_tree import DecisionTree

def process_examples_files(path):
	"""
	Takes a data file and processes into set of training examples.

	Notes:
		Assumes the target attribute lies in the final column

	Arguments:
		path : str : the csv to process

	Returns:
		examples : [({attr_i : val_i} : bool)] : a set of tuples of 
			attribute-value dictionary and boolean valued target concept
			pairs
	"""

	examples = list()

	with open(path, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			# Cast as ordered dictionary to preserve order of columns
			r = OrderedDict(row)
			# Remove the identification
			if "ExampleID" in r:
				r.pop("ExampleID")
			# Determine the value of target attr from column order
			target_val = r.popitem(last=True)
			target_val = True if target_val[1].upper() == "YES" else False
			# Cast back to a simple dict to avoid uneeded complexity
			examples.append((dict(r), target_val))

	return examples

def main():
	if len(sys.argv) < 3:
		print("Usage: main.py [INPUT FILE] [OUTPUT FILE]")
		sys.exit()
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	examples = process_examples_files(
			input_file
		)
	attrs = list(examples[0][0].keys())

	dt = DecisionTree()
	dt.fit(examples, attrs)
	print(str(dt))
	dt.save(output_file)
	pass

if __name__ == "__main__":
	main()

