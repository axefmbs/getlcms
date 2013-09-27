#-*-coding:utf8-*-
import setting as setting

setting=setting.load_setting_file('setting.xml')
password=setting[0]
sender=setting[1]
mail_list=setting[2]

#print setting
print password
print sender
print mail_list
