import string
from shutil import copyfile
import os
import operator
from nltk.corpus import stopwords


stopwords_nltk = set(stopwords.words('english'))


root_keep = "C:\Python3\data_char_lines_top_100"
os.chdir(root_keep)
picard_words = {}
words = []
with open("PICARD.txt") as infile:
	w = infile.readlines()
	for line in w:
		lexs = line.split(" ")
		words.extend(lexs)


def filter_words(wordlist):
  filteredwords = []
  for w in wordlist:
    w = w.lower()
    if not w.isalpha():
      w = ''.join([char for char in w if char not in string.punctuation])
##    if w[-1:] in string.punctuation:
##      w = w[:-1]
##    elif w[0] in string.punctuation:
##      w = w[1:]
    filteredwords.append(w)
  return filteredwords

def remove_stopwords(words):
  filteredwords = []
  for w in words:
    if w not in stopwords_nltk:
      filteredwords.append(w)
  return filteredwords

words = filter_words(words)
words = remove_stopwords(words)

def count_words(words):
  d={}
  for w in set(words):
    d[w] = words.count(w)
  for k, v in d.items():
    if v>15:
      print(k, v)


count_words(words)
