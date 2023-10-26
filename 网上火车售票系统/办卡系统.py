import os,time
os.chdir("D:\\UserDefined_Install\\Python3.10.7\\AAAAAAPythondaima@\\网上火车售票系统")
class User:
    def __init__(self, name, id_card, tel):
        self.cardname = name
        self.id_card = id_card
        self.tel = tel

    def __str__(self):
        return self.cardname
class Card:
    def __init__(self, user):
        self.card_no = str(int(time.time() * 10 ** 6))
        self.balance = .0
        self.user = user
        self.password = self.user.id_card[-1:-7:-1][::-1]
    def __str__(self):
        return f'卡号：{self.card_no}\n用户：'\
               f'{self.user}\n余额：{"{:.2f}".format(self.balance)}'
class ATM:
    users = []
    cards = []
    def __init__(self):
        self.card = None

    def menu(self):
        print('1.开卡\n2.办理个人业务\n3.退出系统')
        key = input('请选择：')
        ret = self.set_input(key, 'main')
        return ret

    def get_menu(self):
        print('1.存款\n2.取款\n3.转账\n4.余额查询\n5.取卡')
        key = input('请选择：')
        ret = self.set_input(key, 'sub')
        return ret

    def create_card(self):
        user = self.create_user()
        card = Card(user)
        self.cards.append(card)
        print(f'开卡成功，欢迎使用酒城银行！\n你的卡号是：{card.card_no}\n默认密码为身份证后六位')

    @staticmethod
    def set_input(key, flag):
        if flag == 'main':
            return int(key) if key in ['1', '2', '3'] else None
        if flag == 'sub':
            return int(key) if key in ['1', '2', '3', '4', '5'] else None

    def create_user(self):
        username, id_card, tel = self.get_user_info()
        user = User(username, id_card, tel)
        self.users.append(user)
        return user

    @staticmethod
    def get_user_info():
        username = input('请输入你的姓名：')
        id_card = input('请输入身份证号码：')
        tel = input('请输入你的手机号：')
        return username, id_card, tel

    def id_card(self):
        card_no = input('请输入你的卡号：')
        password = input('请输入密码：')
        for card in self.cards:
            if card.card_no == card_no and card.password == password:
                self.card = card
                return True
            return False

    def deposit(self):
        money = input('请输入存款金额：')
        self.card.balance += float(money)
        print('存款成功')

    def withdrawal(self):
        money = float(input('请输入取款金额'))
        if money <= self.card.balance:
            self.card.balance -= money
            print('取款成功！')
        else:
            print('余额不足！')

    def transfer(self):
        other_card = input('请输入对方账号：')
        for card in self.cards:
            if card.card_no == other_card:
                money = float(input('请输入转账金额：'))
                if self.card.balance >= money:
                    self.card.balance -= money
                    card.balance +=money
                    print('转账成功！')
                else:
                    print('余额不足！')
                    break
        else:
            print('对方账号不存在！')

    def balance(self):
        print(self.card)

    def update_password(self):
        pass

    def select_method(self):
        while True:
            kw = self.get_menu()
            if kw is None:
                print('输入错误！请重新选择')
                break
            if kw == 5:
                self.card = None
                print('请拿走你的卡片！')
                break
            methods = {1: self.deposit, 2: self.withdrawal, 3: self.transfer, 4: self.balance}
            methods[kw]()

    def main(self):
        while True:
            key = self.menu()
            if key == 1:
                self.create_card()
            elif key == 2:
                is_inserted = self.id_card()
                if is_inserted:
                    self.select_method()
                else:
                    print('密码错误！')
            elif key == 3:
                break
            else:
                print('输入错误！')

atm = ATM()
atm.main()
