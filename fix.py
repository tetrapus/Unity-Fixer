#!/usr/bin/env python

# Save a new, transparent file which is the same size as the original

import sys
import os
import os.path
import shutil

from PIL import Image

# Constants
UNITY_FOLDER = "/usr/share/unity"
RESOURCES_FOLDER = "resource_lists"
DEFAULT_BACKUP = "~/.unitybackup"

# Check unity folder
try:
	folder = os.listdir(UNITY_FOLDER)
	folder = [i for i in folder if i.isdigit()][0]
except OSError, IndexError:
	print "No unity resource folder found, aborting"
	sys.exit(1)
else:
	try:
		blankify = open("%s/%s.txt" % (RESOURCES_FOLDER, folder)).read().split()
	except IOError:
		print "Unity version not supported."
		sys.exit(1)

# Ask for the backup folder
print "Select backup folder:"
backupf = raw_input("[Enter for %s] " % DEFAULT_BACKUP)
if not backupf: backupf = DEFAULT_BACKUP

# Back it up
shutil.copytree("%s/%s" % (UNITY_FOLDER, folder), backupf)

# List resources to blank
print "Resources to blank:"
print "\t".join(blankify)
print "Select resources to keep:"
remove = raw_input("[Enter for none, regexp to select]")
while not remove:
	blankify = [i for i in blankify if not re.search(remove, i)]
	print "Resources to blank:"
	print "\t".join(blankify)
	print "Select resources to keep:"
	remove = raw_input("[regexp to select, enter when finished]")

additional = None
while additional not in "yn":
	additional = raw_input("Add additional resources? (y/n) ")
	if additional == "y":
		resource = True
		while resource:
			print "Other resources:"
			print "\t".join(i for i in os.listdir("%s/%s" % (UNITY_FOLDER, folder)) if i not in blankify)		
			resource = raw_input("[Enter to continue, exact name to add] ")
			if resource: blankify.append(resource)
print "Resources to blank:"
print "\t".join(blankify)

for res in sys.argv:
    try:
        size = Image.open(res).size
        Image.new('RGBA', size, (255, 255, 255, 0)).save(os.path.join(path, res), res.rsplit(".", 1)[-1])
    except:
        print "Could not process %s" % res
        raise
        
