def solution(A):
    global best
    global terminals
    global startgas
    global N
    cnt=0
    gas=startgas-1
    for i in range(2,N):
        if A[i-2]==1:
            gas+=terminals[i-2]
            cnt+=1
        if gas==0 and i != N: break
        if cnt >= best : break
        if gas+i>=N :
            best=cnt
            break
        gas-=1
def subset(A,k,n):
    if k==n: solution(A)
    else:
        A[k]=1
        subset(A,k+1,n)
        A[k]=0
        subset(A,k+1,n)
T=int(input())
for test_case in range(1,T+1):
    terminals=list(map(int,input().split()))
    N=terminals[0]
    startgas=terminals[1]
    terminals=terminals[2:]
    best=N-2
    subset([0]*(N-2),0,N-3)
    print("#{} {}".format(test_case,best))
