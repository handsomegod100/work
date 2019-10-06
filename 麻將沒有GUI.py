import random
card_dict={101:"一餅", 102:"二餅",103:"三餅", 104:"四餅", 105:"五餅", 106:"六餅", 107:"七餅", 108:"八餅", 109:"九餅", #建立「餅」的字典
           201:"一萬", 202:"二萬", 203:"三萬", 204:"四萬", 205:"五萬", 206:"六萬", 207:"七萬", 208:"八萬", 209:"九萬",  #建立「萬」的字典
           301:"一條", 302:"二條", 303:"三條", 304:"四條", 305:"五條", 306:"六條", 307:"七條", 308:"八條", 309:"九條",  #建立「條」的字典
           401:"北", 501:"南", 601:"東", 701:"西", 801:"中", 901:"發", 1001:"白", 
           1101:"春", 1201:"夏", 1301:"秋", 1401:"冬", 1501:"梅", 1601:"蘭", 1701:"菊", 1801:"竹"}   #建立「四喜牌」、「三元牌」、「花牌」的字典
card_dict_reverse = {value:key for key,value in card_dict.items()} #麻將所有的牌
flow=[ "春", "夏", "秋", "冬", "梅", "蘭", "菊", "竹"] 
card_list=["一餅", "二餅", "三餅", "四餅", "五餅", "六餅", "七餅", "八餅", "九餅", #所有的牌的串列
            "一餅", "二餅", "三餅", "四餅", "五餅", "六餅", "七餅", "八餅", "九餅",
            "一餅", "二餅", "三餅", "四餅", "五餅", "六餅", "七餅", "八餅", "九餅",
            "一餅", "二餅", "三餅", "四餅", "五餅", "六餅", "七餅", "八餅", "九餅",
            "一萬", "二萬", "三萬", "四萬", "五萬", "六萬", "七萬", "八萬", "九萬",
            "一萬", "二萬", "三萬", "四萬", "五萬", "六萬", "七萬", "八萬", "九萬",
            "一萬", "二萬", "三萬", "四萬", "五萬", "六萬", "七萬", "八萬", "九萬",
            "一萬", "二萬", "三萬", "四萬", "五萬", "六萬", "七萬", "八萬", "九萬",
            "一條", "二條", "三條", "四條", "五條", "六條", "七條", "八條", "九條",
            "一條", "二條", "三條", "四條", "五條", "六條", "七條", "八條", "九條",
            "一條", "二條", "三條", "四條", "五條", "六條", "七條", "八條", "九條",
            "一條", "二條", "三條", "四條", "五條", "六條", "七條", "八條", "九條",
            "北","南","東","西","北","南","東","西","北","南","東","西","北","南",
            "東","西","中","發","白","中","發","白","中","發","白","中","發","白",
            "春", "夏", "秋", "冬", "梅", "蘭", "菊", "竹"]
def turnfunc(turn):
    global player_list,rememberturn
    global player,com1,com2,com3
    if turn != rememberturn :
        turn = rememberturn + 1
    if turn == 1:
        player = MPlayer("玩家",1)
        com1 = Player("電腦1",2)
        com2 = Player("電腦2",3)
        com3 = Player("電腦3",4)
    elif turn == 2:
        player = MPlayer("玩家",4)
        com1 = Player("電腦1",1)
        com2 = Player("電腦2",2)
        com3 = Player("電腦3",3)
    elif turn == 3:
        player = MPlayer("玩家",3)
        com1 = Player("電腦1",4)
        com2 = Player("電腦2",1)
        com3 = Player("電腦3",2)
    elif turn == 4:
        player = MPlayer("玩家",2)
        com1 = Player("電腦1",3)
        com2 = Player("電腦2",4)
        com3 = Player("電腦3",1)
    player_round_dict = {player.round:player, com1.round : com1, com2.round : com2, com3.round : com3}
    player_list = []
    for i in range(1,5):
        player_list.append(player_round_dict.get(i))
