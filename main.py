# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    file = open(filename,"r+")
    return file.read()


def count_words():
    text = read_file_content("./story.txt")
    text = text.lower()
    words = text.split()
    # [assignment] Add your code here
    dict = {}
    for word in words:
        if dict.get(word) == None :
            dict[word] = int(1)
        else:
            dict[word] = dict.get(word) + 1
    return dict

print(read_file_content("./story.txt"))
print(count_words())