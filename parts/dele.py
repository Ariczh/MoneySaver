import os
import shutil

#定义数据删除器
def deldata(ininame,delnum):
    load = open('%s.ini' %ininame,'r')
    read = load.readlines()[10]
    leno = len(str(read))
    read = read.split(', ')
    delnum = str(delnum)
    delnum = delnum.replace('\'', '')
    read.remove(delnum)
    write = read
    lenth = len(write)
    k = 0
    delstr = ''
    while k < lenth:
        delstr = delstr + write[k] + ', '
        k = k + 1
    else:
        delstr = delstr.rstrip(', ')
        load.close()
    load2nd = open('%s.ini' %ininame,'rb+')
    load2nd.seek(-leno,2)
    load2nd.truncate()
    load2nd.close()
    load3rd = open('%s.ini' %ininame,'r+')
    load3rd.seek(0,2)
    load3rd.write(delstr)
    load3rd.close()