def resetcardlist():
    global card_list
    card_list=["一餅", "二餅", "三餅", "四餅", "五餅", "六餅", "七餅", "八餅", "九餅", #所有的牌的串列
            "一餅", "二餅", "三餅", "四餅", "五餅", "六餅", "七餅", "八餅", "九餅",
            "一餅", "二餅", "三餅", "四餅", "五餅", "六餅", "七餅", "八餅", "九餅",
            "一餅", "二餅", "三餅", "四餅", "五餅", "六餅", "七餅", "八餅", "九餅",
            "一萬", "二萬", "三萬", "四萬", "五萬", "六萬", "七萬", "八萬", "九萬",
            "一萬", "二萬", "三萬", "四萬", "五萬", "六萬", "七萬", "八萬", "九萬",
            "一萬", "二萬", "三萬", "四萬", "五萬", "六萬", "七萬", "八萬", "九萬",
            "一萬", "二萬", "三萬", "四萬", "五萬", "六萬", "七萬", "八萬", "九萬",
            "一條", "二條", "三條", "四條", "五條", "六條", "七條", "八條", "九條",
            "一條", "二條", "三條", "四條", "五條", "六條", "七條", "八條", "九條",
            "一條", "二條", "三條", "四條", "五條", "六條", "七條", "八條", "九條",
            "一條", "二條", "三條", "四條", "五條", "六條", "七條", "八條", "九條",
            "北","南","東","西","北","南","東","西","北","南","東","西","北","南",
            "東","西","中","發","白","中","發","白","中","發","白","中","發","白",
            "春", "夏", "秋", "冬", "梅", "蘭", "菊", "竹"]
def score(ulist):
    tem = []    
    score = []
    for i in ulist:
        tem.append(i)
    for i in tem:
        if ulist.count(i) >= 2:
            for j in range(2):
                ulist.remove(i)
            score.append(scoref(ulist)+2)
            for j in range(2):
                ulist.append(i)
    ulist.clear()
    for i in tem :
        ulist.append(i)
    if len(score) == 0:
        return 0
    elif max(score) == 17 or scoref(ulist) == "win":
        return "win"
    else :
        score.append(scoref(ulist))
        return max(score)
