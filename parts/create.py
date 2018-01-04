import os

#定义文件生成器
#生成一个空文件
def createini():
    os.system("cd.>%s.ini" %ininame)
    first = open('%s.ini' %ininame,'w')
    first.close()

#定义数据创建器
def createdata(ininame,hajime,owari,hitoashi):
    datas = []
    while hajime <= owari:
        datas.append(hajime)
        hajime = hajime + hitoashi
    else:
        strdatas = str(datas)
        strdatas = strdatas[1:-1]
        os.system("cd.>%s.ini" %ininame)
        base = open('%s.ini' %ininame,'w')
        base.write('[SaveMoney365]'+'\n\r'+'\n\r'+'Money='+'\n\r'+'0'+'\n\r'+'LIST=\n\r'+strdatas)
        base.close()