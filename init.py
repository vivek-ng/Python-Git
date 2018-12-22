#!/usr/bin/env python

import sys
import os

# for args in sys.argv[1:]:
#     print(args)

SIMPLE_GIT_DIRECTORY = ".simple-git"
OBJECTS_DIRECTORY = "{}/objects".format(SIMPLE_GIT_DIRECTORY)
REFS_DIRECTORY = "{}/refs".format(SIMPLE_GIT_DIRECTORY)

if os.path.isdir(SIMPLE_GIT_DIRECTORY):
	print("Git Repository already exists!!!!")
	sys.exit()


def build_objects_directory():
	os.mkdir(OBJECTS_DIRECTORY)
	os.mkdir("{}/info".format(OBJECTS_DIRECTORY))
	os.mkdir("{}/pack".format(OBJECTS_DIRECTORY))

def build_refs_directory() :
	os.mkdir(REFS_DIRECTORY)
	os.mkdir("{}/head".format(REFS_DIRECTORY))
	os.mkdir("{}/tags".format(REFS_DIRECTORY))


def initialize_head() :
	#os.mkdir("{}/HEAD".format(SIMPLE_GIT_DIRECTORY))
	file_obj = open("{}/HEAD".format(SIMPLE_GIT_DIRECTORY) , 'w+')
	file_obj.write("ref: refs/heads/master")


os.mkdir(SIMPLE_GIT_DIRECTORY)
build_objects_directory()
build_refs_directory()
initialize_head()

print("Initialized Git Repository in {}".format(SIMPLE_GIT_DIRECTORY))







