#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(ourDir):
  absPaths = []
  files = os.listdir(ourDir)
  for filename in files:
    absPaths.append(os.path.abspath(os.path.join(ourDir,filename)))
  return absPaths

def copy_to(paths,ourDir):
  for filename in paths:
    shutil.copy(filename, ourDir)

def zip_to(paths, zippath):
  cmd = 'zip -j ' + zippath
  for filename in paths:
    cmd = cmd + " " + filename
  print "Command I'm going to do:", cmd
  status, output = commands.getstatusoutput(cmd)
  if status: 
    print "Error:", output
    sys.exit(1)
  else:
    print output 

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  tozip = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
  elif args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]
  else:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(2)

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  ourFilesList = []
  
  for ourDir in args:
    ourFilesList.extend(get_special_paths(ourDir))
  
  if todir:
    copy_to(ourFilesList, todir)
  elif tozip:
    print "Zippping to file"
    zip_to(ourFilesList, tozip)
  else:
    print "buuuuuuuuuu"
  
if __name__ == "__main__":
  main()
