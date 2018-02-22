import os
def screen_draw(board):             #tictac screen view

    print('-------')
    print('|'+board[0]+'|'+board[1]+'|'+board[2]+'|')
    print('|'+board[3]+'|'+board[4]+'|'+board[5]+'|')
    print('|'+board[6]+'|'+board[7]+'|'+board[8]+'|')
    print('-------')


def init():                 # for init screen
    board={}
    for i in range(0,9):
        board[i]=' '
    screen_draw(board)
def compare_success_player(success,board,who):      #compare player tic tac
        for li in success:
            if board[li[0]]==who and board[li[1]]==who and board[li[2]]==who:
                return True

        return False

def move_valid(move):           # for validation
    #print('v')
    if move<1 or move>9:
        print('move within 1-9')
        return False
    return True

success=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];          #tic tac game success list
def game_start():
        board={}
        player1_name=input('Select Your Choice X or $ ::');
        player2_name='';
        if player1_name!='X' and player1_name!='$':
            print('please select one of them only')
            player1_name=input('Select Your Choice X or $ ::');


        if 'X'==player1_name:
            player2_name='$'
        else:
            player1_name='X'

        player_move=True
        player1_move_count=0
        player2_move_count=0
        for i in range(0,9):
            board[i]=' '
        for i in range(0,9):

            if player_move:                                                     #for player 1
                move=int(input('Player 1 Enter Your Move (1-9)::'))
                while move_valid(move)!=True:
                    move=int(input('Player 1 Enter Your Move (1-9)::'))

                while board[move-1]=='X' or board[move-1]=='$':                 #for old move
                    print("move already enterd")
                    move=int(input('Player 1 Enter Your Move (1-9)::'))

                board[move-1]=player1_name
                player1_move_count+=1;
                os.system('clear')
                screen_draw(board)
                player_move=False
                if player1_move_count>=3:
                    if True==compare_success_player(success,board,player1_name):
                        print('Player 1 Win The Match')
                        return


            else:                                                               #for player 2
                move=int(input('Player 2 Enter Your Move (1-9)::'))
                while move_valid(move)!=True:
                    move=int(input('Player 2 Enter Your Move (1-9)::'))

                while board[move-1]=='X' or board[move-1]=='$':
                    print("move already enterd")
                    move=int(input('Player 2 Enter Your Move (1-9)::'))

                board[move-1]=player2_name
                player2_move_count+=1;
                os.system('clear')
                screen_draw(board)
                player_move=True
                if player2_move_count>=3:
                    if True==compare_success_player(success,board,player2_name):
                            print('Player 2 Win The Match')
                            return
        print('Match Draw')




init()  #draw grid
game_start() #start game
