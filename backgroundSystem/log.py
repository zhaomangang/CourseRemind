import time
class LogManagement(object):
    def __init__(self,path):
        self.file =  open(path,'ab+')
        print(path)
    def logRecord(self,text):
        plain = time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))+text+'\n'
        self.file.write(plain.encode('utf-8'))
    
    def closeLog(self):
        self.file.close()

if __name__ == "__main__":
    loger = LogManagement()
    loger.logRecord('测试日志系统')
    loger.closeLog() 
