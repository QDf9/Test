import os
os.chdir("F:\\Win版 ps 2022\\APythondaima\\网上火车售票系统")
title = ['车次 ', '出发站-到达站 ', '出发时间 ', '到达时间 ', '票数 ']
tra = ['T40', 'T298', 'Z158', 'Z62','G8561']
place = ['成都-重庆', '杭州-上海', '长春-北京', '长春-北京','成都-泸州']
start = ['00:12', '00:06', '12:48', '21:57','20:00']
final = ['12:20', '10:50', '21:06', '06:08','04:00']
num = [{'无座':[14,100],'一等':[6,400],'二等': [0,200]},
       {'无座':[13,100],'一等':[5,400],'二等': [1,200]},
       {'无座':[12,100],'一等':[7,400],'二等': [2,200]},
       {'无座':[11,100],'一等':[8,400],'二等': [3,200]},
       {'无座':[10,100],'一等':[9,400],'二等': [4,200]}]
tim = [2] 
m = dict(zip(tra, start))
n = dict(zip(tra, place))
class Tts:
    def menu(self):
        print("·注册\t1\n·登录\t2")
        key = input("请选择您要操作项目数字：")
        print('-' * 33)
        return str(key)
    def main(self):
        while True:
            key = self.menu()
            if key == '1':
                self.register()
                continue
            elif key == '2':
                self.login()
            else:
                print('输入错误！')
    def getmenu(self):
        print("·购票\t1\n·改签\t2\n·退票\t3\n·退出\t4")
        k = input("请选择：")
        if k == '1':
            print('-' * 33)
            self.ticket()
        elif k == '2':
            print('-' * 33)
            print("亲，你是否确定进行改签？")
            dec = input("请输入 是/否：")
            print()
            if dec == '是':
                if tim[0] == 2:
                    print("您未买票，请再次确认")
                    print('-' * 33)
                    self.getmenu()
                else:
                    self.rebk()
            elif dec == '否':
                self.getmenu()
        elif k == '3':
            print('-' * 33)
            print("亲，你是否确定进行退票？")
            dec = input("请输入 是/否：")
            if dec == '是':
                if tim[0] == 2:
                    print()
                    print("您未买票，请再次确认")
                    print('-' * 33)
                    self.getmenu()
                else:
                    self.rett()
            elif dec == '否':
                print('-' * 33)
                self.getmenu()
        elif k == '4':
            print("已退出")
            print('-' * 33)
##############################################################################
    def register(self):
        username = input('请输入新的账户名称：')
        password = input('请输入新的帐户密码：')
        infput = [username, password]
        file = "F:\\Win版 ps 2022\\APythondaima\\网上火车售票系统\\用户信息.txt"
        with open(file,'r+') as f:
            infol = f.readlines()
            line = [line.strip().split(',') for line in infol]
            if infput in line:
                print()
                print("已被注册！")
                print('-' * 30)
            else:
                f.writelines([username,',', password,'\n'])
                print()
                print("注册成功！")
                print('-' * 33)
    def login(self):
        username = input('请输入您的账户名称：')
        password = input('请输入你的账户密码：')
        infput = [username,password]
        file = "F:\\Win版 ps 2022\\APythondaima\\网上火车售票系统\\用户信息.txt"
        with open(file,'r') as f:
            infol = f.readlines()
            line = [line.strip().split(',') for line in infol]
            if infput in line:
                print()
                print("已成功登录！")
                print('-' * 33)
                self.getmenu()
            else:
                print("无该用户信息！")
                print('-' * 33)
                self.main()
    def ticket(self):
        global cost,a,b,c,d,aplace,astart
        #乘客浏览
        tim[0] = 0
        print(title)
        x = int(len(num))
        for i in range (x):
            print(tra[i], ' ', place[i], ' ', start[i], ' ', final[i], ' ', num[i])

        print()
        a = input('请输入要购买的车次:')
        b = float(input('请输入乘坐人数(成人计1,儿童计0.6):'))
        c = input('请输入座型(无座，一等，二等):')
        d = int(input('单程票输入1;往返票输入2:'))
        
        aplace = n[a]
        astart = m[a]
        num[int(tra.index(a))][c][0] -= 1

        p = num[int(tra.index(a))][c][1]
        cost = int(p * b * d)
        self.pay1()
    def pay1(self):
        print('-' * 33)
        print(f"请支付<{cost}>元！")
        pym = input("输入金额：")
        if pym == str(cost):
            print()
            print('您已购', a, '次列车', aplace, astart, '开', '请', b, '尽快换取纸质车票')
            print('-' * 33)
            self.getmenu()
        else:
            print("金额有误，支付失败")
            self.pay1()
        
    def rebk(self):
        global cost1,a1,b1,c1,d1
        #乘客浏览
        tim[0] = 1
        print(title)
        x = int(len(num))
        for i in range (x):
            print(tra[i], ' ', place[i], ' ', start[i], ' ', final[i], ' ', num[i])

        a1 = input('请输入改签的车次:')
        b1 = float(input('请输入改签后乘坐人数(成人计1,儿童计0.6):'))
        c1 = input('请输入改签座型(无座，一等，二等):')
        d1 = int(input('改签后，单程票输入1;往返票输入2:'))
                
        num[int(tra.index(a1))][c1][0] -= 1
        num[int(tra.index(a))][c][0] += 1

        p1 = num[int(tra.index(a1))][c1][1]
        cost1 = int(p1 * b1 * d1)
        dcost = abs(cost1 - cost)
        def rebp2():
            print('-' * 33)
            if cost1 <= cost:
                print(f"已退回<{dcost}>元！")
                print('-' * 33)
            else:
                print(f"仍需支付<{dcost}>元！")
                pym = input("输入金额：")
                if pym == str(dcost):
                    print()
                    print('您已成功改签', a, '次列车', aplace, astart, '开', '请', b, '尽快换取纸质车票')
                    print('-' * 33)
                else:
                    print("金额有误，支付失败")
                    rebp2()
        rebp2()
        self.getmenu()
    def rett(self):
        tim[0] = 2
        if tim[0] == 0:
            num[int(tra.index(a))][c][0] += 1
        if tim[0] == 1:
            num[int(tra.index(a1))][c][0] += 1
        print()
        print("已成功退票")
        print('-' * 33)
        self.getmenu()
print("-----欢迎进入网上火车售票系统-----")
tts = Tts()
tts.main()
