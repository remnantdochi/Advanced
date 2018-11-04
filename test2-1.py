def makedirection(N):
    R,D=(0,1),(1,0)
    mylist=[]
    for _ in range(N-1):
        mylist.append(R)
        mylist.append(D)
    direction=list(itertools.permutations(mylist))
    direction=list(set(direction))
    return direction
T=int(input())
for test_case in range(1,T+1):
    import itertools
    N=int(input())
    fmap=[[] for _ in range(N)]
    for i in range(N):
        fmap[i]=list(map(int,input().split()))
    direction=makedirection(N)
    dirnum=len(direction)
    cnt=[0]*dirnum
    for i in range(dirnum):
        point=[0,0]
        for j in range(2*(N-1)):
            cnt[i]+=fmap[point[0]][point[1]]
            point[0]+=direction[i][j][0]
            point[1]+=direction[i][j][1]
        cnt[i]+=fmap[N-1][N-1]
    res=min(cnt)
    form='#'+str(test_case)
    print(form,res)
