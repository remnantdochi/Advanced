import itertools
T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    fmap=[[] for _ in range(N)]
    for i in range(N):
        fmap[i]=list(map(int,input().split()))
    direction=list(itertools.permutations([i for i in range(1,N)]))
    dirnum=len(direction)
    cnt=[0]*dirnum
    for i in range(dirnum):
        point=0
        for j in range(N-1):
            nextp=direction[i][j]
            cnt[i]+=fmap[point][nextp]
            point=nextp
        cnt[i]+=fmap[point][0]
    res=min(cnt)
    form='#'+str(test_case)
    print(form,res)
