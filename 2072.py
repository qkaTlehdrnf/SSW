TC=int(input())
for t in range(1,TC+1):
    numbers_=input()
    numbers_=numbers_.split()
    numbers_=map(int,numbers_)
    total=0
    for i in numbers_:
        if i%2==1:
            total+=i
    print('#{} {}'.format(t,total))