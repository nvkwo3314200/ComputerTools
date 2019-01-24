#coding=utf-8
'''
Created on 2019年1月23日

@author: Pan
'''
import os
import time
import datetime
import logging


paths= {"H:\\temp"}
expireDay = 15
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S %p"
LOG_FILE = 'my.log'
count = 0


logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
logging.FileHandler(LOG_FILE, encoding='utf-8')  

def deleteExpireFile(fileName):
    modifytime = os.path.getmtime(fileName);
    expireTime = datetime.datetime.now() - datetime.timedelta(expireDay)
    expireTime = time.mktime(expireTime.timetuple());
    if(expireTime  > modifytime):
        try:
            os.remove(fileName)
            global count 
            count = count + 1
            logging.info(u"已删除文件：" + fileName)
        except IOError as e:
            logging.error(u"删除文件失败：" + fileName)
            logging.error(e)
    
def listFile (path):
    """
        this is a statement
    """
    parents = os.listdir(path)
    for parent in parents:
        child = os.path.join(path,parent)
        #print(child)
        if os.path.isdir(child):
            listFile(child)
        else:
            deleteExpireFile(child)

if __name__ == '__main__':
    for path in paths:
        listFile(path)
    logging.info(u"共删除文件数为：" + str(count))