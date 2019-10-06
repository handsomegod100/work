import wx, string
import time, datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="程式交易模擬器",size=(400,500))
        self.Center() 

        panel = wx.Panel(parent=self)
        
        hbox0 = wx.BoxSizer(wx.HORIZONTAL)
        ask = wx.StaticText(panel,label='初始金額：')
        hbox0.Add(ask, 0, wx.ALIGN_CENTER_HORIZONTAL)
        self.money = wx.TextCtrl(panel, size = (100,22))
        unit = wx.StaticText(panel,label='  元 ')
        hbox0.AddStretchSpacer(1)
        hbox0.Add(self.money, 1,flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)
        hbox0.Add(unit, 0, wx.ALIGN_LEFT, 50)
        

        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        statictext = wx.StaticText(panel,label='選擇技術指標：')
        list1=['MACD',"KD線", "5日均線"]
        self.ti = wx.ComboBox(panel,-1,value='技術指標',choices=list1,style=wx.CB_SORT)
        hbox1.Add(statictext , 1 ,flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)
        hbox1.Add(self.ti , 1 ,flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)
        # self.Bind(wx.EVT_COMBOBOX,self.BtnClick,self.ti)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        statictext = wx.StaticText(panel,label='選擇股票：')
        self.list2 = wx.TextCtrl(panel, size = (100,22))
        hbox2.Add(statictext,1,flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)
        hbox2.AddStretchSpacer(1)
        hbox2.Add(self.list2, 1,flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)
  
        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        statictext = wx.StaticText(panel,label='選擇策略：')
        list3 = ['做多','放空']
        self.strategy = wx.ComboBox(panel,-1, value = "策略",choices=list3, style=wx.CB_SORT)
        hbox3.Add(statictext,1,flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)
        hbox3.Add(self.strategy,1,flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)     
        # self.Bind(wx.EVT_COMBOBOX,self.BtnClick,self.strategy)
        
       
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox0,1,flag=wx.ALL|wx.EXPAND,border=9)
        vbox.Add(hbox1,1,flag=wx.ALL|wx.EXPAND,border=5)
        vbox.Add(hbox2,1,flag=wx.ALL|wx.EXPAND,border=5)
        vbox.Add(hbox3,1,flag=wx.ALL|wx.EXPAND,border=5)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        ask = wx.StaticText(panel,label='買進張數：')
        hbox4.Add(ask, 0, wx.ALIGN_CENTER_HORIZONTAL)
        self.buy = wx.TextCtrl(panel, size = (100,22))
        unit = wx.StaticText(panel,label='  張 ')
        hbox4.AddStretchSpacer(1)
        hbox4.Add(self.buy, 1,flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)
        hbox4.Add(unit, 0, wx.ALIGN_LEFT, 50)
        vbox.Add(hbox4,1,flag=wx.ALL|wx.EXPAND,border=9)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        ask = wx.StaticText(panel,label='賣出張數：')
        hbox5.Add(ask, 0, wx.ALIGN_CENTER_HORIZONTAL)
        self.sell = wx.TextCtrl(panel, size = (100,22))
        unit = wx.StaticText(panel,label='  張 ')
        hbox5.AddStretchSpacer(1)
        hbox5.Add(self.sell, 1,flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)
        hbox5.Add(unit, 0, wx.ALIGN_LEFT, 50)
        vbox.Add(hbox5,1,flag=wx.ALL|wx.EXPAND,border=9)

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        btn = wx.Button(panel, label = "開始交易")
        hbox6.AddStretchSpacer(1)
        hbox6.Add(btn, 0, wx.ALIGN_LEFT, 20)
        vbox.Add(hbox6,1,flag=wx.ALL|wx.EXPAND,border=5)
        
        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        self.result = wx.StaticText(panel)
        hbox7.Add(self.result, 0, wx.ALIGN_CENTER_HORIZONTAL)
        vbox.Add(hbox7,1,flag=wx.ALL|wx.EXPAND,border=5)

        hbox8 = wx.BoxSizer(wx.HORIZONTAL)
        self.result1 = wx.StaticText(panel)
        hbox8.Add(self.result1, 0, wx.ALIGN_CENTER_HORIZONTAL)
        vbox.Add(hbox8,1,flag=wx.ALL|wx.EXPAND,border=5)

        # hbox9 = wx.BoxSizer(wx.HORIZONTAL)
        # self.result2 = wx.StaticBItmap(panel)
        # hbox9.Add(self.result2, 0, wx.ALIGN_CENTER_HORIZONTAL)
        # vbox.Add(hbox9,1,flag=wx.ALL|wx.EXPAND,border=5)
        
        self.Bind(wx.EVT_BUTTON,self.BtnClick,btn)

        panel.SetSizer(vbox)
       
       

    
    def BtnClick(self,event):
        
        mn = float(self.money.GetValue()) #初始金額
        stock = self.list2.GetValue() #股票代碼
        sell = float(self.sell.GetValue()) #賣量
        buy = float(self.buy.GetValue()) #買量
        technical = self.ti.GetStringSelection() #技術指標
        strategy = self.strategy.GetStringSelection() #操作策略
        
        

        #爬資料
        startTime = datetime.datetime(2019, 5, 27, 1, 0, 0) #GMT+8
        endTime = datetime.datetime(2019, 5, 27, 5 , 30, 0)
        info = pd.DataFrame(columns = ["時間","成交價"])        
        while datetime.datetime.now() < startTime:
            time.sleep(1)
        print(datetime.datetime.now(),"程式開始執行")
        while endTime  > datetime.datetime.now() > startTime:
            r = requests.get("https://tw.stock.yahoo.com/q/ts?s={}".format(stock))
            r.encoding = 'utf-8'
            data = pd.read_html(r.text)
            new = pd.DataFrame({"時間":data[2].iloc[3,0],"成交價":data[2].iloc[3,3]},index=[1])
            info = info.append(new,ignore_index=True)
            print(datetime.datetime.now(),"新增一筆資料。")
            time.sleep(4)
        print(datetime.datetime.now(),"程式結束")
        print(info)
        '''
        r = requests.get("https://finance.yahoo.com/quote/{}.TWO/history?period1=1524672000&period2=1556208000&interval=1d&filter=history&frequency=1d".format(stock))
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'lxml')
        title = soup.find_all("h1")
        if str(title).find("TWO") == -1 :
            r = requests.get("https://finance.yahoo.com/quote/{}.TW/history?period1=1524672000&period2=1556208000&interval=1d&filter=history&frequency=1d".format(stock))
       
        soup = BeautifulSoup(r.content, 'lxml')
        table = soup.find_all('table')
        info = pd.read_html(str(table))[0]
        info = info.drop(index=100)
        '''
        info['五日移動平均']= 0.0 #資料第7行
        info["DI"]= 0.0 #8
        info["EMA12"]= 0.0 #9
        info["EMA26"]= 0.0 #10
        info["fEMA12"]= 0.0 #1
        info["fEMA26"]= 0.0 #12
        info["DIF"]= 0.0 #13
        info["MACD"]= 0.0 #14
        info["OSC"]= 0.0 #15
        info["high9"] = 0.0 #16
        info["low9"] = 0.0 #17
        info["RSV"] = 0.0 #18
        info["k"] = 0.0 #19
        info["d"] = 0.0 #20
        #info["dividend"] = 0.0 #21
        info = info.sort_index(ascending=False)
        info = info.reset_index(drop=True)
        '''
        for i in range(0,info.shape[0]):
            for j in range(1,7):
              if str(info.iloc[i,j]).find("Dividend") == -1  : 
                    info.iloc[i,j] = float(info.iloc[i,j])
              else:
                 break
        '''
        
        '''
        #股利
        dividend = []
        drop = []
        dropday = []
        for i in range(info.shape[0]):
            if type(info.iloc[i,1]) == str :
                dividend.append(float(info.iloc[i,1].replace("Dividend","")))
                if i > 1:
                    dropday.append(info.iloc[i-1,0])
                drop.append(i) 
        for i in drop :    
            info = info.drop(index = i)
        info = info.reset_index(drop=True)
        '''
        #計算五日移動平均
        for i in range(4,info.shape[0]): 
            info.iloc[i,7] = (info.iloc[i,4]+info.iloc[i-1,4]+info.iloc[i-2,4]+info.iloc[i-3,4]+info.iloc[i-4,4])/5
        #DI    
        for i in range(info.shape[0]): 
            info.iloc[i,8] = (info.iloc[i,2]+info.iloc[i,3]+info.iloc[i,4]*2)/4
        #首日EMA12    
        for i in range(12,info.shape[0]): 
            st = []
            for j in range(0,12):
                st.append(info.iloc[i-j,12])
            info.iloc[i,9] = np.mean(st)
        #首日EMA26    
        for i in range(26,info.shape[0]): 
            st = []
            for j in range(0,26):
                st.append(info.iloc[i-j,12])
            info.iloc[i,10] = np.mean(st)
        #EMA12    
        for i in range(13,info.shape[0]): 
            info.iloc[i,11] = (info.iloc[i-1,9] * 11 + info.iloc[i,8]*2)/13
        #EMA26    
        for i in range(27,info.shape[0]): 
            info.iloc[i,12] = (info.iloc[i-1,10] * 25 + info.iloc[i,8]*2)/27
        #DIF  
        for i in range(27,info.shape[0]): 
            info.iloc[i,13] = (info.iloc[i,11]-info.iloc[i,12])
        #首日MACD    
        st=[] 
        for i in range(0,9):
            st.append(info.iloc[27+i,13])
        info.iloc[35,14] = np.mean(st)
        #MACD
        for i in range(36,info.shape[0]):
            info.iloc[i,14] = (info.iloc[i-1,14] *8 + info.iloc[i,13] * 2)/10
        #OSC
        for i in range(36,info.shape[0]):
            info.iloc[i,15] = info.iloc[i,13] - info.iloc[i,14]
        #9日高價
        for i in range(8,info.shape[0]):
            info.iloc[i,16] = max(info.iloc[range(i-8,i),4])
        #9日低價
        for i in range(8,info.shape[0]):
            info.iloc[i,17] = min(info.iloc[range(i-8,i),4])
        #RSV
        for i in range(8,info.shape[0]):
            info.iloc[i,18] = (info.iloc[i,4]-info.loc[i,"low9"])/(info.loc[i,"high9"]-info.loc[i,"low9"]) * 100
        #首日K值
        info.iloc[8,19] = 50
        #K值
        for i in range(9,info.shape[0]):
            info.iloc[i,19] = (2/3)*info.iloc[i-1,19] + (1/3)*info.iloc[i,18]
        #首日D值
        info.iloc[10,20] = np.mean(info.iloc[range(8,11),19])
        #D值
        for i in range(11,info.shape[0]):
            info.iloc[i,20] = (2/3)*info.iloc[i-1,20] + (1/3)*info.iloc[i,19]


        if technical == 'MACD':
            pf = 0
            initial = mn
            for i in range(35,info.shape[0]-1):
                if info.iloc[i,15] > 0 and info.iloc[i,15] > info.iloc[i-1,15] and mn >= buy * info.iloc[i+1,1]*1000*(1+0.1425/100): #若DIF和MACD黃金交叉(持有資金需大於0)
                    mn -= buy * info.iloc[i+1,1]*1000*(1+0.1425/100) #下一交易日買入
                    pf += buy 
                    #產生交易報表
                    info.loc[i+1,"買進張數"] = buy
                    info.loc[i+1,"持有張數"] = pf
                    info.loc[i+1,"持有現金"] = round(mn,2)
                if info.iloc[i,15] < 0 and info.iloc[i,15] < info.iloc[i-1,15] and pf >= sell: #若DIF和MACD死亡交叉(持有股票張數需大於0)
                    mn += sell * info.iloc[i+1,1]*1000*(1-0.4425/100) #下一交易日賣出     
                    #產生交易報表
                    info.loc[i+1,"賣出張數"] = sell
                    pf -= sell 
                    info.loc[i+1,"持有張數"] = pf
                    info.loc[i+1,"持有現金"] = mn
                else:
                    info.loc[i+1,"持有張數"] = pf
                    info.loc[i+1,"持有現金"] = round(mn,2)
            for i in range(36):
                info.loc[i,"持有現金"] = initial
            info = info.fillna(0)
            for i in range(info.shape[0]):
                info.loc[i,"損益"] = round((info.loc[i,"持有現金"]+info.iloc[i,4]*1000*info.loc[i,"持有張數"]*0.995575)-initial)
            dividends = []
            if len(dividend) > 0:
                for i in range(len(dividend)):
                    dividends.append(dividend[i] * 1000 * (info[info["Date"]==dropday[i]]).iloc[0,24])

        elif technical == 'KD線':
            pf = 0
            initial = mn
            for i in range(11,info.shape[0]-1):
                if info.iloc[i,20] < 20 and info.iloc[i,19] > info.iloc[i,20] and info.iloc[i-1,19] < info.iloc[i-1,20] and mn >= buy * info.iloc[i+1,1]*1000*(1+0.1425/100): #若KD值低於20且黃金交叉(持有資金需大於0)
                    mn -= buy * info.iloc[i+1,1]*1000*(1+0.1425/100) #下一交易日買入
                    pf += buy 
                    #產生交易報表
                    info.loc[i+1,"買進張數"] = buy
                    info.loc[i+1,"持有張數"] = pf
                    info.loc[i+1,"持有現金"] = round(mn,2)
        
                if info.iloc[i,19] < info.iloc[i,20] and info.iloc[i-1,19] > info.iloc[i-1,20] and pf >= sell: #若KD值高於80且死亡交叉(持有股票張數需大於0)
                    mn += sell * info.iloc[i+1,1]*1000*(1-0.4425/100) #下一交易日賣出     
                    #產生交易報表
                    info.loc[i+1,"賣出張數"] = sell
                    pf -= sell 
                    info.loc[i+1,"持有張數"] = pf
                    info.loc[i+1,"持有現金"] = mn
                else:
                    info.loc[i+1,"持有張數"] = pf
                    info.loc[i+1,"持有現金"] = round(mn,2)
            for i in range(12):
                info.loc[i,"持有現金"] = initial
            info = info.fillna(0)
            for i in range(info.shape[0]):
                info.loc[i,"損益"] = info.loc[i,"損益"] = round((info.loc[i,"持有現金"]+info.iloc[i,4]*1000*info.loc[i,"持有張數"]*0.995575)-initial)
            dividends = []
            if len(dividend) > 0:
                for i in range(len(dividend)):
                    dividends.append(dividend[i] * 1000 * (info[info["Date"]==dropday[i]]).iloc[0,24])

        elif technical == '5日均線':
            pf = 0 #持有股票張數，初始為0
            initial = mn
            for i in range(4,info.shape[0]-1):
                if info.iloc[i,4] > info.iloc[i,7]*1.02 and info.iloc[i,4] > info.iloc[i-1,4] and mn >= buy * info.iloc[i+1,1]*1000*(1+0.1425/100): #若股價上漲且高於五日平均1.02倍(持有資金足夠)
                    mn -= buy * info.iloc[i+1,1]*1000*(1+0.1425/100) #下一交易日買入
                    pf += buy 
                    #產生交易報表
                    info.loc[i+1,"買進張數"] = buy
                    info.loc[i+1,"持有張數"] = pf
                    info.loc[i+1,"持有現金"] = round(mn,2)
                
                if info.iloc[i,4] < info.iloc[i,7]*0.98 and info.iloc[i,4] < info.iloc[i-1,4] and pf >= sell: #若股價下跌且低於五日平均0.98倍(持有股票張數足夠)
                    mn += sell * info.iloc[i+1,1]*1000*(1-0.4425/100) #下一交易日賣出     
                    #產生交易報表
                    info.loc[i+1,"賣出張數"] = sell
                    pf -= sell 
                    info.loc[i+1,"持有張數"] = pf
                    info.loc[i+1,"持有現金"] = mn
                else:
                    info.loc[i+1,"持有張數"] = pf
                    info.loc[i+1,"持有現金"] = round(mn,2)
            for i in range(5):
                info.loc[i,"持有現金"] = initial
            info = info.fillna(0)
            for i in range(info.shape[0]):
                info.loc[i,"損益"] = round((info.loc[i,"持有現金"]+info.iloc[i,4]*1000*info.loc[i,"持有張數"]*0.995575)-initial)
            dividends = []
            if len(dividend) > 0:
                for i in range(len(dividend)):
                    dividends.append(dividend[i] * 1000 * (info[info["Date"]==dropday[i]]).iloc[0,24])

        new_data = info.loc[:,["Date","Open","Close*","買進張數","賣出張數","持有張數","持有現金","損益"]]
        new_data.reset_index(drop=True)
        print(new_data)

        result = u'使用技術指標：' + technical + '\n進行：' + strategy + '操作' 
        self.result.SetLabel(result)
        
        result1 = u'初始金額' + self.money.GetValue() + u'元　買進張數：' + self.buy.GetValue() + '張　' + u'賣出張數：' + self.sell.GetValue() + '張　' + '\n' + u"現金股利 {} 元, 總損益 {} 元, 報酬率 {} %".format(sum(dividends)*1000,new_data.iloc[-1,-1]+sum(dividends)*1000,(new_data.iloc[-1,-1] + sum(dividends) *1000)/initial*100)
        self.result1.SetLabel(result1)


        


class App(wx.App):
    def OnInit(self):
        frame=MyFrame()
        frame.Show()
        return True
    def OnExit(self):
        print("結束交易")
        return 0

if __name__=='__main__':
    app=App()
    app.MainLoop()
