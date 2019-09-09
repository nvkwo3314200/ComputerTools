#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 16
PADDING = '\0'
pad_it = lambda s: s+(16 - len(s)%16)*PADDING
key = b'chenlamdba!!0123'
iv = b'chen@#!`chenchen'

#使用aes算法，进行加密解密操作
#为跟java实现同样的编码，注意PADDING符号自定义
def encrypt_aes(sourceStr):
    generator = AES.new(key, AES.MODE_CFB, iv)
    crypt = generator.encrypt(pad_it(sourceStr).encode('utf-8'))
    cryptedStr = base64.b64encode(crypt)
    return cryptedStr.decode('utf-8')

def decrypt_aes(cryptedStr):
    generator = AES.new(key, AES.MODE_CFB, iv)
    cryptedStr = base64.b64decode(cryptedStr)
    recovery = generator.decrypt(cryptedStr)
    decryptedStr = recovery.rstrip(PADDING.encode('utf-8'))
    return decryptedStr.decode('utf-8')


if __name__ == '__main__':
    while(True):
        type = input('请输入类型， 1.解密  2.加密（默认为解密, 其它退出）:')
        try:
            if type == '1' or type == '':
                str = input('请输入要解密的字符串:')
                print ('解密结果:', '【' +decrypt_aes(str) + '】')
            elif type == '2':
                str = input('请输入要加密的字符串:')
                print ('加密结果:', '【' + encrypt_aes(str) + '】')
            else:
                print('退出')
                break
        except:
            print('操作失败， 请重新输入')    
    
    
    


    
    
    
    
    