#!/usr/bin/env python
from collections import defaultdict
import hashlib
import sys
import os
import zlib

SIMPLE_GIT_DIRECTORY = ".simple-git"
OBJECTS_DIRECTORY = "{}/objects".format(SIMPLE_GIT_DIRECTORY)
INDEX_PATH = "{}/index".format(SIMPLE_GIT_DIRECTORY)


index_object = defaultdict(lambda: None)

def index_files_tree():
	#pass
	with open(INDEX_PATH) as f:
		for line in f:
			sha , path = line.split()
			#print(sha , path)
			#index_object = defaultdict(lambda: None)
			index_object = {}
			build_file_path(path , sha , index_object)
			print(index_object)

# Recursively build the index files object....
def build_file_path(paths , sha , index_object):
	paths_array = paths.split('/' , 1)
	if len(paths_array) > 1:
		branch = index_object.setdefault(paths_array[0], {})
		build_file_path(paths_array[1] , sha , branch)
	else:
		index_object[paths_array[0]] = sha




index_files_tree()

