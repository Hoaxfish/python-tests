import os
 
def listdirs(rootdir):
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            print(d)
            listdirs(d)
 
#rootdir = 'path/to/dir'
rootdir = "C:/Users/DF/Desktop"
listdirs(rootdir)