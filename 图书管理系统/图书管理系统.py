import os
import sys
os.chdir("F:\\Win版 ps 2022\\APythondaima\\图书管理系统")
class LMS:
    def menu(self):
        while True:
            print("·注册\t1\n·登录\t2")
            key = input("请选择您要操作项目数字：")
            print('-' * 33)
            if key == '1':
                self.register()
            elif key == '2':
                self.login()
            else:
                print('输入错误！')
                print('-' * 33)
                self.menu()
    def register(self):
        usern = input('请输入新的账户名称(只能五位)：')
        passw = input('请输入新的帐户密码(至少六位)：')
        file = "F:\\Win版 ps 2022\\APythondaima\\图书管理系统\\用户信息储存.txt"
        with open(file,'r+') as f:
            infol = f.readlines()
            line = [line.strip().split(',') for line in infol]
            if len(usern) == 5 and len(passw) >= 6:
                for info in line:
                    if usern == info[0] and passw == info[1]:
                        print()
                        print("已被注册！")
                        print('-' * 30)
                        self.menu()
                else:
                    with open(file,'a') as f:
                        f.writelines([usern,',',passw,',','0',',','非借阅状态','\n'])
                        f.seek(0)
                    print()
                    print("注册成功！")
                    print('-' * 33)
                    self.menu()
            else:
                print()
                print("输入不合格，请重新输入！")
                print('-' * 33)
                self.register()
    def login(self):
        global username,password
        username = input('请输入您的账户名称：')
        password = input('请输入你的账户密码：')
        file = "F:\\Win版 ps 2022\\APythondaima\\图书管理系统\\用户信息储存.txt"
        with open(file,'r') as f:
            infol = f.readlines()
            line = [line.strip().split(',') for line in infol]
            for inf in line:
                if username == inf[0] and password == inf[1]:
                    print()
                    print("已成功登录！")
                    print('-' * 33)
                    self.getm()
            else:
                print()
                print("无对应用户信息！")
                print("账户名称或密码输入有误！")
                print('-' * 33)
                self.menu()
    def getm(self):
        print("""·查询图书\t1
·借阅图书\t2
·归还图书\t3
·添删图书\t4
·个人信息\t5
·退出系统\t6\n""")
        k = input("请选择您要操作项目数字：")
        if k == '1':
            print('-' * 33)
            self.Qb()
        elif k == '2':
            print('-' * 33)
            self.Bb()
        elif k == '3':
            print('-' * 33)
            self.Rb()
        elif k == '4':
            print('-' * 33)
            self.ASb()
        elif k == '5':
            print('-' * 33)
            self.UIf()
        elif k == '6':
            print('-' * 33)
            print("已退出系统！")
            print('-' * 33)
            sys.exit()
    def Qb(self):
        file0 = "F:\\Win版 ps 2022\\APythondaima\\图书管理系统\\图书储存.txt"
        with open(file0,'r',encoding = 'gbk') as f0:
            lst = f0.readlines()
            li = [line.strip().split(',') for line in lst]
            ln = li[0]
            le = li[1:]
            print(ln[0],'\t',ln[1],'\t\t\t',ln[2],'\t',ln[3])
            for l in le:
                if len(l[1]) < 4:
                    print(l[0],'\t',l[1],'\t\t\t\t',l[2],'\t\t',l[3])
                elif 4 <= len(l[1]) < 8:
                    print(l[0],'\t',l[1],'\t\t\t',l[2],'\t\t',l[3])
                else:
                    print(l[0],'\t',l[1],'\t\t' ,l[2],'\t\t',l[3])
            print('-' * 30)
            self.getm()
    def Bb(self):
        global tim
        file0 = "F:\\Win版 ps 2022\\APythondaima\\图书管理系统\\图书储存.txt"
        with open(file0,'r',encoding = 'gbk') as f0:
            lst = f0.readlines()
            li = [line.strip().split(',') for line in lst]
            ln = li[0]
            le = li[1:]
            bk = input("请输入您要借阅的图书的编号：\n")
            print(le)
            print(bk)
            for bi in le:
                if bk in bi:
                    if int(bi[2]) > 0:
                        bi[2] = str(int(bi[2]) - 1)
                        bi[3] = str(int(bi[3]) + 1)
                        vl1 = [','.join(ls) + '\n' for ls in li]
                        with open(file0,'w') as f0:
                            f0.writelines(vl1)
                            f0.seek(0)
                            print("已成功借阅，祝您阅读愉快！")
                        file3 = "F:\\Win版 ps 2022\\APythondaima\\图书管理系统\\用户信息储存.txt"
                        with open(file3,'r') as f3:
                            infol3 = f3.readlines()
                            line3 = [line3.strip().split(',') for line3 in infol3]
                            for inf3 in line3:
                                if username == inf3[0] and password == inf3[1]:
                                    tim = int(inf3[2])
                                    tim += 1
                                    for inf3 in line3:
                                        if username == inf3[0] and password == inf3[1]:
                                            inf3[2] = str(tim)
                                            ul3 = [','.join(us3) + '\n' for us3 in line3]
                                            with open(file3,'w') as f2:
                                                f2.writelines(ul3)
                                                f2.seek(0)
                        file = "F:\\Win版 ps 2022\\APythondaima\\图书管理系统\\用户信息储存.txt"
                        with open(file,'r') as f:
                            infol = f.readlines()
                            line = [line.strip().split(',') for line in infol]
                            for inf in line:
                                if username == inf[0] and password == inf[1]:
                                    if inf[3] == '非借阅状态':
                                        inf[3] = '借阅状态' + f'-{bk}'
                                    else:
                                        inf[3] += f'-{bk}'
                                    ul1 = [','.join(us) + '\n' for us in line]
                                    with open(file,'w') as f:
                                        f.writelines(ul1)
                                        f.seek(0)
                                    print('-' * 33)
                                    self.getm()
                    else:
                        print("此图书已全部借出！")
                        print('-' * 33)
                        de = input("继续借阅按：1\n返回按：2\n")
                        if de == '1':
                            print('-' * 33)
                            self.Bb()
                        elif de == '2':
                            print('-' * 33)
                            self.getm()
            else:
                print('-' * 33)
                print('无对应图书!')
                print('-' * 33)
                self.getm()
    def Rb(self):
        global tim
        file3 = "F:\\Win版 ps 2022\\APythondaima\\图书管理系统\\用户信息储存.txt"
        with open(file3,'r') as f3:
            infol3 = f3.readlines()
            line3 = [line3.strip().split(',') for line3 in infol3]
            for inf3 in line3:
                if username == inf3[0] and password == inf3[1]:
                    tim = int(inf3[2])
                    with open(file3,'r') as f4:
                        infol4 = f4.readlines()
                        line4 = [line4.strip().split(',') for line4 in infol4]
                        for inf4 in line4:
                            if username == inf4[0] and password == inf4[1]:
                                tim = int(inf4[2])
                                if tim > 0:
                                    bk = input("请输入您要归还的图书的编号：\n")
                                    file = "F:\\Win版 ps 2022\\APythondaima\\图书管理系统\\用户信息储存.txt"
                                    with open(file,'r') as f:
                                        infol = f.readlines()
                                        line = [line.strip().split(',') for line in infol]
                                        for inf in line:
                                            if username == inf[0] and password == inf[1]:
                                                if bk in inf[3]:
                                                    tim -= 1
                                                    for inf4 in line4:
                                                        if username == inf4[0] and password == inf4[1]:
                                                            inf4[2] = str(tim)
                                                            ul4 = [','.join(us4) + '\n' for us4 in line4]
                                                            with open(file3,'w') as f4:
                                                                f4.writelines(ul4)
                                                                f4.seek(0)
                                                    file0 = "F:\\Win版 ps 2022\\APythondaima\\图书管理系统\\图书储存.txt"
                                                    with open(file0,'r',encoding = 'gbk') as f0:
                                                        lst = f0.readlines()
                                                        li = [line.strip().split(',') for line in lst]
                                                        ln = li[0]
                                                        le = li[1:]
                                                        for bi in le:
                                                            if bk in bi:
                                                                bi[2] = str(int(bi[2]) + 1)
                                                                vl1 = [','.join(ls) + '\n' for ls in li]
                                                                with open(file0,'w') as f0:
                                                                    f0.writelines(vl1)
                                                                    f0.seek(0)
                                                                    print("已成功归还，欢迎您的借阅！")
                                                    file = "F:\\Win版 ps 2022\\APythondaima\\图书管理系统\\用户信息储存.txt"
                                                    with open(file,'r') as f:
                                                        infol = f.readlines()
                                                        line = [line.strip().split(',') for line in infol]
                                                        for inf in line:
                                                            if username == inf[0] and password == inf[1]:
                                                                inf[3] = inf[3].replace( f'-{bk}','')
                                                                if inf[3] == '借阅状态':
                                                                    inf[3] = '非借阅状态'
                                                                ul1 = [','.join(us) + '\n' for us in line]
                                                                with open(file,'w') as f:
                                                                    f.writelines(ul1)
                                                                    f.seek(0)
                                                                print('-' * 33)
                                                                self.getm()
                                                else:
                                                    print()
                                                    print("未借阅此书,请重新操作！")
                                                    print('-' * 33)
                                                    de = input("继续归还按：1\n返回按：2\n")
                                                    if de == '1':
                                                        print('-' * 33)
                                                        self.Rb()
                                                    elif de == '2':
                                                        print('-' * 33)
                                                        self.getm()
                                else:
                                    print("处于未借阅状态，请重新操作！")
                                    print('-' * 33)
                                    self.getm()
    def ASb(self):
        file0 = "F:\\Win版 ps 2022\\APythondaima\\图书管理系统\\图书储存.txt"
        with open(file0,'r',encoding = 'gbk') as f0:
            lst = f0.readlines()
            li = [line.strip().split(',') for line in lst]
            ln = li[0]
            le = li[1:]
            de = input("请输入（清空1 添加2 返回其他键）：")
            if de == '1':
                bk = input("请输入您要清空的图书的编号：\n")
                for bi in le:
                    if bk in bi:
                        bi[2] = str(0)
                        vl1 = [','.join(ls) + '\n' for ls in li]
                        with open(file0,'w') as f0:
                            f0.writelines(vl1)
                            f0.seek(0)
                        print("已清空此图书库存！")
                        print('-' * 33)
                        self.getm()
            elif de == '2':
                tp = input("请输入图书类型对应的大写字母：")
                bn = input("请输入图书名称(入库,谨慎输入)：")
                nb = input("请输入需要添加的图书的数量：")
                for bi in le:
                    if bn == bi[1]:
                        bi[2] = str(int(bi[2]) + int(nb))
                        vl1 = [','.join(ls) + '\n' for ls in li]
                        with open(file0,'w') as f0:
                            f0.writelines(vl1)
                            f0.seek(0)
                        print("已添加，入库成功！")
                        print('-' * 33)
                        self.getm()
                    else:
                        ml = (bi[0][1:] for tp in bi[0])
                        m = max(ml)
                        bkm = tp + m
                        bk = tp + str(int(m) + 1)
                        lbk = [bk,bn,nb,'0']
                        if bkm == bi[0]:
                            lbkm = bi
                            where = li.index(lbkm) + 1
                            li.insert(where,lbk)
                            nvl1 = [','.join(nls) + '\n' for nls in li]
                            with open(file0,'w') as f0:
                                f0.writelines(nvl1)
                                f0.seek(0)
                            print("已添加，入库成功！")
                            print('-' * 33)
                            self.getm()
            else:
                print('-' * 33)
                self.getm()
    def UIf(self):
        file = "F:\\Win版 ps 2022\\APythondaima\\图书管理系统\\用户信息储存.txt"
        with open(file,'r') as f:
            infol = f.readlines()
            line = [line.strip().split(',') for line in infol]
            for inf in line:
                if username in inf and password in inf:
                    print(f'账户 {inf[0]} 的信息为：\n\t处于{inf[3]}')
                    print('-' * 33)
                    self.getm()
print("-----欢迎进入图书管理系统-----")
lms = LMS()
lms.menu()
