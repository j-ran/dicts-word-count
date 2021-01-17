# put your code here.
"""
Defines a function to input .txt file and outputs word counts in file.
"""

# define function, with file
def count_words(filename):
    """Open a file and count how many times each space-separated word occurs in the file. 
    Print the counts to the screen. """

    # create empty list to keep each word in the text file 
    all_words = []
    # create empty dictionary to keep each word:instance pair
    word_count = {}

    # open .txt file
    txt_file = open(filename)

     # for each line in the text file
     # strip out returns 
     # split the line into words at the spaces
     # and save it into a list called "split_line"
    for line in txt_file:
        split_line = line.rstrip().split(' ')
        # - test - print(f"Split line is many lists. One of them is: {split_line}")
        for word in split_line:
            all_words.append(word)
    # - test - print(f"Now we have one list of lots of words: {all_words}") 

    for word in all_words:
        # use '.get' to retrieve instances of the word; 
        # default is zero, then increment one with each instance encountered 
        word_count[word] = word_count.get(word, 0) + 1
    # print(f"This is 'word_count': {word_count}")
    return word_count 

# Right now, the dictionary is printed via line 34 of the previous block.
# The following block is another attempt to print the dictionary.
# It's not quite right at present, so it is commented out.

# in-progress : 
"""
def print_dict(word_count):
    count_words(filename)
    word_count = word_count
    for word, count in word_count.item():
        print(word, count)
"""
# Print the result when the function is called
print(count_words('test.txt'))