def scoref(ulist) : #計分
    score1 = []
    score2 = []
    tem = [] #原始牌組的暫存串列
    ulist2 = [] #用來先吃後碰
    for i in ulist :
        tem.append(i)
        ulist2.append(i)
    key_list = [] #牌組的key值串列
    key_listt = [] #KEY值串列的迭代串列
    ktem = [] #算分時暫存key值的串列
    for i in tem: #原始牌組中的牌
        if isinstance(i,list)  != True: #若非串列
            if i in ulist: #確認此牌仍然位於牌組中 (因為tem的牌組為原始牌組，ulist的牌組會自碰自吃，這樣tem原本的牌可能不會出現在ulist中)
                if ulist.count(i) == 3: #如果牌組中有三張此牌
                    ulist.remove(i) #把這張牌從牌組中移除
                    peng(ulist,i) #自碰 (剩下兩張一樣的牌被移除，加入上一行被移除的牌後，組成串列後加入ulsit)
    for i in ulist: #自碰完後的牌組中的牌
        if isinstance(i,list)  != True: #若非串列
            k = card_dict_reverse.get(i) #轉換成KEY值
            key_list.append(k) #加入牌組的key值串列
    for i in key_list:
        key_listt.append(i)
    for i in key_listt:   
        if card_dict.get(i+1) in ulist and card_dict.get(i-1) in ulist: #牌的上下兩張連號若在牌組裡
            if i in key_list:
                v = card_dict.get(i)
                ulist.remove(v) #牌組移除這張牌         
                key_list.remove(i)
                key_list.remove(i+1)
                key_list.remove(i-1)
                eat(ulist,v) #自吃 (兩張連號會被移除，加入上一行被移除的牌後，加入ulist)
        elif card_dict.get(i+1) in ulist and card_dict.get(i+2) in ulist:
            if i in key_list:
                v = card_dict.get(i)
                ulist.remove(v)
                key_list.remove(i)
                key_list.remove(i+1)
                key_list.remove(i+2)
                eat(ulist,v)        
        elif card_dict.get(i-1) in ulist and card_dict.get(i-2) in ulist:
            if i in key_list:
                v = card_dict.get(i)
                ulist.remove(v)
                key_list.remove(i)
                key_list.remove(i-2)
                key_list.remove(i-1)
                eat(ulist,v)
    for i in ulist: # 組好牌後計算分數，一組組好的牌3分
        if isinstance(i,list)  == True:
            for j in i :
                score1.append(3) 
    key_list.clear()  #清空key_list 重新取得組好牌後剩餘所有單張的牌的key值
    for i in ulist:
        if isinstance(i,list)  != True:
            k = card_dict_reverse.get(i)
            key_list.append(k)
    for k in key_list :
        if key_list.count(k) == 2: # 剩餘的牌有兩張一樣
            if [k,k].sort() in ktem : #若暫存key值的串列已有這兩張牌
                continue #跳過此輪不加分
            else : #若沒有
                ktem.append([k,k].sort()) #將兩張牌加入暫存key值串列
                score1.append(2) #加分
        elif k+1 in key_list: #連號1.5分
            if [k,k+1].sort() in ktem :
                continue
            else :
                ktem.append([k,k+1].sort())
                score1.append(1.5)
        elif k-1 in key_list: 
            if [k,k-1].sort() in ktem:
                continue
            else:
                ktem.append([k,k-1].sort())
                score1.append(1.5)
        elif k-2 in key_list:#中洞1分
            if [k,k-2].sort() in ktem:    
                continue
            else:
                ktem.append([k,k-2].sort())
                score1.append(1)
        elif k+2 in key_list:
            if [k,k+2].sort() in ktem:    
                continue
            else:
                ktem.append([k,k+2].sort())
                score1.append(1)
    key_list.clear()
    key_listt.clear() #清空key值 計算先吃後碰的分數
    for i in ulist2:
        if isinstance(i,list)  != True:
            k = card_dict_reverse.get(i)
            key_list.append(k)
    for i in key_list:
        key_listt.append(i)
    for i in key_listt: #自吃
        if card_dict.get(i+1) in ulist2 and card_dict.get(i-1) in ulist2:
            if i in key_list:
                key_list.remove(i)
                key_list.remove(i+1)
                key_list.remove(i-1)
                v = card_dict.get(i)
                ulist2.remove(v) #牌組移除這張牌
                eat(ulist2,v) #自吃 (兩張連號會被移除，加入上一行被移除的牌後，加入ulist)

        elif card_dict.get(i+1) in ulist2 and card_dict.get(i+2) in ulist2:
            if i in key_list:
                key_list.remove(i)
                key_list.remove(i+1)
                key_list.remove(i+2)
                v = card_dict.get(i)
                ulist2.remove(v)
                eat(ulist2,v) 
        elif card_dict.get(i-1) in ulist2 and card_dict.get(i-2) in ulist2:
            if i in key_list:
                key_list.remove(i)
                key_list.remove(i-2)
                key_list.remove(i-1)
                v = card_dict.get(i)
                ulist2.remove(v)
                eat(ulist2,v) 
    for i in tem:
        if isinstance(i,list)  != True: #自碰
            if i in ulist2:
                if ulist2.count(i) == 3:
                    ulist2.remove(i)
                    peng(ulist2,i) 
    key_list.clear()
    for i in ulist2:
        if isinstance(i,list)  != True:
            k = card_dict_reverse.get(i)
            key_list.append(k)
    for i in ulist2:
        if isinstance(i,list)  == True:
            for j in i :
                score2.append(3)
    ktem.clear()
    for k in key_list :
        if key_list.count(k) == 2: #眼睛2分
            if [k,k].sort() in ktem :
                continue
            else : 
                ktem.append([k,k].sort())
                score2.append(2)
        elif k+1 in key_list: #連號1.5分
            if [k,k+1].sort() in ktem :
                continue
            else :
                ktem.append([k,k+1].sort())
                score2.append(1.5)
        elif k-1 in key_list: 
            if [k,k-1].sort() in ktem:
                continue
            else:
                ktem.append([k,k-1].sort())
                score2.append(1.5)
        elif k-2 in key_list:#中洞1分
            if [k,k-2].sort() in ktem:    
                continue
            else:
                ktem.append([k,k-2].sort())
                score2.append(1)
        elif k+2 in key_list:
            if [k,k+2].sort() in ktem:    
                continue
            else:
                ktem.append([k,k+2].sort())
                score2.append(1)  
    ulist.clear()
    for i in tem:
        ulist.append(i)
    if sum(score1) == 17 or sum(score2) == 17 : 
        score1.sort()
        score2.sort()
        if score1 == [2,3,3,3,3,3] or score2 == [2,3,3,3,3,3]:
            return "win"
        elif score1 == [2,2,2,2,2,2,2,3] or score2 == [2,2,2,2,2,2,2,3] :
            return "win"
    else:
        if sum(score1) >= sum(score2):
            return sum(score1)
        else:
            return sum(score2)
