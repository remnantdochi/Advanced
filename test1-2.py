T=int(input())
for test_case in range(1,T+1):
    num=float(input())
    bina=[]
    cnt=0
    while num!=0:
        temp=num*2
        cnt+=1
        if cnt ==13: break
        if temp>=1:
            bina.append(1)
            num=temp-1
        else:
            bina.append(0)
            num=temp
    form='#'+str(test_case)
    if cnt==13:
        print(form,"overflow")
    else:
        print(form,end=" ")
        for i in range(cnt-1):
            print(bina[i],end="")
        print(bina[cnt-1])
