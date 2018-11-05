T=int(input())
for test_case in range(1,T+1):
    N,M=map(int,input().split())
    items=list(map(int,input().split()))
    trucks=list(map(int,input().split()))
    items.sort()
    trucks.sort(reverse=True)
    #print(items)
    #print(trucks)
    weight=0
    for truck in trucks:
        if items == []: break
        itembig=items.pop()
        while itembig > truck:
            if items == []: break
            itembig=items.pop()
        #print('test',items)
        if itembig <= truck : weight+=itembig
        #print('test',itembig,truck)
    print("#{} {}".format(test_case,weight))
