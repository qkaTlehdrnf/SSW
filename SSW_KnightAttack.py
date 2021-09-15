movable_L=[[1,2],[2,1],[-2,-1],[-1,-2],[-1,2],[2,-1],[1,-2],[-2,1]]
def make_board(board_size):
    return [[0]*board_size[1] for _ in range(board_size[0])]

def search_possibilities(board_size,y,x):
    leny=board_size[0]
    lenx=board_size[1]
    movable1=[]
    for i in movable_L:
        movable1.append(list([y,x][j]+i[j] for j in range(2)))
    movable2=[]
    for i in movable1:
        if 0<=i[0]<leny and 0<=i[1]<lenx:
            movable2.append(i)
    return movable2
'''
def loop(num,loop_list,inf_board,inf_reset,board_size,possibilities):
    if len(loop_list)==board_size[0]*board_size[1]:
        if sum(map(sum,inf_board))==0:#다 0인 경우도 포함하니까 총 경우 중 하나를 빼야한다.
            possibilities+=1
            num+=1
            return loop(num,loop_list,inf_board,inf_reset,board_size,possibilities)

    binary=bin(num)[2:]
    if inf_reset==0:
        board=make_board(board_size)
        for y in range(board_size[0]):
            for x in range(board_size[1]):
                try:
                    board[y][x]=binary[2*x+y]
                except IndexError:
                    board[y][x]=0
    return board
print(loop('10110',[],[2,3],0))'''
'''
def detect_loop(board,status_board,inf_board,board_L):#board: 말이 놓이면 1, status_board: 조건을 만족하면 1, inf_board: 주변의 놓이 말의 갯수(자신포함)
    global possibilities
    y_len=len(board)-1
    x_len=len(board[0])-1
    if y<y_len:
        y+=1
    elif x<x_len:
        y=0
        x+=1
    else:
        return
    cur_inf_board=inf_board


    print(board,'===',status_board,'===',cur_inf_board,'===',total_board,y,x)
    for yt in range(len(board)):
        for xt in range(x):
            if cur_inf_board[yt][xt]==-1:
                continue
            if total_board[yt][xt]==cur_inf_board[yt][xt]:
                if status_board[yt][xt]==1:
                    cur_inf_board[yt][xt]=-1
                else:
                    return
    for line in status_board:
        if 0 in line:
            suc=0
    if suc==1:
        print('success',board,'===',status_board,'===',cur_inf_board,'===',inf_board,'===',total_board,y,x)
        possibilities+=1

    changes=search_possibilities(board,y,x)
    detect_loop(board,status_board,cur_inf_board,y,x)#board에 아무것도 놓지 않았을 때
    changes.append([y,x])
    for change in changes:
        cur_inf_board[change[0]][change[1]]+=1
        if status_board[change[0]][change[1]]==1:
            status_board[change[0]][change[1]]=0

        else:
            status_board[change[0]][change[1]]=1
    detect_loop(board,status_board,cur_inf_board,y,x)'''
def make_tot_board(board_size):
    total_board=make_board(board_size)
    for y in range(board_size[0]):
        for x in range(board_size[1]):
            total_board[y][x] = len(search_possibilities(board_size, y, x))+1
    return total_board

def make_inf_board(board,board_size):
    inf_board=make_board(board_size)
    for y in range(board_size[0]):
        for x in range(board_size[1]):
            if board[y][x]==1:
                inf_board[y][x]+=1
            movable=search_possibilities(board_size,y,x)
            for pos in movable:
                if board[pos[0]][pos[1]]==1:
                    inf_board[y][x]+=1
    return inf_board

def valid_board_check(inf_board):
    global total_board
    if inf_board==total_board:
        return True
    else:
        return False

def loop(board_L,board_size):
    global possibilities
    global inf_board
    board=board_L(len(board_L)-1)#가장 최근의 board를 불러온다
    y=len(board)-1
    x=y if y==-1 else len(board[y])#해당 보드의 최근의 위치를 불러온다.
    for ty in board_size[0]:
        for tx in board_size[1]:
            if inf_board[ty][tx]==-1:
                continue





Tot=1
board_size=[2,3]
global total_board
global inf_board
global possibilities
for i in range(1,Tot+1):
    possibilities=0
    board=make_board(board_size)
    status_board=make_board(board_size)
    inf_board=make_board(board_size)
    total_board=make_tot_board(board_size)
    #detect_loop(board,status_board,inf_board,-1,0)
    print('#{} {}'.format(i,possibilities))