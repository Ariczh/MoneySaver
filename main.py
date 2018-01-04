#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import re
import wx
import sys
import random
import shutil

sys.path.append("parts");
import create
import choose
import dele
import saves


#主程序
print('Welcome to use SaveMoney365 to save your Money')
ininame = 'sm365conf'
got = 0.0

if os.path.exists('%s.ini'%ininame) == False: 
    endnum = 365
    firstnum = 1.0
    step = 1.0
    create.createdata(ininame, firstnum, endnum, step)

else:
    fc = open('%s.ini' %ininame).readlines()
    sums = fc[6]
    sums = float(sums)
    if sums == 66794.0:
    #if sums == 33397.5:
        print('u r winner') 
    else:
        got = choose.choosedata(ininame)
        print('You may save CNY %s0, Accept?' %got[0])
        dele.deldata(ininame,got[0])
        savedm = saves.savedmoney(ininame,got[0])
        print('You\'re already saved CNY %s0!'%savedm)
