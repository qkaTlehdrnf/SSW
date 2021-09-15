T=int(input())
answer=[]
global ignorable
global temp_list
global cycle_remover_L
global temp_cycle_list
def sun_tracker(a,k_,total_):
    if a in temp_list:
        return total_
    if a in ignorable and k_!=0:
        k_-=1
        temp_cycle_list.append(a)
        if len(temp_list)+len(temp_cycle_list)==k+2:
            del(temp_list[0])
        total_+=a*len(temp_list)
        return sun_tracker(sun[a], k_, total_)
    if k_==0:
        return total_
    temp_list.append(a)
    ignorable.append(a)
    total_+=a*len(temp_list)
    return sun_tracker(sun[a],k_,total_)

def cycle_remover(a):
    if a in temp_list:
        cycle_start=temp_list.index(a)
        ignorable.extend(temp_list[cycle_start:])
        return sum(temp_list[cycle_start:])*min(len(temp_list[cycle_start:]),(k+1))
    elif a in cycle_remover_L:
        return 0
    cycle_remover_L.append(a)
    temp_list.append(a)

    return cycle_remover(sun[a])

for t in range(1,T+1):
    ignorable=[]
    cycle_remover_L=[]
    NK=input()
    NK=NK.split()
    N,k=int(NK[0]),int(NK[1])
    sun={}
    for i in range(N):
       sun[i+1]=int(input())
    total=0

    #cycle remove
    for i in range(1,N+1):
        if i in cycle_remover_L:
            continue
        temp_list=[]
        total+=cycle_remover(i)

    #main count
    for i in range(1,N+1):
        temp_cycle_list=[]
        temp_list=[]
        if i in ignorable:
            continue
        total+=sun_tracker(i,k,0)
    print('#{} '.format(t)+str(total))