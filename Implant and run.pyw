#Startup .py File Creator

import os
import subprocess as sp

path = "spotify restart.pyw"
outName = "spot res.pyw"
newfilepath = os.path.join(os.path.expanduser('~'), 'AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup', outName)

#######################################################
try:
    with open (path, 'r', encoding='utf-8') as f:
        contt = f.read()
except:
    print('Sorry, Invalid source file')

#-----------------------------------------------------#
try:
    with open (newfilepath, 'w', encoding='utf-8') as f:
        f.write(contt)
except:
    print('Sorry, Invalid destination file')

#######################################################

# sp.Popen('', shell = True)
