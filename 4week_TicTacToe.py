###################

# 프로그램명 : 틱택토
# 작성자 : 소프트웨어학부 / 이충희
# 작성일 : 2025-03-30
# 프로그램 설명 : 틱택토 게임 프로그램 

###################


import random

def draw(arr) :
   
    for i in range(0 ,3) :
        print(" " + arr[i][0] + " | " + arr[i][1] + " | " + arr[i][2])
        if(i != 2) :
            print("---|---|---")

def check(arr , a, b) :
    flag = False
    tag = arr[b][a]
    if(arr[b][0] == arr[b][1] == arr[b][2] == tag) : flag = True
    if(arr[0][a] == arr[1][a] == arr[2][a] == tag) : flag = True
    if(arr[0][0] == arr[1][1] == arr[2][2] == tag) : flag = True
    if(arr[2][0] == arr[1][1] == arr[0][2] == tag) : flag = True

    return flag

def Isvalid(board, a, b) :
    if( (a > 2 or a < 0 ) or (b > 2 or b < 0 )) :
        print("잘못된 좌표입니다")
        return False
        
    elif(board[b][a] != " ") :
        print("이미 놓여진 자리입니다")
        return False
    else :
        return True
   
def Is_draw(board) : 
    flag = True
    for i in range(0, 3) :
        for j in range(0, 3) :
            if board[i][j] == " " :
                flag = False

    return flag






board = [[" ", " ", " "],[ " ", " ", " "],[" ", " ", " "]]


draw(board)
while True :
    
    print("---User Turn---")
    a = int(input("x좌표 입력 : "))
    b = int(input("y좌표 입력 : "))
    if Isvalid(board, a, b) == False :
        continue
    else :
        board[b][a] = "O"
        draw(board)
        
        if(check(board, a, b)) : 
            print("User Win") 
            break
        elif(Is_draw(board)) :
            print("draw")
            break
    
    print("----Computer Turn----")
    
    while True :
        computer_x = random.randrange(0,3)
        computer_y = random.randrange(0,3)
        if(board[computer_y][computer_x] == " ") :
            break
    
    board[computer_y][computer_x] = "X"
    draw(board)
    if(check(board, computer_x, computer_y)) : 
        print("Computer Win") 
        break
    elif(Is_draw(board)) :
        print("draw")
        break
