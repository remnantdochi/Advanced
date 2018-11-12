class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
'''
def printlist(sourceList):
    printnode=sourceList
    if sourceList==None:
        print('printnode-None')
    else:
        while printnode.next != None:
            print('printnode',printnode.data,end=" ")
            printnode=printnode.next
        print('printnode',printnode.data)'''
def findtail(sourceList):
    tmpnode=sourceList
    while tmpnode.next != None:
        tmpnode=tmpnode.next
    return tmpnode.data
def merge(leftHalf, rightHalf):
    global cnt
    if findtail(leftHalf) > findtail(rightHalf):
        cnt+=1
    fake_head = Node(None,None)
    curr = fake_head
    while leftHalf and rightHalf:
        if leftHalf.data < rightHalf.data:
            curr.next = leftHalf
            leftHalf = leftHalf.next
        else:
            curr.next = rightHalf
            rightHalf = rightHalf.next
        curr = curr.next
    if leftHalf == None:
        curr.next = rightHalf
    elif rightHalf == None:
        curr.next = leftHalf
    return fake_head.next
def countlist(sourceList):
    count=1
    tmpnode=sourceList
    while tmpnode.next != None:
        tmpnode=tmpnode.next
        count+=1
    return count
def split(sourceList):
    if sourceList == None or sourceList.next == None:
        leftHalf = sourceList
        rightHalf = None
        return leftHalf, rightHalf
    else:
        numofdata=countlist(sourceList)
        count=0
        midPointer = sourceList
        while count != numofdata//2-1:
            midPointer=midPointer.next
            count += 1
    leftHalf = sourceList
    rightHalf = midPointer.next
    midPointer.next = None
    return leftHalf, rightHalf
def merge_sort(m):
    if m==None or m.next==None:
        return m
    left,right= split(m)
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)
def findmiddle(sourceList,N):
    tmpnode=sourceList
    length=0
    while length != N//2:
        tmpnode=tmpnode.next
        length+=1
    return tmpnode.data
T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    todolist=list(map(int,input().split()))
    for i in range(N):
        if i==0:
            Head=Node(todolist[0],None)
            tmpnode=Head
        else:
            tmpnode.next=Node(todolist[i],None)
            tmpnode=tmpnode.next
    cnt=0
    resultnode=merge_sort(Head)
    result=findmiddle(resultnode,N)
    print("#{} {} {}".format(test_case,result,cnt))
