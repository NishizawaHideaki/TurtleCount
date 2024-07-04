"""
Filtering according to the aspect ratio of carapace
"""
import argparse
import os
import shutil
from glob import glob
import fnmatch

all_file_num = 0
erase_file_num = 0
aspect = 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--aspect_ratio', type=float, default=0.5, help='aspect ratio of carapace')
    opt = parser.parse_args()

dir_path = "./runs/detect/carapaceImg"
for N in glob(dir_path + "/*/", recursive=True):
    
    erase_flag = 0  
    
    for file in glob(N + '/*.txt'):
        
        lines = []
        all_file_num += 1
        
        with open(file) as f:
            
            lines = f.readlines()
            
            for box in lines:
                tmp = box.rstrip().split()
                
                if tmp[3] < tmp[4]:
                    aspect = float(tmp[3]) / float(tmp[4])
                else:
                    aspect = float(tmp[4]) / float(tmp[3])
                
                if opt.aspect_ratio <= aspect:
                    pass
                else:
                    erase_flag = 1
                    
        if erase_flag == 1:
            erase_file_num += 1

            os.remove(file)
            os.remove(file[:-4] + ".jpg")
            print(file + ' has been deleted')
            print(file[:-4] + ".jpg" + ' has been deleted')
    
    #If the number of text files is 0, delete the folder
    if len(fnmatch.filter(os.listdir(N), "*.txt")) == 0:
        print(N+' has been deleted!!!!!')
        shutil.rmtree(N)
    
print("all_file_num:" + str(all_file_num))
print("erase_file_num:" + str(erase_file_num))