def sortpy(ulist): #排序
    key_list = [] #牌組的key值串列
    list_sorted = [] #整理好的牌
    show=[] #牌組中已組好的牌暫存的串列
    for i in ulist: #牌組中
        if isinstance(i,list) == True: #若是串列
            for j in i :
                show.append(j) #一組一組放入暫存串列中
        else :
            k = card_dict_reverse.get(i) #剩餘的牌轉換成key值
            key_list.append(k) #加入key值串列
    key_list.sort() #利用key值排序
    for i in key_list:
        v = card_dict.get(i)
        list_sorted.append(v) #再轉回value  一個一個加入整理好的串列
    if len(show) != 0:
        list_sorted.append(show)#整理好的串列再加暫存組好的牌的串列
    ulist.clear() #清空原本的串列
    for i in list_sorted:
        ulist.append(i) #整理好的牌重新加入原本的串列
    return ulist
def peng(ulist,target): #碰 target = 要碰的牌
    show = [] #暫存牌組中已經組好的牌的串列
    set1 = [] #碰的組合
    for i in ulist : #先將組好的牌放進暫存串列
        if isinstance(i,list) == True:
            for j in i :
                show.append(j)
    if show in ulist:
        ulist.remove(show) #刪除組好的牌
    if target in ulist: #如果要碰的牌存在此牌組
        if ulist.count(target)==2: #且張數為2
            ulist.remove(target) #牌組刪除這張牌兩次
            ulist.remove(target)
            set1.append(target) #碰的組合加入這張牌三次
            set1.append(target)
            set1.append(target)
            show.append(set1) #已組好的牌加入這組碰的組合
            ulist.append(show) #重新加入組好的牌
            return ulist
        else:
            if len(show) != 0 :
                ulist.append(show)
            return ulist
    else :
        if len(show) != 0 :
            ulist.append(show)
        return ulist
def eat(ulist,target,way = 0):#吃  target = 要吃的牌 way = 怎麼吃
    key_list=[] #牌組的key值串列
    set1 = [] #吃的組合(key)
    set1v = [] #吃的組合(value)
    show = [] #暫存已組好的牌
    for i in ulist : #已組好的牌加入暫存串列
        if isinstance(i,list) == True:
            for j in i :
                show.append(j)
    if show in ulist:
        ulist.remove(show) #刪除組好的牌
    for i in ulist: #剩下的牌換成key值
        k = card_dict_reverse.get(i)
        key_list.append(k) #加入key值串列
    target = card_dict_reverse.get(target) #要吃的牌也轉換成key值
    if target+1 in key_list and target-1 in key_list and (way == 0 or way ==1): #如果target的前後兩張連續牌的牌也在牌組中
        ulist.remove(card_dict.get(target+1)) #牌組移除這兩牌
        ulist.remove(card_dict.get(target-1))
        set1.append(target+1) #吃的組合加入這三張連續的牌(包括target)
        set1.append(target)
        set1.append(target-1)
        for i in set1 : #吃的組合轉換成value
            v = card_dict.get(i)
            set1v.append(v)
        show.append(set1v) #組好的牌加入轉換好的吃的組合       
        ulist.append(show) #牌組重新加入已組好的牌
        return ulist
    elif target+1 in key_list and target+2 in key_list and (way == 0 or way == 2):
        ulist.remove(card_dict.get(target+1))
        ulist.remove(card_dict.get(target+2))
        set1.append(target+1)
        set1.append(target)
        set1.append(target+2)
        for i in set1 :
            v = card_dict.get(i)
            set1v.append(v)
        show.append(set1v)         
        ulist.append(show)
        return ulist
    elif target-1 in key_list and target-2 in key_list and (way == 0 or way ==3):
        ulist.remove(card_dict.get(target-1))
        ulist.remove(card_dict.get(target-2))
        set1.append(target-2)
        set1.append(target)
        set1.append(target-1)
        for i in set1 :
            v = card_dict.get(i)
            set1v.append(v)
        show.append(set1v) 
        ulist.append(show)
        return ulist   
    else:
        if len(show) != 0 :
            ulist.append(show)
        return ulist
