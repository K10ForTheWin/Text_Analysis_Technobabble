import os
from collections import defaultdict

##Change paths to relative paths

mychardict=defaultdict(list)

def process_file(fi):

  newlines = []
  with open(fi, encoding='utf-8') as infile:
    lines = infile.readlines()
    previous_char = ''
    previous_lines = ''
    seen_previous_line = False
    for line in lines:
      if ":" in line:
        character, punct, current_line = line.partition(":")
        previous_char = character
        previous_lines = current_line
        seen_previous_line = True
        newlines.append((character, current_line))
      else:
        current_line = line.strip()
        character = previous_char
        previous_lines += current_line

        newlines.append((previous_char, current_line))

  return newlines


def create_char_dict(newlines):
  mydict = defaultdict(list)
  for i in range(0, len(newlines)-1):
   # print(newlines[i])
    ch, line = newlines[i]
   # print(ch, line)
    if "[OC]" in ch:
      ch=ch.strip(" [OC]")
    elif "[OC}" in ch:
      ch=ch.strip(" [OC}")
    elif "[OC" in ch:
      ch=ch.strip(" [OC")
    elif "[on monitor]" in ch:
      ch=ch.strip(" [on monitor]")
    elif "[on viewscreen]" in ch:
      ch=ch.strip(" [on viewscreen]")
    elif "[on viewscreen" in ch:
      ch=ch.strip(" [on viewscreen")
    elif "[on screen]" in ch:
      ch=ch.strip(" [on screen]")
##    elif "2" in ch:
##      ch=ch.strip(" 2")
##    elif ch.startswith("BRIEN"):
##      ch="O'BRIEN"
##    

      
    mydict[ch.strip()].append(line)
    ch=ch.strip()
    mychardict[ch].append(line)

  return mydict


    
def dir_dir(dirname):
  if os.path.isdir(dirname):
    pass
  else:
    os.mkdir(dirname)


def check_keys(k):

  if k=='':
    return False
  if 'QUARK/KIRA' in k:
    return False
  if 'STETH/PARIS' in k:
    return False
  if 'PARIS/STETH' in k:
    return False
  if 'STETH/JANEWAY' in k:
    return False
  if 'BOMB/EMH' in k:
    return False
  if 'KIM|' in k:
    return False
  if'\\' in k:
    return False
  if '/' in k:
    return False
  if '?' in k:
    return False
  if not k.isupper():
    return False

  return True


def create_dest(folder):
  _, series = folder.split("_")
  dirname = os.path.join(".\data_char_lines", series)
  dir_dir(dirname)
  return dirname


def write_lines(mydict,dest_folder):
  for k, v in mydict.items():
    if check_keys(k):
      fo = os.path.join(dest_folder, k+".txt")
      with open(fo, 'a', encoding='utf-8') as outfile:
      
          vv=" ".join(i.strip() for i in v)
          outfile.write(vv)
          outfile.write("\n")


root = ".\data"
folders = os.listdir(root)

root_dest = ".\data_char_lines"
dir_dir(root_dest)

##ONLY RUN THIS METHOD ONCE UNLESS YOU WIPE CONTENTS OF DEST FOLDER FIRST
##WILL RESULT IN DUPLICATE LINES BEING ADDED FOR EACH RUN

def process_all_scripts(): 
  for folder in folders:

    files = os.listdir(os.path.join(root, folder))


    for f in files:
#give me the file locations
      file_loc = os.path.join(root, folder, f)
      flines=process_file(file_loc)  
#create directory of character names, and normalize to reduce set
      mydict=create_char_dict(flines)


#create destination folders/files to save text
      dest_folder = create_dest(folder)

     

#write character lines to files
      write_lines(mydict,dest_folder)
   


process_all_scripts()


print(len(mychardict))

def fix_enterprise():
  ent = ".\data\scripts_Enterprise"
  files = os.listdir(ent)
  for file in files:
    print(file)
    if file.isdir():
      pass
    else:
      file_loc = os.path.join(ent, file)
      print(file_loc)
      
      flines=process_file(file_loc)
      ch_line_dict = create_char_dict(flines)
      dest_folder=".\data_char_lines\Enterprise"
      write_lines(ch_line_dict, dest_folder)

#fix_enterprise()
