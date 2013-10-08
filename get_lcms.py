#-*-coding:utf8-*-
import time,md5,os,sys

import setting as setting
import file_functions as files
import mail as mail

def login(psw):
    while(1):
        s=str(raw_input('please input the password>>>')).lower().strip()
        if s=='exit':sys.exit(0)
        m=md5.new(s)
        s=m.hexdigest()
        if s==psw:
            print 'Let\'s start working'
            break
        else:
            print 'The password you entered is incorrect.'
def init(paths,year=time.strftime("%Y"),month=time.strftime("%m"),day=time.strftime("%d")):    
    #获取当前的lcms路径
    #按照日期分类保存，每天一个文件夹，文件夹以日期命名
    #\\Beita-pc\D\2013\201309\2013-09-25保存的是2013年9月25日的lcms信息
    lcmspath=lcms_path(paths['inputpath'],year,month,day)
    #log 和输出文件夹
    logfile=logfile_path(paths['logpath'],year,month,day)
    outputpath=output_path(paths['outputpath'],year,month,day)
    
    #建立工作环境
    if os.path.isdir(paths['logpath'])==False:os.mkdir(paths['logpath'])
    if os.path.isdir(paths['outputpath'])==False:os.mkdir(paths['outputpath'])
    if os.path.isdir(outputpath)==False:os.mkdir(outputpath)    
    FILE=open(logfile,'a')
    FILE.close()

    return lcmspath,logfile,outputpath
    
def lcms_path(rootpath,year=time.strftime("%Y"),month=time.strftime("%m"),day=time.strftime("%d")):
    '''获取当前的lcms路径
    按照日期分类保存，每天一个文件夹，文件夹以日期命名
    \\Beita-pc\D\2013\201309\2013-09-25保存的是2013年9月25日的lcms信息
    默认获取当天信息'''
    year,month,day=str(year),str(month),str(day)
    return rootpath+year+'\\'+year+month+'\\'+year+'-'+month+'-'+day
def logfile_path(logpath,year=time.strftime("%Y"),month=time.strftime("%m"),day=time.strftime("%d")):
    year,month,day=str(year),str(month),str(day)
    
    return logpath+year+'-'+month+'-'+day+'.log'

def output_path(outputpath,year=time.strftime("%Y"),month=time.strftime("%m"),day=time.strftime("%d")):
    year,month,day=str(year),str(month),str(day)
    return outputpath+year+'-'+month+'-'+day

def listsub(list1,list2):
    '''两个列表相减'''
    l1,l2=len(list1),len(list2)
    if l1>=l2:
        return list(set(list1)-set(list2))
    return list(set(list2)-set(list1))
    #return [item for item in list2 if item not in list1]
           
    #l1,l2=len(list1),len(list2)
    #if l1>=l2:
    #    return list(set(list1).difference(set(list2)))
    #return list(set(list2).difference(set(list1)))
    #return list(set(list1)-set(list2))
def print_list(list):
    '''打印列表'''
    c=0
    for i in list:
        c+=1
        print '%2s. %s'%(c,files.filename(i))
    print 'total',c,'items'
def print_log(logs):
    c=0
    for log in logs:
        c+=1
        print '%2s. %s'%(c,files.filename(log))
    print 'total',c,'items'

def getfilesbeginwith(items,key):
    '''获得文件名以key开头的文件'''
    current_reports=[]
    klen=len(key)
    for file in items:
        if key==files.filename(file)[:klen]:
            current_reports.append(file)
    return current_reports

