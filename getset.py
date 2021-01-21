#!/usr/bin/python3
#
# getset.py - Download images given search terms as
#             arguments.
#
# By Jim McClanahan, W4JBM (Dec 2020)
#
# Makes use of customized bing-image-downloader (BID) modules
# https://github.com/gurugaurav/bing_image_downloader
# by Guru Prasad Singh under the MIT License.
#
# The only change to BID is that files now keep their original
# names. This better fits the way I use things, making it easier
# to find where the file came from if I want to dig back a bit
# during research.
#
# This software is also released under the MIT License.

import sys, os
from datetime import datetime
# we need to import our local, tweaked version of downloader
import downloader2

# Get the current date and time to create timestamp for
# the subdirectory.
now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y_%H%M%S")
# print("date and time:",date_time)	
 
# Get the total number of arguments passed to us...
argcnt = len(sys.argv)
 
# Get the arguments list ignoring the first element (which is going
# to be something like './getimg.py').
srchfor = '+'.join(sys.argv[1:])

# This is kind of an ugly way to code (guess who started programming
# with BASIC and FORTRAN), but we want to quit if we didn't receive
# any search arguments.
if argcnt == 1:
    print("Enter one or more search terms to download images.")
    exit()

# And now that we've done all of that, we can download the images...
downloader2.download(srchfor, limit=250,  output_dir='ImageSets',
    adult_filter_off=True, force_replace=False, timeout=60)

# For the above, you can tweak to meet your needs (or, with a bit
# more work could allow command line arguments for):
#
# limit - the number of images downloades
# output_dir - the 'upper' director under which our subdirectories
#              will be created
# timeout - the timeout limit for a download attempt

# This program is designed to keep the image subdirectory free of
# duplicate files. If you don't want to do that, comment this out.
# If you don't want this, getsets.sh might be a better fit for you
# But in testing this shaved my Images subdirectory size:
# From: 4,987 items, totalling 1.3 GB
# To:   2,508 items, totalling 701.9 MB
# Requires that rdfind has been installed in Linux
os.system('rdfind -deleteduplicates true ImageSets/'+srchfor)

# To make sure files with duplicate names are captures, copies with
# the original name and a second copy with 'zzzzzImage_###' are
# saved. The rdfind command above should have removed all duplicates
# and only kept zzzzzImage files that are NOT duplicates. Now that
# we've done that, we can rename them.

fileprefix = "zzzzz"
fnames = os.listdir('ImageSets/'+srchfor)

for fname in fnames:
    if fname.startswith(fileprefix):
        os.rename('ImageSets/'+srchfor+'/'+fname, 'ImageSets/'+srchfor+'/'+fname.replace(fileprefix, '', 1))

# Now that we have the images, we rename the destination directory
# so that it includes the timestamp...
os.rename(os.path.join('ImageSets', srchfor),
    os.path.join('ImageSets', srchfor+'_'+date_time))

print("Image downloads completed!")

