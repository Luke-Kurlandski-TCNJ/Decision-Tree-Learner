# Decision-Tree-Learner

A basic descision tree learning algorithm.

Comptibile with python 3.6.0. 

To use on TCNJ's hpc:
	> module add python/3.6.0

To run the program:
	> python3 main.py input_path output_path

where
	input_path : name of a .csv file that contains training data (last column should be value of target attribute)
	output_path : name of a .txt file where the decision tree will be written to as it is built
