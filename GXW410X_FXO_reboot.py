# coding=utf-8

import sys
import telnetlib
import datetime

fileName = "logFXO.txt"
accessMode = "a"

day = datetime.datetime.now()


def write_log(log):
    with open(fileName, accessMode) as myLog:
        myLog.write(log)
		
		
def restart_server(host, password):
	try:
		write_log('---- ' + str(day.ctime()) + ' ---------------------\n')
		write_log('trying to connect: ' + host + '\n')
		tn = telnetlib.Telnet(host)
		tn.read_until(b"Password: ")
		tn.write(password.encode('ascii') + b"\n")
		l = tn.read_until("> ".encode('ascii'))
		# write_log(str(l) + '\n')
		write_log('successfully logged in' + '\n')
		tn.write('r'.encode('ascii') + b"\n")
		l = tn.read_until("> ".encode('ascii'))
		# write_log(str(l) + '\n')
		write_log("Был перезагружен: ")
		write_log(day.ctime() + '\n')

		tn.write(b"exit\n")
		write_log(tn.read_all().decode('ascii'))
	except Exception as e:
		write_log('!!! error: ' + str(e) + '\n')    
	write_log('--\n')


password = 'XXXX'
restart_server('10.10.10.35', password)
restart_server('10.10.10.37', password)
restart_server('10.10.10.39', password)