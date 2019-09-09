# 用python语言来更好的管理电脑
开发中使用的都是最基础的语法，达到很好的学习的目的

### 使用环境， 基于python3 && pip3
```
Linux 安装方法
- wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
- tar -zxvf Python-3.6.1.tgz
- cd Python-3.6.1
- ./configure --prefix=/usr/local/python3
- make
- make install
- ln -s /usr/local/python3/bin/python3 /usr/bin/python3
- ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
- vim ~/.bash_profile
- export PATH=$PATH:$HOME/bin:/usr/local/python3/bin
```

### 清理电脑中的临时文件 [clearTempFile.py](https://github.com/nvkwo3314200/ComputerTools/blob/master/clearTempFile.py)
电脑中有很多很长时间不用的文件，不能及时清理，很占空间。
里面的方法能很好的，清理paths下超过expireDay天数的文件.
<br>
**Tips:可将此方法放在系统的计划任务中,达到定期清理的目的**

### 加解密小工具 [dev.py]
- 安装依赖：pip install pycrypto
