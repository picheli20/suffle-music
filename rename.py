import os
import sys
import random

directory = "./test"
firstRun = False
arg_names = ['fileName', 'path', 'first']
args = dict(zip(arg_names, sys.argv))


for root, subFolders, files in os.walk(directory, topdown=True):
  for file in files:
    rand = str(random.randrange(0, 9999)).zfill(4);
    path = os.path.join(root, file)
    fileName = file
    if 'first' not in args:
      fileName = fileName[5:]

    fileName = rand + "_" + fileName;
    target = os.path.join(root, fileName)
    os.rename(path, target)
    pass
