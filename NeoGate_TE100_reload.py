import paramiko
import datetime


user = 'root'
secret = 'XXX'
port = 8022

fileName = "logFXO.txt"
accessMode = "a"
day = datetime.datetime.now()


def write_log(log):
    with open(fileName, accessMode) as myLog:
        myLog.write(log)

def rebootTE(host):
    try:
        write_log('---- ' + str(day.ctime()) + ' ---------------------\n')
        write_log('trying to connect: ' + host + '\n')
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Подключение
        client.connect(hostname=host, username=user, password=secret, port=port)

        # Выполнение команды
        stdin, stdout, stderr = client.exec_command('asterisk -rx "sip reload"')

        # Читаем результат
        data = str(stdout.read() + stderr.read())
        write_log("Был перезагружен: ")
        write_log(day.ctime() + data+'\n')
        #print(data)
        #print('done!')
        client.close()
    except Exception as e:
        write_log('!!! error: ' + str(e) + '\n')
        write_log('--\n')

rebootTE('10.10.10.32')