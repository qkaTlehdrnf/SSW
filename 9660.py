TC=int(input())
for t in range(1,TC+1):
    peoples_d={}
    N=int(input())
    temp_=[i for i in range(1,N+1)]
    for i in range(1,N+1):
        N[i]=temp_
    hate_num_l=map(int,input().split())
    for i in range(N+1):
        if hate_num_l[i] in peoples_d[i+1]:
            peoples_d[i+1].remove(hate_num_l[i])

