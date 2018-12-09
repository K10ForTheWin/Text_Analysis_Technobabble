import os
from collections import defaultdict


def process_file(fi):
##  fname = os.path.join(root, name)

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

  
def clean_values(mydict2):
  md = {}

  for k, v in mydict2.items():
    if '/' in k:
      pass
    elif "?" in k:
      pass
    else:
      v=v[0]
      vv=[line.strip() for line in v]

      vv=' '.join(vv)
      md[k] = vv
  
  return md
  ##    print(vv)


def remove_dups(dict1):
  dup_keys = {}
  undup_keys = []
  newdict = defaultdict(list)

  for k in dict1.keys():

    if len(k.split("["))==2:
      kk, k0 = k.split("[")
      k0 = k0.strip()
    elif ")" in k:
          #"Elsewhere -)SARIN": 'SARIN
      try:
        k0, kk = k.split(")")
      except ValueError:
        print(kk) #2 errors
    else:
      kk = k.strip()

    dup_keys[k] = kk.strip()
    undup_keys.append(kk)
##    print(dup_keys)
##    print(undup_keys)
    
  for k, v in dict1.items():
    if k not in undup_keys:
      try:
        newdict[dup_keys[k]].append(v)
      except KeyError:
        pass
    else:
      newdict[k].append(v)
  return newdict


def create_char_dict(newlines):

  mydict = defaultdict(list)
  for i in range(0, len(newlines)-1):
    ch, line = newlines[i]
    mydict[ch].append(line)

  mydict2 = remove_dups(mydict)
  mydict2 = clean_values(mydict2)
  return mydict2

def create_episode_folder(name):
  if os.path.isdir(name):
    pass
  else:
    os.mkdir(name)
    
def dir_dir(dirname):
  if os.path.isdir(dirname):
    pass
  else:
    os.mkdir(dirname)

def get_fo(root, k):
  series = root.split("/")[-1]
  fo = os.path.join("C:\Python3\data_char_lines\\", series, k+".txt")

def check_keys(k):
  if k=='':
    return False
  elif k=='Original Airdate':
    return False
  elif k=='Stardate':
    return False
  #check if multiple words/character mentions
  elif k.startswith(" "):
    return False #idk
  elif len(k.split(" "))>3:
    print(k)
    return False
  else:
    return True

def create_dest(folder):
  _, series = folder.split("_")
  dirname = os.path.join("C:\Python3\data_char_lines", series)
  dir_dir(dirname)
  return dirname


def write_lines(char_line_dict, dest_folder):
  for k, v in char_line_dict.items():
    if check_keys(k):
      fo = os.path.join(dest_folder, k+".txt")
      with open(fo, 'a', encoding='utf-8') as outfile:
        print(fo)
        outfile.write(v)
        outfile.write("\n")


def fix_enterprise():
  ent = "C:\Python3\data\scripts_Enterprise"
  files = os.listdir(ent)
  for file in files:
    file_loc = os.path.join(ent, file)
  ##    print(file_loc)
    flines=process_file(file_loc)
    ch_line_dict = create_char_dict(flines)
    dest_folder="C:\Python3\data_char_lines\Enterprise"
    write_lines(ch_line_dict, dest_folder)


root = "C:\Python3\data"
contents = os.listdir(root)
folders = [f for f in contents if os.path.isdir(f)]
root_dest = "C:\Python3\data_char_lines"
dir_dir(root_dest)

def process_all_scripts(): 
  for folder in folders:
    files = os.listdir(os.path.join(root, folder))
    for f in files: 
      file_loc = os.path.join(folder, f)
  ##    print(file_loc)
      flines=process_file(file_loc)
      ch_line_dict = create_char_dict(flines)
  ##    print(sorted(ch_line_dict.keys()))
      dest_folder = create_dest(folder)
      write_lines(ch_line_dict, dest_folder)

##process_all_scripts()
##os.remove_dir("C:\Python3\data\scripts_Enterprise")
##os.mkdir("C:\Python3\data\scripts_Enterprise")
##fix_enterprise()



##  for m in more:
##  for mm in m:
##    statinfo = os.stat(mm)
##    size = statinfo.st_size
##    sz = file_size(mm)
##    print(file, sz)

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)
      
root = "C:\Python3\data_char_lines"
contents = os.listdir(root)
##print(contents)
more = [os.listdir(os.path.join(root,c)) for c in contents]

mydict = {}
keep_files=[]
for c in contents:
  file_sizes = []
  r = os.path.join(root, c)
  for file in os.listdir(r):
    f = os.path.join(r, file)
    statinfo = os.stat(f)
    size = statinfo.st_size
    if size > 9228:
      keep_files.append(file)
    file_sizes.append(size)
##    print(f)
##    sz = file_size(f)
##    if not sz.endswith("bytes"):
##      print(file, sz)
  mydict[c] = file_sizes
  print(c, len(file_sizes), min(file_sizes), max(file_sizes), sum(file_sizes)/len(file_sizes))
      
print(len(keep_files))


# 10 GB
##>>> os.stat("C:\Python3\data_char_lines\Voyager\GEGEN.txt")
##os.stat_result(st_mode=33206, st_ino=281474977348190, st_dev=606102944, st_nlink=1, st_uid=0, st_gid=0, st_size=9228, st_atime=1542864677, st_mtime=1542864677, st_ctime=1542864677)
##>>> x=_
##>>> x.st_size
##9228
