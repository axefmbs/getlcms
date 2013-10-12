#-*-coding:utf8-*-
import datetime,time,os,shutil,re

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
def statistics(cmds):

    if len(cmds)<3:
        print 'please input like as "sta *** 2013-10-12 2013-11-12"'
        return False
    key,strstartdate,strenddate=cmds[1],cmds[2],cmds[3]

    try:
        startdate=datetime.datetime.fromtimestamp(time.mktime(time.strptime(strstartdate,"%Y-%m-%d")))
    except:
        startdate=datetime.datetime.fromtimestamp(time.mktime(time.strptime(strstartdate,"%Y%m%d")))
    try:
        enddate=datetime.datetime.fromtimestamp(time.mktime(time.strptime(strenddate,"%Y-%m-%d")))
    except:
        enddate=datetime.datetime.fromtimestamp(time.mktime(time.strptime(strenddate,"%Y%m%d")))
    print startdate.year,startdate.month,startdate.day
    print enddate.year,enddate.month,enddate.day
    while(1):
        print startdate
        year=str(startdate.year)
        month=str(startdate.month)
        if len(month)==1:month='0'+month
        day=str(startdate.day)
        if len(day)==1:day='0'+day
        print type(year)
        startdate+=datetime.timedelta(days=1)
        if startdate>=enddate:
            break


''' 
    if '-' in startdate:
        startdate=time.strptime(startdate,'%Y-%m-%d')
    else:
        startdate=time.strptime(startdate,'%Y%m%d')

    if '-' in enddate:
        enddate=time.strptime(enddate,'%Y-%m-%d')
    else:
        enddate=time.strptime(enddate,'%Y%m%d')

    year1=startdate.tm_year
    month1=str(startdate.tm_mon)
    if len(month1)==1:month1='0'+month1    
    day1=str(startdate.tm_mday)
    if len(day1)==1:day1='0'+day1\

    year2=startdate.tm_year
    month2=str(startdate.tm_mon)
    if len(month2)==1:month2='0'+month2    
    day2=str(startdate.tm_mday)
    if len(day2)==1:day2='0'+day2

    startdate=datetime.date(int(year1), int(month1), int(day1))
    enddate=datetime.date(int(year2), int(month2), int(day2))

    while(1):
        startdate+=datetime.timedelta(days=1)
        if startdate>=enddate:
            break

        year=startdate.tm_year
        month=str(startdate.tm_mon)
        if len(month)==1:month='0'+month

        day=str(startdate.tm_mday)
        if len(day)==1:day='0'+day

        print 'now is','%s-%s-%s' % (year,month,day)
'''
    #del inits

    #inits=init(paths,year,month,day)

    #lcmspath,logfile,outputpath=inits[0],inits[1],inits[2]

    
    #print key,startdate,enddate
if __name__=='__main__':
    rootpath=r'e:\test'
    #print getfiles(rootpath,'txt')
    print getdirs(rootpath)
    #print filename(r'.\abc\123.txt')
            
