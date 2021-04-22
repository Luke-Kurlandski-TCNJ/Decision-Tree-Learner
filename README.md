# Decision-Tree-Learner
# CSC 426 Project 3
# Authors: 
Lana Abdelmohsen, Luke Kurlandski, Gordon Petry, Jason Swick
# Description: 
A basic descision tree learning algorithm, capable of learning a tree from multiple data sources and producing a visual output.
# Content Guide and Description of Code
1. main.py 
- primarily for executing the code
- contains a function to process input files
  - reads the csv/txt file, learns the attributes from the first row, the target concept from the final column, ignores column named "ExampleID"
  - processes each successive row into a tuple, where the first element is a dict of attribute : value pairs and the second element is the boolean target concept
2. decision_tree.py 
- contains the DecisionTree class, which
   - contains ID3 algorithm
   - computes information gain
   - computes entropy of a set
   - converts itself to a string representation
   - prints itself to a file
- contains the Node class, which
   - is a simple, non-optimized n-tree with labeled edges
   - serves as the backbone for the DecisionTree class
   - can convert itself into a string representation
3. D2_output.txt
- contains string representation of the decision tree as it is being built for the PlayTennis task
4. D3_output.txt
- contains string representation of the decision tree as it is being built for the EnjoySport task
5. D3.pdf
- a repsonse to the version space question
6. D4_input.csv
- contains our own input data for PlayTennis task for task 4
7. D4_output.txt
- contains our own output data for PlayTennis task for task 4
8. D5.pdf
- group deliverable
9. other .txt, .csv
- other files such as the project description etc.
# Instructions for Use
1. Compatibile with python 3.6.0. 
2. TCNJ HPC specific instructions:
- > module add python/3.6.0
3. To run the program:
- > python3 main.py input_path output_path
4. where
- input_path : name of a .csv file that contains training data 
  - may also be .txt file type, but must contain comma separated values
  - last column should be value of target attribute
- output_path : name of a .txt file to write the learned decision tree
  - NOTE: the decision tree is printed sideways, not vertically!
# Output
A sideways-printed decision tree will be output the the output_path supplied when running the program.
