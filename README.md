# Decision-Tree-Learner
# CSC 426 Project 3
# Authors: Lana Abdelmohsen, Luke Kurlandski, Gordon Petry, Jason Swick
# Filename: README.md
# Description: Includes instructions on how to run the code and an explanation of the output format
This repository contains a basic descision tree learning algorithm.
## Output Format **TODO**
The format of the output is a sideways tree.

## High Level Description of code
1. main.py 
- primarily for executing the code
- also contains a function to process input files
2. decision_tree.py 
- contains the DecisionTree class, which contains the ID3 algorithm, information gain, and entropy functions
- contains the Node class, which serves as the backbone for the DecisionTree class
3. tests.py
- contains unit tests for information gain and entropy
- tests for converting Node into a string
4. PlayTennisOutputTrace.txt
- contains string representation of the decision tree as it is being built for the PlayTennis task
5. Task4.csv
- contains our own input data for PlayTennis task for task 4
6. other .txt, .csv
- other files such as the project description etc.


## Instructions for the HPC 
1. Comptibile with python 3.6.0. 

2. To use on TCNJ's hpc:
- > module add python/3.6.0

3. To run the program:
- > python3 main.py input_path output_path

4. where
- input_path : name of a .csv file (or .txt, if formatted correctly) that contains training data (last column should be value of target attribute)
- output_path : name of a .txt file where the decision tree will be written to as it is built
