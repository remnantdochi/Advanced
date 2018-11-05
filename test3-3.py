T=int(input())
for test_case in range(1,T+1):
    cards=list(map(int,input().split()))
    p1cards=[0]*10
    p2cards=[0]*10
    def addcard(cardnum,pcards):
        pcards[cardnum]+=1
        return pcards
    def winner(pcards):
        for i in range(10):
            if pcards[i] >=3 : return 1
            if i>7: continue
            elif pcards[i] >= 1 and pcards[i+1] >=1 and pcards[i+2] >=1: return 1
        return 0
    res=0
    while cards != []:
        p1cards=addcard(cards.pop(0),p1cards)
        if winner(p1cards) :
            res=1
            break
        p2cards=addcard(cards.pop(0),p2cards)
        if winner(p2cards) and res !=1 :
            res=2
            break
    print("#{} {}".format(test_case,res))
