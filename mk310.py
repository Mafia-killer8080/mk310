import platform
import os
os.system('termux-setup-storage')
#os.system('git pull')
#try:os.system('mkdir /sdcard/mk310')
#except:pass
#try:os.system('mkdir /sdcard/mk310/OK')
#except:pass
#try:os.system('mkdir /sdcard/mk310/CP')
#except:pass
try:os.system('touch .prox.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
        __import__("mk310")._site_view_
elif 'aarch' in arc:
        __import__("mk310")._site_view_()
else:
        exit(f' Unknow device machine {arc}')
 
