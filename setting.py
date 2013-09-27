# -*- coding: utf-8 -*-
try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et

#读取xml文件
def load_setting_file(fileName):
    password=''
    sender={}
    mail_list={}
    paths={}
    
    root = et.parse(fileName).getroot()

    password=root.find('password').text

    elems=root.getiterator('mail_sender')    
    for elem in elems.next():
        sender[elem.tag]=elem.text
    
    elems=root.getiterator('mail_list')
    for elem in elems.next():
        mail_list[elem.tag]=elem.text

    elems=root.getiterator('paths')
    for elem in elems.next():
        paths[elem.tag]=elem.text
        
    return password,sender,mail_list,paths

if __name__ == '__main__':
    #print dir(et)

    setting=load_setting_file('setting.xml')
    password=setting[0]
    mail_sender=setting[1]
    mail_list=setting[2]
    paths=setting[3]

    print password
    print mail_sender.keys()
    print mail_list.keys()
    print paths.keys()

    print
    print setting
