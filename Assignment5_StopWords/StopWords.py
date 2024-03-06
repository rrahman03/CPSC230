import operator
import string


#takes in a file, read the contents, store in a string and return the string
def read_file (file):
    file_str=""
    for line in file:
         file_str += line[:-1] + " "

    return file_str
    
#writes the content of a dictionary into a file - with the key value pairs
#takes in a dictionay and a file name
def write_file(dictionary, filename):
    sorted_list = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    with open (filename, "w") as file:
        for word in sorted_list:
            file.write(f"{word}\n")

#takes in a string, and builds a dictionary with wordcount
def build_dictionary(file_str):
    words = file_str.lower().split()
    wordcountdict={}
    for word in words:
        word = removepunctuation(word)
        if word in wordcountdict:
            wordcountdict[word] +=1
        else:
            wordcountdict[word] = 1
    
    return wordcountdict

def removepunctuation(word):
    punct = string.punctuation
    #removing any leading punctuations
    while len(word) > 0 and word[0] in punct:
        word = word[1:]
    #remove any tralining punctuation
    while len(word) > 0 and word[-1] in punct:
        word = word[:-1]
    return word.strip()

file = open("BeeMovieScript.txt")
file_str=read_file(file)
dict = build_dictionary(file_str)
write_file(dict,"counts.txt")