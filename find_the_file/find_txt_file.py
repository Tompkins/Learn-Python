import os
from os.path import join

the_directory = raw_input('Please enter the directory\n')
base_directory = os.path.basename(the_directory)
os.chdir(os.path.dirname(the_directory))
all_files = []
for root, dirs, files in os.walk(base_directory):
    for name in files:
        all_files.append(join(root, name))
for i in all_files:
    if '.txt' in i:
        print i
