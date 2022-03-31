ans_num=[]
cin_num=[]


while True:
    a=input("輸入一個四位數字")
    if len(a)==4:
        cin_num=list(a)

        break
    else:
        print("四位數！！")
print(cin_num)