#GenerateCharacterStopwords.py
import os
#Pull file names from character + dialogue file lists to create list
# of character names to add to stopwords
#Include option to add "s" to name to filter "'s" occurences
root="C:\Python3\data_char_lines"
folders = os.listdir(root)
charslist = []
for f in folders:
  chars= [file.strip(".txt").lower() for file in os.listdir(os.path.join(root,f))]
##  print(chars)
  charslist.extend(chars)
  
with open("C:\Python3\data\char_stopwords.txt", 'w') as fo:
  for ch in chars:
    fo.write(ch)
    fo.write("\n")