def gun(ulist,target): #槓
    show = [] #組好的牌的暫存串列
    set1 = [] #槓的組合
    for i in ulist : #組好的牌加入暫存串列
        if isinstance(i,list) == True:
            for j in i :
                show.append(j)
    if show in ulist:
        ulist.remove(show)#刪除組好的牌
    if target in ulist: #若要槓的牌存在牌組中
        if ulist.count(target)==3: #且張數為3
            ulist.remove(target) #牌組移除這張牌三次
            ulist.remove(target)
            ulist.remove(target)
            set1.append(target) #槓的組合加入這張牌四次
            set1.append(target)
            set1.append(target)
            set1.append(target)
            show.append(set1) #槓的組合加入組好的牌
            ulist.append(show) #組好的牌重新加入牌組
            return ulist
        else:
            if len(show) != 0:
                ulist.append(show)
            return ulist
    else :
        if len(show) != 0:
            ulist.append(show)
        return ulist
def printcard(ulist): #印出牌的函數(為了不把暗槓、手牌印出，但還是要保留牌組的值)
    show=[]
    printout=[]
    for i in ulist: #若是串列則要分析是否有暗槓
        if isinstance(i,list) == True: #組好的牌
            for j in i: #每組組好的牌
                set1 = [] #暫存串列 每換一組組好的牌歸零一次
                for k in j: #每個組好的牌中的每張牌
                    if k.find("*") != -1: #若每張牌字串中有暗槓標記
                        set1.append("暗槓") #把暗槓的牌放入暫存串列
                    else: #若沒有暗槓標記
                        set1.append(k)#把沒暗槓的牌放入暫存串列(為了讓一組的牌變成組成一組串列 ex.2萬,3萬,4萬變成[2萬,3萬,4萬])
                if len(set1) != 0:
                    show.append(set1) #暫存串列組好牌後放入show裡
        else: #不是串列的牌(手牌)
            printout.append("麻")
    if len(show) != 0 :
        printout.append(show) #將show加入要印出的牌           
    print(printout)           
def toll(ulist) : #丟牌 
    sortpy(ulist)
    tem = []
    origin = []
    score_list = []
    abanlist = []
    for i in ulist:
        tem.append(i)
        origin.append(i) #原始牌組丟入暫存串列 
    if eatcard != 0:
        while eatcard in ulist:
            ulist.remove(eatcard)
            tem.remove(eatcard)
        while au in ulist:
            ulist.remove(au)
            tem.remove(au)
        while ad in ulist :
            ulist.remove(ad)
            tem.remove(ad)
    for i in tem :
        if isinstance(i,list) != True:
            ulist.remove(i)
            s = score(ulist)
            score_list.append(s)
            ulist.append(i)
            sortpy(ulist)
    for i in range(len(score_list)):
        if score_list[i] == max(score_list):
            abanlist.append(ulist[i])
    ulist.clear()
    for i in origin:
        ulist.append(i)
    aban = random.sample(abanlist,1)[0]
    ulist.remove(aban)
    return aban 
def take(ulist): #拿牌
    card = random.sample(card_list,1) #抽一張牌
    card_list.remove(card[0]) #card_list中移除這張牌
    ulist.append(card[0]) #ulist中增加這張牌
def countpy(ulist) : #計算張數
    num = 0 #張數計數器
    for i in ulist :#ulist的元素
        if isinstance(i,list) != True:#若非串列
            num += 1 #計數器加一張
        else: #若為串列
            for j in i: #i裡的元素
                num += 3 #張數計數器
    return num
