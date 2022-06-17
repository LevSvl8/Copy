from distutils.dir_util import copy_tree
import shutil
import os

dir_from = 'C:\\proects/'
dir_to = 'C:\\PerfLogs/'

get_files = os.listdir(dir_from) # файлы в список

for file in get_files: # в цикле проходимся по каждому файлу и, если это не папка, то txt и py копируем в dir_to
    if os.path.isdir(dir_from+file) == False:
        if file.endswith('.txt') or file.endswith('.py'):
            shutil.copy(os.path.join(dir_from+file), os.path.join(dir_to))
    else:               # натыкаясь на папку, снова делаем список и в цикле проходимся по каждому файлу
        get_files2 = os.listdir(dir_from + file)
        os.mkdir(dir_to+file)
        for file2 in get_files2:
            if file2.endswith('.txt') or file2.endswith('.py'):
                shutil.copy(os.path.join(dir_from + file+"/"+file2), os.path.join(dir_to+"/"+file))