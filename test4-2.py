def partition(A,l,r):
    p=A[l]
    i=l+1
    j=r
    while i<=j:
        while (i<=j and A[i]<=p) : i+=1
        while (i<=j and A[j]>=p) : j-=1
        if i<=j:
            A[i],A[j]=A[j],A[i]
    A[l],A[j]=A[j],A[l]
    return j
def quicksort(A,l,r):
    if l<r:
        s=partition(A,l,r)
        quicksort(A,l,s-1)
        quicksort(A,s+1,r)
T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    todolist=list(map(int,input().split()))
    quicksort(todolist,0,N-1)
    print("#{} {}".format(test_case,todolist[N//2]))
