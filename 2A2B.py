import random
ans_num=[]
ans_num.append(random.randint(1,9))
while len(ans_num)!=4:
    ran=random.randint(0,9)
    if  ran not in ans_num:
        ans_num.append(ran)  
    else:
        continue  
#make a random list for answer
count=0
mes="{}A{}B"
while True:
    num_A=0
    num_B=0
    error=False
    cin=input("輸入一個1000~9999的數字,各位數字不重複")
    cin_num=list(cin)
    if len(cin_num)==4:
        if cin_num[0]=="0":
            error=True
            print("第一個數不為0")
        for y in range(1,4):
            if str(cin_num[y]) in cin[:y]:
                print("各位數字不重複")
                error=True
                break
    if len(cin_num)==4 and error ==False:
        for x in range(0,4):
            if int(cin_num[x])==ans_num[x]:
                num_A+=1
            if int(cin_num[x]) in ans_num:
                num_B+=1
        num_B=num_B-num_A 
        print(mes.format(num_A,num_B))
        count=count+1

    if num_A==4:
        print("恭喜答對，答案是"+cin+"，共猜了"+str(count)+"次！")
        break       
    if len(cin_num) != 4:
        print("四位數！！")
        continue
    
