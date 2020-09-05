# Get files of a certain size threshold, top 100
#preview file lexicon
import string
from shutil import copyfile
import os
import operator
from nltk.corpus import stopwords

      
def dir_dir(dirname):
  if os.path.isdir(dirname):
    pass
  else:
    os.mkdir(dirname)
    
##root = "C:\Python3\data_char_lines"
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "data_char_lines")


series=os.listdir(".\data_char_lines")
root_keep = ".\data_char_lines_top_100"
dir_dir(root_keep)

mydict = {}
keep_files=[]
for c in series:
  file_sizes = []
  r = os.path.join(".\data_char_lines", c)
  for file in os.listdir(r):
    f = os.path.join(r, file)

    with open(f,encoding='utf-8') as infile:
        lex = []
        lines = infile.readlines()
        for line in lines:
            print(line)
    
 
def filter_words(wordlist):
  filteredwords = []
  for w in wordlist:
    w = w.lower()
    if w[-1:] in string.punctuation:
      w = w[:-1]
    elif w[0] in string.punctuation:
      w = w[1:]
    filteredwords.append(w)
  return filteredwords
    
# 10 GB
##>>> os.stat("C:\Python3\data_char_lines\Voyager\GEGEN.txt")
##os.stat_result(st_mode=33206, st_ino=281474977348190, st_dev=606102944, st_nlink=1, st_uid=0, st_gid=0, st_size=9228, st_atime=1542864677, st_mtime=1542864677, st_ctime=1542864677)
##>>> x=_
##>>> x.st_size
##9228

##    print(f)
##    sz = file_size(f)
##    if not sz.endswith("bytes"):
##      print(file, sz)