def ver(ulist,a):##創造出新串列優先計算胡了沒
    ver=[]
    for i in ulist:
        ver.append(i)
    ver.append(a)
    return ver
class Player:
    def __init__(self,name,r):
        self.name = name
        self.card = sortpy(random.sample(card_list,16))
        for i in self.card:
            card_list.remove(i)
        self.flow = []
        self.round = r
    def cardvalue(self):
        klist = []
        for i in self.card:
            if isinstance(i,list) != True:
                k = card_dict_reverse.get(i)
                klist.append(k)
        return klist
    def checkselfwin(self):
        if score(self.card) == "win":
            print(self.name+"自摸！你輸了！")
            print(self.name+":"+self.card)
            end = 1
    def mflow(self):
        while len([i for i in self.card if i in flow]) != 0 :
            for i in self.card:
                if i in flow :
                    self.card.remove(i)
                    self.flow.append(i)
                    print(self.name+"補花:"+i)
            if self.round == turn :
                while countpy(self.card) < 17:
                    take(self.card)
            else :
                while countpy(self.card) < 16:
                    take(self.card)
    def angun(self,target):
        show = [] #組好的牌的暫存串列
        set1 = [] #暗槓的組合
        for i in self.card : #組好的牌加入暫存串列
            if isinstance(i,list) == True:
                for j in i :
                    show.append(j)
        if show in self.card:
            self.card.remove(show)#刪除組好的牌
        if target in self.card: #若要暗槓的牌存在牌組中
            if self.card.count(target)==4: #且張數為4
                for i in range(4):
                    self.card.remove(target) #牌組移除這張牌四次
                for i in range(4):
                    set1.append(target + "*") #暗槓的組合加入這張牌四次，且標記*號
                show.append(set1) #暗槓的組合加入組好的牌
                self.card.append(show)#組好的牌重新加入牌組
                print(self.name+"暗槓")
                print(self.name+":",end="")
                printcard(self.card)
                take(self.card)
            else:
                if len(show) != 0 :
                    self.card.append(show)       
    def turn(self):
        global a
        if countpy(self.card) < 17:
            take(self.card)
            self.mflow()
            while self.card.count(self.card[-1]) == 4:
                self.angun(self.card[-1])
            a = toll(self.card)
        else :
            a = toll(self.card)
        sortpy(self.card)
        print(self.name+"打出:"+a)
    def checkwin(self,target):
        global stop
        global end
        if stop == 0:
            if score(ver(self.card,target)) == "win":
                print(self.name+"win")
                print(self.name+":",end = "")
                print(self.card) 
                end = 1
                stop+=1
                ###########重新開始
    def checkgun(self,target):
        global stop
        if stop == 0:
            if self.card.count(target) == 3:
                gun(self.card,target)
                stop = 1
                sortpy(self.card)
                print(self.name+"槓"+target)
                print(self.name+":",end="")
                printcard(self.card)
                turn = self.round
                ####換出牌序
    def checkpeng(self,target):
        global stop
        if stop == 0:
            if self.card.count(target) == 2:
                peng(self.card,target)
                stop = 1
                sortpy(self.card)
                print(self.name+"碰"+target)
                print(self.name+":",end="")
                printcard(self.card)
                turn = self.round
                ####換出牌序
    def checkeat(self,target):
        global stop,eatcard,au,ad
        global turn
        k = card_dict_reverse.get(target)
        if k-1 in self.cardvalue() and k+1 in self.cardvalue() and stop == 0:
            eat(self.card,target,1)
            sortpy(self.card)
            print(self.name+"吃"+target)
            print(self.name+":",end="")
            printcard(self.card)
            eatcard = target
            au = 0
            ad = 0
            stop = 1
            turn+=1
        if k-1 in self.cardvalue() and k-2 in self.cardvalue() and stop == 0 :
            eat(self.card,target,3)
            sortpy(self.card)
            print(self.name+"吃"+target)
            print(self.name+":",end="")
            printcard(self.card)
            eatcard = target
            k = card_dict_reverse.get(target)
            au = 0
            ad = card_dict.get(k-3)
            stop = 1
            turn+=1
        if k+1 in self.cardvalue() and k+2 in self.cardvalue() and stop == 0 :
            eat(self.card,target,2)
            sortpy(self.card)
            print(self.name+"吃"+target)
            print(self.name+":",end="")
            printcard(self.card)
            eatcard = target
            k = card_dict_reverse.get(target)
            au = card_dict.get(k+3)
            ad = 0
            stop = 1
            turn+=1
    
