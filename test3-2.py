T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    wantlist=[[]]*N
    for i in range(N):
        wantlist[i]=list(map(int,input().split()))
    wantlist.sort()
    startlist=[[wantlist[i][0],wantlist[i][1],i] for i in range(N)]
    #print(startlist)
    endlist=[[startlist[i][1],startlist[i][0],startlist[i][2]] for i in range(N)]
    endlist.sort()
    #print(endlist)
    cnt=0
    #finish=[]
    while endlist!=[]:
        done=endlist.pop(0)
        cnt+=1
        #print('done',done)
        if endlist ==[] :break
        i=0
        while i != range(len(endlist)):
            #print('endlist',i,endlist[i])
            if endlist[i][1] < done[0]:
                #print('endlist2',endlist[i])
                endlist=endlist[:i]+endlist[i+1:]
                #print('endlist3',endlist)
            else: i+=1
            if i > len(endlist)-1 : break

    print("#{} {}".format(test_case,cnt))
