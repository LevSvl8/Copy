import os
import shutil

def list_of_files(dir_from1,dir_to1):
    global dir_from,dir_to
    dir_from, dir_to = dir_from1,dir_to1
    list_of_f = os.listdir(dir_from1)
    scan_list(list_of_f)
    return list_of_f

def scan_list(list):
    for file in list:
        if os.path.isdir(dir_from+file) != True:
            shutil.copy(dir_from+'/'+file,dir_to)
        else:
            os.mkdir(dir_to+file)
            list_of_files(dir_from+file,dir_to+file)
            print(dir_to+file)



dir1 = 'C:\\Users\\Work\\Documents\\git-learn/'
dir2 = 'C:\\Users\\Work\\Documents\\test2/'

list_of_files(dir1,dir2)