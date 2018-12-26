#!/usr/bin/env python

import sys
import subprocess


comm_length = len(sys.argv)
# if comm_length < 2:
# 	print("wrong usgage need to pass a command to work!")
# 	sys.exit()

exec_options = sys.argv[1:]
print(exec_options)
subprocess.call(exec_options)
