"""
Run the program using this file

	> python3 main.py input_path output_path

	where 
		input_path : the .csv input path to learn a decision tree from
		output_path : the .txt output path to save the tree to
"""

import sys
import csv
from decision_tree import DecisionTree

def process_examples_files(path, target_attr):
	"""
	Takes a data file and processes into set of training examples.

	Arguments:
		path : str : the csv to process
		target_attr : str : the name of the column which is the target
			attribute in this csv file

	Returns:
		examples : [({attr_i : val_i} : bool)] : a set of tuples of 
			attribute-value dictionary and boolean valued target concept
			pairs
	"""

	examples = list()

	with open(path, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			r = dict(row)
			if "ExampleID" in r:
				r.pop("ExampleID")
			target_val = r.pop(target_attr)
			target_val = True if target_val.upper() == "YES" else False
			examples.append((r, target_val))

	return examples

def main():
	if len(sys.argv) < 3:
		print("Usage: main.py [INPUT FILE] [OUTPUT FILE]")
		sys.exit()
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	examples = process_examples_files(
			input_file, 
			'PlayTennis'
		)
	attrs = list(examples[0][0].keys())

	dt = DecisionTree()
	dt.fit(examples, attrs)
	print(str(dt))
	dt.save(output_file)
	pass

if __name__ == "__main__":
	main()

