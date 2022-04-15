import random
import time
ans_num=[]
while len(ans_num)!=4:
    ran=random.randint(1,9)
    if  ran not in ans_num:
        ans_num.append(ran)  
    else:
        continue  
#make a random list for answer
# print(ans_num)
mes="{}A{}B"
while True:
    num_A=0
    num_B=0
    cin=input("輸入一個1000~9999的數字，各位數字不重複")
    cin_num=list(cin)
    if len(cin_num)==4:
        for x in range(0,4):
            if int(cin_num[x])==ans_num[x]:
                num_A+=1
            if int(cin_num[x]) in ans_num:
                num_B+=1
        num_B=num_B-num_A 
    print(mes.format(num_A,num_B))

    if num_A==4:
        print("恭喜答對，答案是",cin)
        break       
    if len(cin_num) != 4:
        print("四位數！！")
        continue
    
