#!/usr/bin/env python

import zlib
import sys
import hashlib
import os


SIMPLE_GIT_DIRECTORY = ".simple-git"
OBJECTS_DIRECTORY = "{}/objects".format(SIMPLE_GIT_DIRECTORY)
INDEX_PATH = "{}/index".format(SIMPLE_GIT_DIRECTORY)

if not os.path.isdir(SIMPLE_GIT_DIRECTORY):
	print("Not a Simple Git Repo!!!!!!")
	sys.exit()

path = sys.argv[1]

if not path:
	print("No path specifies!!!! please provide correct arguments!!!!")
	sys.exit()

f = open(path , "r")
contents = f.read()
sha1Hash = hashlib.sha1(contents)
sha = sha1Hash.hexdigest()
blob = zlib.compress(contents)

print(sha)

object_directory = "{0}/{1}".format(OBJECTS_DIRECTORY , sha[:2])
# perform mkdir -p functionality
blob_path = "{0}/{1}".format(object_directory , sha[2:])
os.makedirs(object_directory)

fl = open(blob_path , "w+")
fl.write(blob)

ind = open(INDEX_PATH , "a")
ind.write("{0} {1}".format(sha , path))









