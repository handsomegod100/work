# coding: utf-8
import random
def test():
    print("數學小測驗")
    score = 0
    for i in range(0,9):
        x = random.randint(1,999)
        y = random.randint(1,999)
        sign = ["+","-","*","/"]
        s = random.choice(sign)
        res = float(input("{}{}{}=?(小數點四捨五入至第二位):".format(x,s,y)))
        if s == "+":
            if res == x+y:
                print("答對了")
                score += 10
            else:
                print("答錯了")
        elif s == "-":
            if res == x-y:
                print("答對了")
                score += 10
            else:
                print("答錯了")
        elif s == "*":
            if res == x*y:
                print("答對了")
                score += 10
            else:
                print("答錯了")
        elif s == "/":
            if res == round(x/y,2):
                print("答對了")
                score += 10
            else:
                print("答錯了")
    print("測驗結束，你的分數是{}分".format(score))
test()
