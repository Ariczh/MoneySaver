import os
import random

#定义数据抽选器
def choosedata(ininame):
    loadini = open('%s.ini' %ininame,'r')
    readini = [loadini.readlines()[10]]
    readini = str(readini)
    readini = readini.lstrip('[')
    readini = readini.rstrip(']')
    readini = readini.strip()
    readini = readini.split(", ")
    r = map(float,readini)
    temp = []
    for j in readini:
        temp.append(j)
    readini = list(temp)
    #随机抽取
    ran = random.sample(readini,1)
    return ran
