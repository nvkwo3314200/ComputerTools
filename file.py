# coding=utf-8
def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格, 去除尾部 \ 符号
    path = path.strip().rstrip("\\")
    # 判断路径是否存在
    if not  os.path.exists(path):
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
        print (path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path + ' 目录已存在')
        return False
# 定义要创建的目录
mkpath = "d:\\qttc\\web\\"
# 调用函数
mkdir(mkpath)
