import os

#从src中递归转移所有cpp文件到dist中，末尾须有'/'
#cpp文件重命名为：所在最后一层目录名+原名

srcPath = '/home/sunriz/pat/'
distPath = '/home/sunriz/patgit2/'

def GetCppAbDirs(path,dirs_list=[]) :
    os.chdir(path)
    abpath = os.popen('pwd').read().split()[0] + '/'
    result = os.popen('ls -F | grep /')
    try:
        temp_list = [abpath+path for path in result.read().split()]
        dirs_list += temp_list
        for each in temp_list:
            GetCppAbDirs(each,dirs_list)
    except:
        pass

def cp(src,dist):
    os.system('cp {} {}'.format(src,dist))

def main():
    cppfiles = []
    dirs = []
    dirs.append(srcPath)
    #print(dirs)
    GetCppAbDirs(srcPath,dirs)
    count = 0
    for dir in dirs:
        pre = dir.split('/')[-2]
        #print(pre)
        os.chdir(dir)
        file_names = os.popen('ls | grep .cpp').read().split()
        for each in file_names:
            fname = pre + each
            #print(fname)
            cp(dir+each,distPath+fname)
            count+=1
    print("tatal:%d"%count)

if __name__ == '__main__':
    main()
