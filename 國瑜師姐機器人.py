# coding: utf-8
import random
word = open('靜思語錄.txt', 'r')
r = word.readlines()
angry = ["孺子不可教也","爛泥扶不上牆","扶不起的阿斗","對牛鼓簧"]
refuse = "不"
class bot:
    def __init__ (self,name):
        self.name = name
        self.msg =  r
        self.angry = angry
    def conversation(self):
        print(">>" + self.name + "師姐為您開示。")
        print(">>" + random.choice(self.msg).strip())
        while True:
            msg = input(">>")
            if msg != "感恩SeaFood":
                if msg.find(refuse) == -1 :
                    print(">>" + random.choice(self.msg).strip())
                else:
                    print(">>" + random.choice(self.angry))
                    break
            else:
                print(">>施主平安。")
                break
fish = bot("國瑜")
fish.conversation()
