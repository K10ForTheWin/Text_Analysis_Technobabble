
##
##  
##def clean_values(mydict2):
##  md = {}
##
##  for k, v in mydict2.items():
##    if '/' in k:
##      pass
##    elif "?" in k:
##      pass
##    else:
##      v=v[0]
##      vv=[line.strip() for line in v]
##
##      vv=' '.join(vv)
##      md[k] = vv
##  
##  return md
##  ##    print(vv)
##
##
##def remove_dups(dict1):
##  dup_keys = {}
##  undup_keys = []
##  newdict = defaultdict(list)
##
##  for k in dict1.keys():
##
##    if len(k.split("["))==2:
##      kk, k0 = k.split("[")
##      k0 = k0.strip()
##    elif ")" in k:
##          #"Elsewhere -)SARIN": 'SARIN
##      try:
##        k0, kk = k.split(")")
##      except ValueError:
##        print(kk) #2 errors
##    else:
##      kk = k.strip()
##
##    dup_keys[k] = kk.strip()
##    undup_keys.append(kk)
####    print(dup_keys)
####    print(undup_keys)
##    
##  for k, v in dict1.items():
##    if k not in undup_keys:
##      try:
##        newdict[dup_keys[k]].append(v)
##      except KeyError:
##        pass
##    else:
##      newdict[k].append(v)
##  return newdict



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
      
##root = ".\data_char_lines"
##contents = os.listdir(root)
####print(contents)
##more = [os.listdir(os.path.join(root,c)) for c in contents]
##
##mydict = {}
##keep_files=[]
##for c in contents:
##  file_sizes = []
##  r = os.path.join(root, c)
##  for file in os.listdir(r):
##    f = os.path.join(r, file)
##    statinfo = os.stat(f)
##    size = statinfo.st_size
##    if size > 9228:
##      keep_files.append(file)
##    file_sizes.append(size)
####    print(f)
####    sz = file_size(f)
####    if not sz.endswith("bytes"):
####      print(file, sz)
##  mydict[c] = file_sizes
##  print(c, len(file_sizes), min(file_sizes), max(file_sizes), sum(file_sizes)/len(file_sizes))
##      
##print(len(keep_files))


# 10 GB
##>>> os.stat("C:\Python3\data_char_lines\Voyager\GEGEN.txt")
##os.stat_result(st_mode=33206, st_ino=281474977348190, st_dev=606102944, st_nlink=1, st_uid=0, st_gid=0, st_size=9228, st_atime=1542864677, st_mtime=1542864677, st_ctime=1542864677)
##>>> x=_
##>>> x.st_size
##9228

