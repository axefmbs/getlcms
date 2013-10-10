#-*-coding:utf8-*-
import smtplib, mimetypes,os,types
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  
from email.mime.multipart import MIMEMultipart

import file_functions as functions

def send_mail(sender,mail_list,subject,content, files):
    '''
sender:
{'mail_user': 'axefmbs', 'mail_pass': '123454', 'mail_postfix': 'gmail.com', 'mail_host': 'smtp.gmail.com:587'}
mail_list:
qshi@biortus.com;dxu@biortus.com
    '''
    try:
        mail_host=sender['mail_host']
        mail_user=sender['mail_user']
        mail_pass=sender['mail_pass']
        mail_postfix=sender['mail_postfix']
        mail_from=mail_user+"<"+mail_user + "@" + mail_postfix + ">" 
 
        message = MIMEMultipart()
        message.attach(MIMEText(content))
        message["Subject"] = subject
        message["From"] = mail_from
        
        #mail_list 可能传入字符串，在这里要将其分割成列表，可能有“;”；“,”；“ ”分隔，分情况考虑
        if type(mail_list) is types.StringType:
            if ';' in mail_list:
                mail_list=mail_list.split(';')
            elif ',' in mail_list:
                mail_list=mail_list.split(',')
            elif ' ' in mail_list:
                mail_list=mail_list.split(' ')
            
        message["To"] = ";".join(mail_list)

        print 'attachment...'
        c=0
        for file in files:
            if file != None and os.path.exists(file):
                ctype, encoding = mimetypes.guess_type(file)
                if ctype is None or encoding is not None:
                    ctype = "application/octet-stream"
                maintype, subtype = ctype.split("/", 1)
                c+=1
                print '%2d. %s ...' % (c,functions.filename(file))
                #添加附件
                attachment = MIMEImage((lambda f: (f.read(), f.close()))(open(file, "rb"))[0], _subtype = subtype)
                attachment.add_header("Content-Disposition", "attachment", filename = functions.filename(file))
                message.attach(attachment)
        print 'senting',c,'files to[',message["To"],']...'

        #设置邮件服务器
        print 'setting mail host...'
        smtp = smtplib.SMTP(mail_host)
        smtp.starttls()
        #smtp.connect(MAIL_HOST,MAIL_PORT)

        #登录邮箱服务器
        print 'loginning...'
        smtp.login(mail_user, mail_pass)

        #开始发送邮件
        print 'sending...'
        smtp.sendmail(mail_from, mail_list, message.as_string())
        print 'ok.'
        smtp.quit()  
 
        return True 
    except Exception, errmsg:  
        print "Send mail failed to:%s" % errmsg  
        return False
    
def parser_sender(sender,mail_list):
    #弃用
    mail_host=sender['mail_host']
    mail_user=sender['mail_user']
    mail_pass=sender['mail_pass']
    mail_postfix=sender['mail_postfix']
    mail_from=mail_user+"<"+mail_user + "@" + mail_postfix + ">"

    return mail_host,mail_user,mail_pass,mail_postfix,mail_from,mail_list
    
if __name__=='__main__':
    import setting as setting
    setting=setting.load_setting_file('setting.xml')
    mail_sender=setting[1]
    mail_list=setting[2]

    
    mail_host=mail_sender['mail_host']
    mail_user=mail_sender['mail_user']
    mail_pass=mail_sender['mail_pass']
    mail_postfix=mail_sender['mail_postfix']
    mail_from=mail_user+"<"+mail_user + "@" + mail_postfix + ">"

    print mail_host,mail_user,mail_pass,mail_postfix,mail_from
    #print parser_sender(mail_sender,mail_list)