class MPlayer(Player):
    def __init__(self,name,r):
        super().__init__(name,r)
    def checkselfwin(self):
        if score(self.card) == "win":
            print(self.name+":",end="")
            print(self.card)
            answer = input("請輸入是否自摸:")
            if answer == "是":
                print(self.name+"自摸!!")
                print(self.name+":",end ="")
                print(self.card)              
    def mflow(self):
        while len([i for i in self.card if i in flow]) != 0 :
            for i in self.card:
                if i in flow :
                    self.card.remove(i)
                    self.flow.append(i)
                    print(self.name+"補花:"+i)
            if self.round == turn :
                print("輪到玩家，補牌後抽牌")
                while countpy(self.card) < 17:
                    take(self.card)
                    print(self.name+":",end="")
                    print(self.card)
            else :
                while countpy(self.card) < 16:
                    take(self.card)
                    print(self.name+":",end="")
                    print(self.card)

    def angun(self,target):
        show = [] #組好的牌的暫存串列
        set1 = [] #暗槓的組合
        for i in self.card : #組好的牌加入暫存串列
            if isinstance(i,list) == True:
                for j in i :
                    show.append(j)
        if show in self.card:
            self.card.remove(show)#刪除組好的牌
        if target in self.card: #若要暗槓的牌存在牌組中
            if self.card.count(target)==4: #且張數為4
                for i in range(4):
                    self.card.remove(target)#牌組移除這張牌四次
                for i in range(4):
                    set1.append(target) #暗槓的組合加入這張牌四次
                show.append(set1) #暗槓的組合加入組好的牌
                self.card.append(show)#組好的牌重新加入牌組
                print(self.name+"暗槓")
            else:
                if len(show) != 0 :
                    self.card.append(show)    
                print(self.card)
    def turn(self):
        global a,peatcard
        if countpy(self.card) <17:
            take(self.card)
            print(self.name+":",end="")
            print(self.card)
            self.checkselfwin()
            self.mflow()
            while self.card.count(self.card[-1]) == 4:
                print(self.name+":",end="")
                print(self.card)
                answer = input("請選擇是否暗槓")
                if answer == "是":
                    self.angun(self.card[-1])
                else :
                    break
        else :
            print(self.name+":",end="")
            print(self.card)
        while True :
            a = input("請選擇要丟棄的牌:")
            if peatcard != 0:
                if a == peatcard or a == eu or a == ed:
                    print("吃完牌後禁止吃入打出！")
                    continue
                else :
                    break
            else:
                break
        peatcard = 0
        self.card.remove(a)
        sortpy(self.card)
        print(self.name+"打出:"+a)
    def checkwin(self,target):
        global end
        global stop
        if stop == 0:
            if score(ver(self.card,target)) == "win":
                print(self.name+":",end="")
                print(self.card)
                answer = input("請輸入是否胡牌")
                if answer == "是":
                    print(self.name+"win")
                    print(self.name+":",end="")
                    print(self.card,end="")
                    print("聽"+":"+target)
                    end = 1
                    stop = 1 
                    ###########重新開始
    def checkgun(self,target):
        global turn
        global stop
        if stop == 0:
            if self.card.count(target) == 3:
                print(self.name+":",end="")
                print(self.card)
                answer = input("請輸入是否槓牌")
                if answer == "是":
                    gun(self.card,target)
                    print(self.name+"槓"+target)
                    print(self.name+":",end="")
                    print(self.card)
                    ####換出牌
                    stop = 1
                    turn = self.round

    def checkpeng(self,target):
        global turn
        global stop
        if stop == 0:
            if self.card.count(target) == 2:
                print(self.name+":",end="")
                print(self.card)
                answer = input("請輸入是否碰牌")
                if answer == "是":
                    peng(self.card,target)
                    print(self.name+"碰"+target)
                    ####換出牌序
                    stop = 1
                    turn = self.round

    def checkeat(self,target):
        global stop , eu ,ed
        global turn , peatcard
        if stop == 0:
            k = card_dict_reverse.get(target)
            while True:
                if k+1 in self.cardvalue() and k-1 in self.cardvalue():
                    print(self.name+":",end="")
                    print(self.card)
                    answer = input("您有{}、{}是否吃{}?".format(card_dict.get(k-1),card_dict.get(k+1),target))
                    if answer == "是":
                        eat(self.card,target,1)
                        print(self.name+"吃"+target)
                        peatcard = target
                        eu = 0
                        ed = 0
                        break    
                if k-1 in self.cardvalue() and k-2 in self.cardvalue():
                    print(self.name+":",end="")
                    print(self.card)
                    answer = input("您有{}、{}是否吃{}?".format(card_dict.get(k-2),card_dict.get(k-1),target))
                    if answer == "是":
                        eat(self.card,target,3)
                        print(self.name+"吃"+target)
                        peatcard = target
                        k = card_dict_reverse.get(target)
                        eu = 0
                        ed = card_dict.get(k-3)
                        break                 
                if k+1 in self.cardvalue() and k+2 in self.cardvalue():
                    print(self.name+":",end="")
                    print(self.card)
                    answer = input("您有{}、{}是否吃{}?".format(card_dict.get(k+1),card_dict.get(k+2),target))
                    if answer == "是":
                        eat(self.card,target,2)
                        print(self.name+"吃"+target)
                        peatcard = target
                        k = card_dict_reverse.get(target)
                        eu = card_dict.get(k+3)
                        ed = 0
                        break
                break
