T=int(input())
for test_case in range(1,T+1):
    N,numbers=map(str,input().split())
    bina=int(numbers,16)
    bina=bin(bina)[2:]
    if len(bina) != 4*int(N):
        bina='0'*(4*int(N)-len(bina))+bina
    form='#'+str(test_case)
    print(form,bina)
