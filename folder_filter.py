"""
Filtering according to the number of jpg in a folder
"""

import argparse
import os
import shutil
from glob import glob
import fnmatch


base_path = "./runs/detect/carapaceImg"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--delete_num', type=int, default=100, help='Threshold for the number of jpg files to be deleted')
    opt = parser.parse_args()

def delete_folder(directory_dir, N):
    if len(fnmatch.filter(os.listdir(directory_dir), "*.jpg")) <= N:
        print(directory_dir+' has been deleted!!!!!')
        shutil.rmtree(directory_dir)

for p in glob(base_path + "/*/", recursive=True):
    delete_folder(p, opt.delete_num)

