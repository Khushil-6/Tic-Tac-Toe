

# This Function Show's the 3x3 board
def show():
    print(board[6], '|', board[7], '|', board[8])
    print('----------')
    print(board[3], '|', board[4], '|', board[5])
    print('----------')
    print(board[0], '|', board[1], '|', board[2])


# The function checks the winning conditions
def checkline(chr,spot1, spot2, spot3):
    if board[spot1] == chr and board[spot2] == chr and board[spot3] == chr:
        return True


# The functions checks each line on the board with the help of checkline function
def checkall(chr):
    if checkline(chr, 0, 1, 2):
        return True
    if checkline(chr, 3, 4, 5):
        return True
    if checkline(chr, 6, 7, 8):
        return True
    if checkline(chr, 0, 3, 6):
        return True
    if checkline(chr, 1, 4, 7):
        return True
    if checkline(chr, 2, 5, 8):
        return True
    if checkline(chr, 2, 4, 6):
        return True
    if checkline(chr, 0, 4, 8):
        return True


# The function Checks if there is any available place on the board to place X or O
def isboardfull():
    check = 0

    for space in board:
        if space != ' ':
            check += 1
        else:
            pass
    if check == 9:
        return True


# The function Prints the Overview of the game
def overview():
    print('Overview :')
    print('\t'"There Would be Two Player's.\n\tPlayer_1 = X and Player_2 = O""\n")
    print("--> Use Number pad to position your choice [1,9]"'\n')
    print('\t\t', 7, '|', 8, '|', 9)
    print('\t\t''----------')
    print('\t\t', 4, '|', 5, '|', 6)
    print('\t\t''----------')
    print('\t\t', 1, '|', 2, '|', 3, '\n')
    print(
        "------------------------------------------------------------------------------------------------------------"'\n')


# The Program starts

board = [" "," "," "," "," "," "," "," "," "," "]
print("\n \t!!! Welcome To The Tic Tc Toe !!!""\n")
print('Overview :')
print('\t'"There Would be Two Player's.\n\tPlayer_1 = X and Player_2 = O""\n")
print("--> Use Number pad to position your choice [1,9]"'\n')
print('\t\t',7,'|',8,'|',9)
print('\t\t''----------')
print('\t\t',4,'|',5,'|',6)
print('\t\t''----------')
print('\t\t',1,'|',2,'|',3)
inst = input('\n'"Do you want to see Overview while you play [Y/N] :").lower()

like_to_play = 0
print_x_o = 0
while True:
    if like_to_play == 0:
        board = [' ']*10

        user = input('\n'"Are you ready to play ? [Y/N] : ").lower()
        if user != 'y' and user != 'n':
            print("I did not understand that !!!""\n")
            continue
        if user == 'n':
            print("Get Lost :[ ")
            exit()
        if user == 'y':
            print('\n'*200)
            like_to_play = 1
    else:
        enter = input("Choose a Spot on the board:"'\n')
        try:
            enter = int(enter)
        except Exception:
            print("Please choose only numbers."'\n')
            continue
        if enter not in range(1,10):
            print("Wrong Number is Chosen"'\n')
            continue
        if board[enter-1] != 'X' and board[enter-1] != 'O':
            if print_x_o % 2 == 0:
                symbol = 'X'
                print_x_o += 1
            else:
                symbol = 'O'
                print_x_o += 1
            board[enter-1] = symbol

            if checkall(symbol):
                print("\n"*100)
                show()
                print("\n""{} wins, Thanks for playing !!!".format(symbol))
                play_again = input("\n""Would you like to play again. Press y or n : "'\n')
                if play_again == 'y':
                    print("\n"*100)
                    print_x_o += 1
                    like_to_play = 0
                    continue

                else:
                    if play_again == 'n':
                        print("\n""Thanks for playing :[")
                        exit()
                break
            if isboardfull():
                print("\n"*100)
                show()
                play_again = input("\n""The Game is a Draw.\nWould you like to play again. Press y or n : "'\n')
                if play_again == 'y':
                    print("\n" * 100)
                    print_x_o += 1
                    like_to_play = 0
                    continue
                elif play_again == 'n':
                    print("Thanks for playing.")
                    exit()
                else:
                    print("Wrong symbol. I don't want you to play again with me. Bye"'\n')
                    exit()
            print('\n' * 200)
        else:
            print("The spot is taken")
            continue
    if inst == 'y':
        overview()
    else:
        pass
    show()
