#!/usr/bin/env python
from collections import defaultdict
import hashlib
import sys
import os
import zlib
import datetime


SIMPLE_GIT_DIRECTORY = ".simple-git"
OBJECTS_DIRECTORY = "{}/objects".format(SIMPLE_GIT_DIRECTORY)
INDEX_PATH = "{}/index".format(SIMPLE_GIT_DIRECTORY)


#index_object = defaultdict(lambda: None)

def index_files_tree():
	#pass
	index_object = {}
	with open(INDEX_PATH) as f:
		for line in f:
			sha , path = line.split()
			build_file_path(path , sha , index_object)
	return index_object

# Recursively build the index files object....
def build_file_path(paths , sha , index_object):
	paths_array = paths.split('/' , 1)
	if len(paths_array) > 1:
		branch = index_object.setdefault(paths_array[0], {})
		build_file_path(paths_array[1] , sha , branch)
	else:
		index_object[paths_array[0]] = sha

# separate out the file creation module from the tree object creation method .........
def build_file_object(sha):
	object_directory = "{}/{}".format(OBJECTS_DIRECTORY ,sha[:2])
	os.makedirs(object_directory)
	object_path = "{}/{}".format(object_directory , sha[2:])
	f = open(object_path, "a")
	return f

# recursively build the tree object .....
def build_tree_object(name , tree):
	sha_cont = hashlib.sha1(datetime.datetime.now().isoformat() + name)
	sha = sha_cont.hexdigest()
	file = build_file_object(sha)
	for k , v in tree.items():
		if type(v) is dict:
			sha_child = build_tree_object(k , v)
			file.write("tree {} {}\n".format(sha_child , k))
		else:
			file.write("blob {} {}".format(v, k))

	return sha

def build_commit_object(tree):
	#pass
	commit_message_path = "{}/COMMIT_EDITMSG".format(SIMPLE_GIT_DIRECTORY)
	message = sys.argv[1]
	commit_user = "vivek"
	sha_cont = hashlib.sha1(datetime.datetime.now().isoformat() + commit_user)
	sha = sha_cont.hexdigest()
	file = build_file_object(sha)
	file.write("tree {}\nauthor {}\n\n{}".format(tree , commit_user , message))
	return sha

root_sha = build_tree_object("root", index_files_tree())
commit_sha = build_commit_object(root_sha)

print("commit_sha {}".format(commit_sha))


