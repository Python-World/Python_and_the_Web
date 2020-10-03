import optparse
from socket import *
from threading import *

lock=Semaphore(value=1)

def connScan(tgthost,tgtport):
	try:
		skt=socket(AF_INET,SOCK_STREAM)
		skt.connect((tgthost,tgtport))
		skt.send(('hello\r\n').encode('utf-8'))
		results=skt.recv(100)
		lock.acquire()
		print(f'[+] {tgtport} is open')
	except:
		lock.acquire()
		print(f'[-] {tgtport} is closed')
	finally:
		lock.release()
		skt.close()

def portScan(tgthost,tgtports):
	try:
		tgtIP=gethostbyname(tgthost)
	except:
		print(f'Cannot resolve {tgthost} unknown')
	try:
		tgtname=gethostbyaddr(tgtIP)
		print(f'Scan results for {tgtname[0]}')
	except:
		print(f'Scan results for {tgtIP}: ')
	setdefaulttimeout(1)
	for tgtport in tgtports:
		t=Thread(target=connScan,args=(tgthost,int(tgtport)))
		t.start()

def Main():
	parser=optparse.OptionParser("usage: %prog [options] arg1 arg2")
	parser.add_option("-H","--host",dest="tgthost",default="127.0.0.1",type="string",help="specify hostname to run on")
	parser.add_option("-p","--port",dest="tgtport",default=80,type="string",help="port number to run on")
	(options,args)=parser.parse_args()
	if (options.tgthost==None) | (options.tgtport==None):
		print(parser.usage)
		exit(0)
	else:
		tgthost=options.tgthost
		tgtports=str(options.tgtport).split(',')
	portScan(tgthost,tgtports)

if __name__=='__main__':
	Main()
