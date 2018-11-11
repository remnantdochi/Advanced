def binsearch(A,low,high,key):
    global check
    if low>high :
        check=-1
        return -1
    else:
        middle=(low+high)//2
        if key==A[middle]:
            if check==3: check=-1
            return middle
        elif key<A[middle]:
            if check == 3: check=0
            elif check == 1:check=0
            elif check == 0: check=-1
            print('test1',check,key)
            return binsearch(A,low,middle-1,key)
        else :
            if check==3: check=1
            elif check==0: check=1
            elif check==1: check=-1
            print('test2',check,key)
            return binsearch(A,middle+1,high,key)
T=int(input())
for test_case in range(1,T+1):
    N,M=map(int,input().split())
    Alist=list(map(int,input().split()))
    Blist=list(map(int,input().split()))
    totalcnt=0
    for bitem in Blist:
        check=3
        binsearch(Alist,0,N-1,bitem)
        print('test3',check,bitem)
        if check!=-1 :
            totalcnt+=1
    print("#{} {}".format(test_case,totalcnt))
