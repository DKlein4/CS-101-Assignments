'''
CS 101
Klein.Dustin-Program5
Assignment 5
Dustin Klein
dbktgb@mail.umkc.edu
Problem: Find the word commonality and relative frequency of mystery texts compared to speeches
Algorithm:
•	Open all files
•	These steps will be done for each of the documents to clean them up
o	Convert to lower case
o	Remove punctuation
o	Remove stop words
•	Break into lists of strings
•	Create a dictionary for each text
o	The key is each individual word and the value is the number of times it appears
•	Calculate word commonality
o	(Distinct words in first document) + (Distinct words in second document) – (Words in common) = (Distinct words in both)
o	Word Commonality = (Words in common) / (Distinct words in both)
o	Compare each document to each other and find the highest commonality
•	Calculate relative frequency
o	Find words in common between the texts
o	For each word:
	Find the difference between each document’s relative frequency
	Square that difference
	Add that to a running total of all the squares
o	Divide the sum by number of words in common between the texts
o	Return the square root of that sum
o	Compare each document to each other and find the lowest score
•	Print each mystery document’s best commonality and relative frequency
•	Close files
'''

import string
import math

def openFile(file_name):
    #opens the files
    try:
        file = open(file_name, "r")
        return file
    except FileNotFoundError:
        print(file_name, "could not be opened")

def cleanFile(file, stop_words):
    #returns a dictionary with each unique word as the key and the number of times its appeared as the value

    file_str = file.read()

    #remove puncuation and convert to lower case
    no_punc = "".join(x.lower() for x in file_str if x not in string.punctuation)

    #Break into a list of strings
    word_list = no_punc.split()

    #Remove stop words
    clean_list = [x for x in word_list if x not in stop_words]

    #Create a dictionary with the keys being unique words
    unique_words = dict()
    for word in clean_list:
        if word in unique_words:
            unique_words[word] += 1
        else:
            unique_words[word] = 1

    return unique_words

def calcCommonality(dict1, dict2):
    #calulates the commonality between two speeches

    distinct_in_first = len(dict1)
    distinct_in_second = len(dict2)
    words_in_common = 0
    for key in dict1:
        if key in dict2:
            words_in_common += 1

    distinct_in_both = distinct_in_first + distinct_in_second - words_in_common

    commonality = words_in_common / distinct_in_both

    return commonality

def bestCommonality(mystery, mystery_name, speeches):
    #finds the best commonality between a mystery speech and the known speeches

    best_commonality = 0
    for i in range(4):
        com = calcCommonality(mystery, speeches[i])
        if com > best_commonality:
            best_commonality = com
            if i == 0:
                best_commonality_name = "Trump"
            elif i == 1:
                best_commonality_name = "Clinton"
            elif i == 2:
                best_commonality_name = "Obama"
            else:
                best_commonality_name = "Romney"

    print("The text", mystery_name, "has the highest word commonality with", best_commonality_name, "({:.4%})".format(best_commonality))

def calcFrequency(dict1, dict2):
    #calculates the frequency between two speeches

    words_in_common = 0
    for key in dict1:
        if key in dict2:
            words_in_common += 1

    dict1_length = 0
    for key in dict1:
        dict1_length += dict1[key]
    dict1_freq = dict()
    for key in dict1:
        dict1_freq[key] = dict1[key] / dict1_length

    dict2_length = 0
    for key in dict2:
        dict2_length += dict2[key]
    dict2_freq = dict()
    for key in dict2:
        dict2_freq[key] = dict2[key] / dict2_length

    sum_of_squares = 0
    for key in dict1:
        if key in dict2:
            difference = dict1_freq[key] - dict2_freq[key]
            sum_of_squares += difference**2

    return math.sqrt(sum_of_squares / words_in_common)

def bestFrequency(mystery, mystery_name, speeches):
    #finds the best frequency of an unkown speech compared to the known speeches

    best_frequency = 999999
    for i in range(4):
        freq = calcFrequency(mystery, speeches[i])
        if freq < best_frequency:
            best_frequency = freq
            if i == 0:
                best_frequency_name = "Trump"
            elif i == 1:
                best_frequency_name = "Clinton"
            elif i == 2:
                best_frequency_name = "Obama"
            else:
                best_frequency_name = "Romney"

    print("The text", mystery_name, "has the highest word frequency with", best_frequency_name, "({:.4})\n".format(best_frequency))

#open and get dictionaries of all the necessary files
stop_words = openFile("stopWords.txt")
stop_words_list = stop_words.read().split()

trump = openFile("trump.txt")
trump_dict = cleanFile(trump, stop_words_list)

clinton = openFile("clinton.txt")
clinton_dict = cleanFile(clinton, stop_words_list)

obama = openFile("obama.txt")
obama_dict = cleanFile(obama, stop_words_list)

romney = openFile("romney.txt")
romney_dict = cleanFile(romney, stop_words_list)

mys1 = openFile("mystery1.txt")
mys1_dict = cleanFile(mys1, stop_words_list)

mys2 = openFile("mystery2.txt")
mys2_dict = cleanFile(mys2, stop_words_list)

mys3 = openFile("mystery3.txt")
mys3_dict = cleanFile(mys3, stop_words_list)

mys4 = openFile("mystery4.txt")
mys4_dict = cleanFile(mys4, stop_words_list)

#put all the speech dictionaries in a list to be used later
known_speeches = [trump_dict, clinton_dict, obama_dict, romney_dict]

#call the functions to find the best commonaluty and frequency for each unkown text
bestCommonality(mys1_dict, "mystery1", known_speeches)
bestFrequency(mys1_dict, "mystery1", known_speeches)

bestCommonality(mys2_dict, "mystery2", known_speeches)
bestFrequency(mys2_dict, "mystery2", known_speeches)

bestCommonality(mys3_dict, "mystery3", known_speeches)
bestFrequency(mys3_dict, "mystery3", known_speeches)

bestCommonality(mys4_dict, "mystery4", known_speeches)
bestFrequency(mys4_dict, "mystery4", known_speeches)

