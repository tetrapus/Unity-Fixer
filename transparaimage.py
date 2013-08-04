#!/usr/bin/env python

# Save a new, transparent file which is the same size as the original

import sys
import os.path

from PIL import Image
script = sys.argv.pop(0);

if not sys.argv:
    print "Usage: %s [path] file1 file2 ..." % script

elif os.path.isdir(sys.argv[0]):
    path = sys.argv.pop(0)
else:
    path = "."


for file in sys.argv:
    try:
        size = Image.open(file).size
        Image.new('RGBA', size, (255, 255, 255, 0)).save(os.path.join(path, file), file.rsplit(".", 1)[-1])
    except:
        print "Could not process %s" % file
        raise
        
