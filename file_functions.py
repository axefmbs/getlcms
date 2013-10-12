#-*-coding:utf8-*-
import os,shutil,re

def getfiles(rootpath,filetype='all'):
    #if os.path.isdir(rootpath)==False:return False
    file_list=[]
    if filetype=='all':
        for root,dirs,files in os.walk(rootpath):
            for file in files:
                file_list.append(os.path.join(root,file))
        return file_list
        #return [os.path.join(root,file) for file in os.listdir(rootpath) if os.path.isfile(os.path.join(rootpath,file))]
    else:
        for root,dirs,files in os.walk(rootpath):
            for file in files:
                #print os.path.splitext(file),os.path.splitext(file)[1][1:]
                if os.path.splitext(file)[1][1:]==filetype:
                    file_list.append(os.path.join(root,file))
        return file_list

def getdirs(rootpath,):
    #if os.path.isdir(rootpath)==False:return False
    try:
        return [os.path.join(rootpath,elem) for elem in os.listdir(rootpath) if os.path.isdir(os.path.join(rootpath,elem))]
    except:
        return []
            
    #dir_list=[]
    #for elem in os.listdir(rootpath):
    #    dir=os.path.join(rootpath,elem)
    #    if os.path.isdir(dir):
    #        dir_list.append(dir)
    #return dir_list
    
    #for root,dirs,files in os.walk(rootpath):
    #    for dir in dirs:
    #        dir_list.append(os.path.join(root,dir))
    #return dir_list

def copyfiles(files,outputpath):
    c=0
    for file in files:
        c+=1
        print 'copying...',c,filename(file)
        shutil.copy(file,outputpath)
    print '%s files is copyed!' % c
   
def delfiles(files):
    c=0
    for file in files:
        c+=1
        print 'deleting...',c,filename(file)
        os.remove(file)
    print '%s files is deleted!' % c
    
def filename(filepath):
    '''
    input: .\abc\123.txt
    return: 123.txt
    '''
    return os.path.basename(filepath)

def writelog(logs,logfile):
    try:
        #如果log文件存在并正确读取，则打开文件并追加内容
        FILE=open(logfile,'a')
    except:
        #如果log文件不存在或不正确读取，则新建文件并写入内容
        FILE=open(logfile,'w')
    for log in logs:
        FILE.write(log+'\n')
    FILE.close()
    
def readlogs(logfile):
    try:
        #如果log文件存在
        #for log in open(logfile,'rb+').readlines():
        #        logs.append(log.strip())
        #return logs
        return [log.strip() for log in open(logfile,'rb+').readlines()]
    except:
        #如果log文件不存在
        return []
def ismail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
        return False

if __name__=='__main__':
    rootpath=r'e:\test'
    #print getfiles(rootpath,'txt')
    print getdirs(rootpath)
    #print filename(r'.\abc\123.txt')
            
