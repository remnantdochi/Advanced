class node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
def findindex(sourceList,index):
    i=0
    tmpnode=sourceList
    while i != index:
        tmpnode=tmpnode.next
        i+=1
    return tmpnode
def partition(A,l,r):
    p=findindex(A,l).data
    i=l+1
    j=r
    while i<=j:
        while (i<=j and findindex(A,i).data<=p) : i+=1
        while (i<=j and findindex(A,j).data>=p) : j-=1
        if i<=j:
            idata=findindex(A,i).data
            jdata=findindex(A,j).data
            findindex(A,i).data,findindex(A,j).data=jdata,idata
    ldata=findindex(A,l).data
    jdata=findindex(A,j).data
    findindex(A,l).data,findindex(A,j).data=jdata,ldata
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
    for i in range(N):
        if i==0:
            Head=node(todolist[0],None)
            tmpnode=Head
        else:
            tmpnode.next=node(todolist[i],None)
            tmpnode=tmpnode.next
    quicksort(Head,0,N-1)
    print("#{} {}".format(test_case,findindex(Head,N//2).data))
