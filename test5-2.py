import itertools
T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    fmap=[[]]*N
    for i in range(N):
        fmap[i]=list(map(int,input().split()))
    mylist=[i for i in range(N)]
    result=list(itertools.permutations(mylist,N))
    best=0
    for i in range(N):
        best+=fmap[i][i]
    for i in range(len(result)):
        cnt=0
        for j in range(N):
            if cnt>=best: break
            cnt+=fmap[j][result[i][j]]
        if cnt<=best: best=cnt
    print("#{} {}".format(test_case,best))