if __name__=='__main__':
    #year = time.strftime("%Y-%m-%d %H:%M:%S")
    #year = time.strftime("%Y")
    #month=time.strftime("%m")
    #day=time.strftime("%d")    
    print 'loading...'
    setting=setting.load_setting_file('setting.xml')
    
    psw=setting[0]
    #邮件服务器信息
    mail_sender=setting[1]
    #发送的邮件列表
    mail_list=setting[2]
    #文件保存信息
    paths=setting[3]
    
    #登录
    #login(psw)
    print 'initialization...'
    #按照当天日期建立工作环境
    inits=init(paths)
    lcmspath,logfile,outputpath=inits[0],inits[1],inits[2]
 
    print 'let\'s working...'
    commands=['get','see','log','send','find','del','set','to','exit','help']
    while(1):
        #exit
        cmds=raw_input('>>>').lower().strip().split(' ')
        cmd=cmds[0]
        
        if cmd not in commands:
            print cmd,'is not a command.'
            continue
        
        if len(cmds)>=1:
            #输入一个参数
            #退出
            if cmd=='exit':sys.exit(0)
            #帮助
            if cmd=='help':
                print commands
                continue
            #检查未发送的报告
            if cmd=='find':
                print 'find...'
                checks=files.getfiles(outputpath,'pdf')
                if len(cmds)==1:                    
                    print_list(checks)
                else:
                    if cmds[1] not in mail_list.keys():
                        print cmds[1],'is not a maillist'
                        continue
                    begins=getfilesbeginwith(checks,cmds[1])
                    print_list(begins)                           
                        
            #获得lcms报告
            if cmd=='get':
                print 'getting all report in',lcmspath
                reports=files.getfiles(lcmspath,'pdf')
                #print reports
                logs=files.readlogs(logfile)
                #print logs
                sublogs=listsub(logs,reports)
                if len(sublogs)>0:
                    files.writelog(reports,logfile)
                    files.copyfiles(reports,outputpath)
                else:
                    print '0 report get.'
            #查看全部的lcms
            if cmd=='see':
                print 'see lcms in',lcmspath
                lcms=files.getdirs(lcmspath)
                print_list(lcms)
            #查看发送邮件列表
            if cmd=='to':
                for key in mail_list.keys():
                    print key,':',mail_list[key]
            #查看log文件
            if cmd=='log':
                print 'files in',logfile
                logs=files.readlogs(logfile)
                if len(cmds)==1:
                    print_log(logs)
                else:
                    print_log(getfilesbeginwith(logs,cmds[1]))
                    
            #设置获取报告的日期
            if cmd=='set':
                if len(cmds)==1:
                    #默认当天日期
                    del inits
                    inits=init(paths)
                    lcmspath,logfile,outputpath=inits[0],inits[1],inits[2]
                    print 'now is',time.strftime("%Y-%m-%d")
                else:
                    #设置自己的时间，如2013-09-27或者20130927
                    try:
                        if '-' in cmds[1]:
                            date=time.strptime(cmds[1],'%Y-%m-%d')
                        else:
                            date=time.strptime(cmds[1],'%Y%m%d')
                        year=date.tm_year
                        month=str(date.tm_mon)
                        if len(month)==1:month='0'+month
                        day=str(date.tm_mday)
                        if len(day)==1:day='0'+day
                        
                        del inits
                        inits=init(paths,year,month,day)
                        lcmspath,logfile,outputpath=inits[0],inits[1],inits[2]
                        print 'now is','%s-%s-%s' % (year,month,day)
                    except:
                        print cmds[1],'is not a date string.'
            #发送邮件
            if cmd=='send':
                if len(cmds)==1:
                    print 'please set a email or a maillist.'
                    continue                
                if cmds[1] in mail_list.keys():
                    #发送到邮件列表
                    print 'send...'
                    subject=mail_sender['mail_subject']+files.filename(logfile)
                    content=mail_sender['mail_context']
                    attments=getfilesbeginwith(files.getfiles(outputpath,'pdf'),cmds[1])
                    mail.send_mail(mail_sender,mail_list[cmds[1]],subject,content, attments)                    
                elif files.ismail(cmds[1]):
                    #发送到具体的邮件
                    print 'send...'                    
                    subject=mail_sender['mail_subject']+files.filename(logfile)
                    content=mail_sender['mail_context']
                    attments=files.getfiles(outputpath,'pdf')
                    mail.send_mail(mail_sender,cmds[1],subject,content, attments)
                else:
                    print '"',cmds[1],'" is not a email or a set maillist.'
            #删除文件
            if cmd=='del':
                print 'del...'
                checks=files.getfiles(outputpath,'pdf')
                if len(cmds)==1:
                    files.delfiles(checks)
                else:
                    if cmds[1] not in mail_list.keys():
                        print cmds[1],'is not a maillist'
                        continue
                    begins=getfilesbeginwith(checks,cmds[1])
                    files.delfiles(begins)
                
