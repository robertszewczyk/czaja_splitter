import sys
import os
from os import listdir
from os.path import isfile
import shutil

def main():
    if(len(sys.argv) != 4):
        sys.exit('Usage: %s source_directory target_directory split_symbol' % sys.argv[0])

    if(os.path.isdir(sys.argv[1]) == False):
        sys.exit('%s is not a directory' % sys.argv[1])

    if(os.path.isdir(sys.argv[2]) == False):
        sys.exit('%s is not a directory' % sys.argv[2])

    for f in listdir(sys.argv[1]):
        if(isfile(str(sys.argv[1])+str(f))):
            list = f.split(sys.argv[3])
            directory = sys.argv[2] + list[0] + '/' + list[1]
            if not os.path.exists(directory):
                os.makedirs(directory)
            shutil.move(sys.argv[1] + f,directory)

if(__name__ == "__main__"):
    main()
