def merge(left,right):
    global cnt
    if left[len(left)-1] > right[len(right)-1]:
        cnt+=1
    result=[]
    while len(left)>0 and len(right)>0:
        if left[0] <= right[0]: result.append(left.pop(0))
        else : result.append(right.pop(0))
    if len(left)>0: result.extend(left)
    if len(right)>0: result.extend(right)
    return result
def merge_sort(m):
    if len(m) <= 1: return m
    left=m[:len(m)//2]
    right=m[len(m)//2:]
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)
T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    todolist=list(map(int,input().split()))
    cnt=0
    result=merge_sort(todolist)
    print("#{} {} {}".format(test_case,result[N//2],cnt))