#開局
turn = 0
while True:
    if turn == 0:
        turn =1 
        rememberturn = 1  
    eatcard = 0
    peatcard = 0
    end = 0
    resetcardlist()
    turnfunc(turn)
    print(player.card)
    for i in player_list:
        i.mflow()
    while True:
        global stop
        while turn == 1 and end == 0:
            if len(card_list)== 8:
                print("流局!遊戲結束!")
                end = 1
                break
            player_list[0].turn()
            stop = 0
            for i in [player_list[1],player_list[2],player_list[3]]:
                i.checkwin(a)
            for i in [player_list[2],player_list[3]]:
                i.checkgun(a)
            for i in [player_list[1],player_list[2],player_list[3]]:
                i.checkpeng(a)
            player_list[1].checkeat(a)
            if stop == 0:
                turn += 1
        while turn == 2 and end == 0:
            if len(card_list)== 8:
                print("流局!遊戲結束!")
                end = 1
                break
            player_list[1].turn()
            stop = 0
            for i in [player_list[2],player_list[3],player_list[0]]:
                i.checkwin(a)
            for i in [player_list[3],player]:
                i.checkgun(a)
            for i in [player_list[2],player_list[3],player_list[0]]:
                i.checkpeng(a)
            player_list[2].checkeat(a)
            if stop == 0:
                turn += 1 
        while turn == 3 and end == 0 :
            if len(card_list)== 8:
                print("流局!遊戲結束!")
                end = 1
                break
            player_list[2].turn()
            stop = 0
            for i in [player_list[3],player_list[0],player_list[1]]:
                i.checkwin(a)
            for i in [player_list[0],player_list[1]]:
                i.checkgun(a)
            for i in [player_list[3],player_list[0],player_list[1]]:
                i.checkpeng(a)
            player_list[3].checkeat(a)
            if stop == 0:
                turn += 1
        while turn == 4 and end == 0:
            if len(card_list)== 8:
                print("流局!遊戲結束!")
                end = 1
                break
            player_list[3].turn()
            stop = 0
            for i in [player_list[0],player_list[1],player_list[2]]:
                i.checkwin(a)
            for i in [player_list[1],player_list[2]]:
                i.checkgun(a)
            for i in [player_list[0],player_list[1],player_list[2]]:
                i.checkpeng(a)
            player_list[0].checkeat(a)
            if stop == 0:
                turn -= 3
        if end == 1:
            break