# coding: utf-8
def change():
    while True:
        ans = input("請輸入單位(公斤/台斤):")
        n = int(input("請輸入數量:"))
        if ans ==  "台斤" and isinstance(n,int) == True :
            print("{}台斤為{}公斤。".format(n,n*0.6))
        elif ans == "公斤"and isinstance(n,int) == True:
            print("{}公斤為{}台斤。".format(n,n/0.6))
        else:
            print("請輸入正確單位及數量")
change()
