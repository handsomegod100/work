import random
cardlist = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K",
"A",2,3,4,5,6,7,8,9,10,"J","Q","K",
"A",2,3,4,5,6,7,8,9,10,"J","Q","K",
"A",2,3,4,5,6,7,8,9,10,"J","Q","K",]
carddict = {2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"J":10,"Q":10,"K":10}
class player :
    def __init__(self):
        self.card = []
        self.point = []
        self.score = 0
    def pick(self):
        a = random.choice(cardlist)
        self.card.append(a)
        print("您拿到的牌是{},您現在有{}。".format(a,self.card))
        self.count()
    def count(self):
        self.point = []
        p = 0
        c = 0
        for i in self.card :
            if i != "A":
                pp = carddict[i]
                p += pp
            else :
                c += 1
        if c == 1:
            self.point.append(p+1)
            self.point.append(p+11)
        elif c == 2:
            self.point.append(p+2)
            self.point.append(p+12)
        elif c == 3:
            self.point.append(p+3)
            self.point.append(p+13)
        elif c == 4:
            self.point.append(p+4)
            self.point.append(p+14)
        else :
            self.point.append(p)
        if max(self.point) <= 21:
            self.score = max(self.point)
        else :
            self.score = min(self.point)
class computer(player):
    def __init__(self):
        super(computer,self).__init__()
    def pick(self):
        a = random.choice(cardlist)
        self.card.append(a)
        print("莊家拿到的牌是{}，莊家現在有{}。".format(a,self.card))
        self.count()
def start():
    human = player()
    com = computer()
    print("歡迎來到Python21點！")
    com.pick()
    human.pick()
    while True :
        if human.score < 21 :
            ans = input("是否繼續拿牌？(Y/N)")
            if ans == "Y":
                human.pick()
                pass
            elif ans == "N":
                print("莊家補牌。")
                break
            else :
                print("請輸入正確回答。")
        elif human.score == 21 :
            print("您已達21點，莊家補牌。")
            break
        elif human.score > 21 :
            print("您已爆點，遊戲結束。")
            break
    while human.score <= 21 :
        if com.score >= human.score and com.score <= 21:
            print("莊家牌組為{}、總點數為{}，玩家牌組為{}、總點數為{}，莊家贏了。".format(com.card,com.score,human.card,human.score))
            break
        elif com.score > 21:
            print("莊家點數為{}，爆點，你贏了！".format(com.score))
            break
        else :
            com.pick()
start()
