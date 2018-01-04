import os
import shutil


#定义已存计数器
def savedmoney(ininame,savenum):
    lines = open('%s.ini' %ininame).readlines()
    oldnum = lines[6]
    oldnum = float(oldnum)
    savenum = savenum.replace('\'', '')
    savenum = float(savenum)
    savenums = oldnum+savenum
    savenums = str(savenums)
    lines[6] = savenums +'\n'
    open('%s.in' %ininame,"w").writelines(lines)
    shutil.move('%s.in' %ininame, '%s.ini' %ininame)
    return savenums

