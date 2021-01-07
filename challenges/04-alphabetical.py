# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def sorting():
    string = input('Enter a word to aplhabetize.. ')
    print(string)
    print(''.join(sorted(string)))
sorting()