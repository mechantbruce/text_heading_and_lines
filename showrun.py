from __future__ import print_function
import re
import sys

'''print AP name followed by primary, secondary, tertiary WLC configuration. 
Each AP name and primary secondary tertiary appears in the config twice (once for each radio)
so it is printed twice. One day I will figure out how to just print it once.'''
#http://stackoverflow.com/questions/4595197/how-to-grab-the-lines-after-a-matched-line-in-python
#Generator explanation: https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
run = open("show_run-config2.log", "r")

def group_by_heading( some_source ):
    buffer= []
    found = False
    for line in some_source:
        if "Cisco AP Name" in line:
            buffer.append(line)
            found = True
        elif found:
    		if "Primary" in line:
    			buffer.append(line)
    		elif "Secondary" in line:
    			buffer.append(line)
    			print("true")
    		elif "Tertiary" in line:
    			buffer.append(line)
    			print("true")
    		elif "Administrative State" in line:
    			found = False
    			print("false")
    yield buffer


for heading_and_lines in group_by_heading( run ):
	print(*heading_and_lines, sep="\n")
# process away.