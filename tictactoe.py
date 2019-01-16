'''
writing a tic tac toe program to be played by two players.
Author: SAI KISHORE AKULA
UNIVERSITY OF CINCINNATI

'''
import os
global p
p = { "1": ' ' , "2" : ' ', "3" : ' ',"4" : ' ', "5" : ' ',"6" : ' ',"7" : ' ',"8" : ' ',"9": ' '}

# clears the window.
def clear_board():
    if os.name == 'nt': 
        _ = os.system('cls')



#displays new boarded with selected values
def print_game_board():
    line_1 = "   "+p["1"]+"   "+"|"+"   "+p["2"]+"   "+"|"+"   "+p["3"]+"   "
    line_2 = "   "+p["4"]+"   "+"|"+"   "+p["5"]+"   "+"|"+"   "+p["6"]+"   "
    line_3 = "   "+p["7"]+"   "+"|"+"   "+p["8"]+"   "+"|"+"   "+p["9"]+"   "
    print('\n')
    print('\n')
    print('\n')
    print(line_1)
    print("       |       |       ")
    print("___________________________")
    print(line_2)
    print("       |       |       ")
    print("____________________________")
    print(line_3)
    print("       |       |       ")




#This function is used to check the status of game
def check_game_status(a,b):
    if p["1"]+p["2"]+p["3"] == a+a+a or p["4"]+p["5"]+p["6"] == a+a+a or  p["7"]+p["8"]+p["9"] == a+a+a or  p["1"]+p["4"]+p["7"] == a+a+a or  p["2"]+p["5"]+p["8"] == a+a+a or  p["3"]+p["6"]+p["9"] == a+a+a or  p["1"]+p["5"]+p["9"] == a+a+a or  p["3"]+p["5"]+p["7"] == a+a+a:
        return True
    elif p["1"]+p["2"]+p["3"] == b+b+b or p["4"]+p["5"]+p["6"] == b+b+b or  p["7"]+p["8"]+p["9"] == b+b+b or  p["1"]+p["4"]+p["7"] == b+b+b or  p["2"]+p["5"]+p["8"] == b+b+b or  p["3"]+p["6"]+p["9"] == b+b+b or  p["1"]+p["5"]+p["9"] == b+b+b or  p["3"]+p["5"]+p["7"] == b+b+b:
        return True    



#This function allocates X or O values to the board
def play_game(a,b):
    draw = 1 
    for i in range(1,10):
        if i%2 != 0:
            i = input("Player 1 Choose a number:  ")
            p[i] = a
            print('\n')
            print('\n')
            clear_board()
            print_game_board()
            print('\n')
            print('\n')
            check = check_game_status(a,b)
            if check == True:
                draw = 0
                print ("Player 1 Wins")
                break;
        else:
            i = input("Player 2 Choose a number:  ")
            p[i] = b
            print('\n')
            print('\n')
            clear_board()
            print_game_board()
            print('\n')
            print('\n')
            check = check_game_status(a,b)
            if check == True:
                draw = 0
                print ("Player 2 Wins")
                break;
    if draw == 1:
        print("---------Game Drawn---------------")
    re = input("Wanna play another game Y/N: ")

    if re.upper() == "Y":
        return re.upper()




#This function is to select players and their respective values (X,O)
def player_selection(a,b):
    player1 = a
    player2 = b
    print('\n')
    print("-------Player 1 : {} and Player 2: {}-----------".format(a,b))
    print ("       BEGIN THE GAME        ")
    print("     Player 1 goes first   ")
    print('\n')
    print_game_board()
    print('\n')
    print('\n')
    return play_game(a,b)



#this function, we enter details of the players. 
def enter_details():
    choosen = input("Player 1 please select X or O:  ")
    while True:
        if choosen.upper() == "X":
            return player_selection(choosen.upper(),'O')
            break;
        elif choosen.upper() == "O":
            return player_selection(choosen.upper(),'X')
            break;
        else:
            print("Please select either X or O")
            enter_details()




def main():
    while True:
        print("Welcome to TIC TAC TOE game")    
        print("---------------------------")
        print("---------------------------")
        print()
        re = enter_details()
        global p
        p = { "1": ' ' , "2" : ' ', "3" : ' ',"4" : ' ', "5" : ' ',"6" : ' ',"7" : ' ',"8" : ' ',"9": ' '}
        if re != 'Y':
            break

if  __name__ == '__main__':
    main()        



        

