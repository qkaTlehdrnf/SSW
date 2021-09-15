lines='''1
4 8 5 7
.......#
..#....#
.###...#
.....###
R=lll
G=ub(B)
B=ub(m)lib(l)(m)
H=ib()(mmHllmll)
I=III
1 1 w
G
1 1 e
G
2 2 n
G
2 6 w
BR
4 1 s
ib(lib()(mmm))(mmmm)
1 1 e
H
2 2 s
I'''
direction={'w':(-1,0),'e':(1,0),'s':(0,1),'n':(0,-1)}
lines=lines.split('\n')

#'ub(m)lib(l)(m)ib' --> ['ub(m)', 'l', 'm', 'ib(l) (m)']
def procedures_spliter(program):
    print('spliter',program)
    long=len(program)
    sorted=[]
    bracket=0
    touchdown=0
    memory=0
    for i in range(long):
        cur=program[i]
        if cur=='(':
            bracket+=1
            continue
        elif cur==')':
            bracket-=1
            if bracket==0:
                touchdown-=1
                if touchdown==0:
                    end=i
                    if memory:
                        ifproc+=program[start: end + 1]
                        sorted.append(ifproc)
                        memory=0
                    else:
                        sorted.append(program[start:end+1])

                elif bracket==0:
                    end=i
                    ifproc=program[start: end + 1]+' '
                    start=i+1
            continue
        if bracket==0:
            if cur.isupper():
                former_program=program
                cur_program=procdures[cur]
                if former_program==cur_program:
                    raise RecursionError
                sorted.extend(procedures_spliter(procdures[cur]))
            elif cur=='m' or cur=='l':
                sorted.append(cur)

            elif cur == 'u':
                start=i
                touchdown=1
            elif cur=='i':
                start=i
                memory=1
                touchdown=2
    print('sorted',sorted)
    return sorted

#['ub(m)', 'l', 'm', 'ib(l)(m)']
def mechanism(splited_commands,x_,y_,z_):
    print('mechanism',splited_commands,x_,y_,z_)
    for proc in splited_commands:
        if proc=='m':#forward
            if not board[y_+direction[z_][1]][x_+direction[z_][0]]:
                x_,y_=x_+direction[z_][0],y_+direction[z_][1]
        elif proc=='l':
            if z_=='n':
                z_='w'
            elif z_=='w':
                z_='s'
            elif z_=='s':
                z_='e'
            elif z_=='e':
                z_='n'
            else:
                raise TypeError


        elif proc[0]=='u':
            condition_true=0
            condition_=proc[1]
            if condition_=='b':
                if board[y_ + direction[z_][1]][x_ + direction[z_][0]]:
                    condition_true=1
            elif condition_==z_:
                condition_true=1
            while not condition_true:
                print('inside while')
                if condition_=='b':
                    if board[y_ + direction[z_][1]][x_ + direction[z_][0]]:
                        condition_true=1
                        print('1')
                elif condition_==z_:
                    condition_true=1
                print('2')
                if condition_true:
                    break
                x__,y__,z__=x_,y_,z_
                x_,y_,z_=mechanism(procedures_spliter(proc[3:-1]),x_,y_,z_)
                if x_==x__ and y_==y__ and z_==z__ and not condition_true:
                    raise RecursionError


        elif proc[0]=='i':
            condition_true=0
            condition_=proc[1]
            programs_=proc.split()
            program1_,program2_=programs_[0][1:-1],programs_[1][1:-1]
            if condition_=='b':
                if board[y_ + direction[z_][1]][x_ + direction[z_][0]]:
                    condition_true=1
            elif condition_==z_:
                condition_true=1
            if condition_true:
                splited_program1_=procedures_spliter(program1_)
                x_,y_,z_=mechanism(splited_program1_,x_,y_,z_)
            else:
                splited_program2_=procedures_spliter(program2_)
                x_,y_,z_=mechanism(splited_program2_,x_,y_,z_)
            if x_==0:
                return 0,0,0
    return x_,y_,z_

line=0
T=int(lines[line])
#T = int(input())
for test_case in range(1, T + 1):
    line+=1
    NMde = lines[line]
    #NMde=input()
    N,M,d,e=map(int,NMde.split())
    board = [[]] * (N+2)
    board[0]=[1]*(M+2)
    board[-1]=[1]*(M+2)
    procdures = {}
    programs=[[]]*e
    # board
    for i in range(N):
        line+=1
        row=lines[line]
        # row=input()
        row = row.replace('.', '0')
        row = row.replace('#', '1')
        row=list(map(int,row))
        row=[1]+row+[1]
        board[i+1]=row
    # procedure
    for i in range(d):
        line+=1
        code=lines[line]
        # code=input()
        title = code[0]
        procedure = code[2:]
        procdures[title] = procedure

    for i in range(e):
        line+=1
        loc=lines[line]
        # loc=input()

        y, x, z = loc.split()
        x,y=int(x),int(y)
        line+=1
        program=lines[line]
        programs[i]=program
        # command=input()

        try:
            print('##########################start',x,y,z,program)
            splited_program=procedures_spliter(program)
            x,y,z=mechanism(splited_program,x,y,z)
            print(x,y,z)
        except RecursionError:
            print('inf')



