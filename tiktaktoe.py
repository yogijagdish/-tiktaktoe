# creating the space 
game = { 1:" ", 2:" ", 3: " ", 4:" ", 5:" ", 6:" ",7:" ",8:" ",9:" "}

# creating the board
def creating_board():
    print(game.get(7),"|",game.get(8),"|",game.get(9))
    print("---------")
    print(game.get(4),"|",game.get(5),"|",game.get(6))
    print("---------")
    print(game.get(1),"|",game.get(2),"|",game.get(3))


gamer1 = input("\n enter the name of player1: ")
gamer2 = input("\n enter the name of player2: ")

#selection of player
player1 = "*"
player2 = "0"
turn = player1

creating_board()

def check():
    if game.get(1)=='*' and game.get(5)=='*' and game.get(9)=='*':
        print("game over!!!")
        print(gamer1,"wins")
        exit()
    elif game.get(7)=='*' and game.get(5)=='*' and game.get(3)=='*':
        print("game over!!!")
        print(gamer1,"wins")
        exit()
    elif game.get(1)=='*' and game.get(2)=='*' and game.get(3)=='*':
        print("game over!!!")
        print(gamer1,"wins")
        exit()
    elif game.get(4)=='*' and game.get(5)=='*' and game.get(6)=='*':
        print("game over!!!")
        print(gamer1,"wins")
        exit()
    elif game.get(7)=='*' and game.get(8)=='*' and game.get(9)=='*':
        print("game over!!!")
        print(gamer1,"wins")
        exit()
    elif game.get(1)=='*' and game.get(4)=='*' and game.get(7)=='*':
        print("game over!!!")
        print(gamer1,"wins")
        exit()
    elif game.get(2)=='*' and game.get(5)=='*' and game.get(8)=='*':
        print("game over!!!")
        print(gamer1,"wins")
        exit()
    elif game.get(3)=='*' and game.get(6)=='*' and game.get(9)=='*':
        print("game over!!!")
        print(gamer1,"wins")
        exit()
    elif game.get(1)=='*' and game.get(5)=='*' and game.get(9)=='*':
        print("game over!!!")
        print(gamer1,"wins")
        exit()
    elif game.get(7)=='0' and game.get(5)=='0' and game.get(3)=='0':
        print("game over!!!")
        print(gamer2,"wins")
        exit()
    elif game.get(1)=='0' and game.get(2)=='0' and game.get(3)=='0':
        print("game over!!!")
        print(gamer2,"wins")
        exit()
    elif game.get(4)=='0' and game.get(5)=='0' and game.get(6)=='0':
        print("game over!!!")
        print(gamer2,"wins")
        exit()
    elif game.get(7)=='0' and game.get(8)=='0' and game.get(9)=='0':
        print("game over!!!")
        print(gamer2,"wins")
        exit()
    elif game.get(1)=='0' and game.get(4)=='0' and game.get(7)=='0':
        print("game over!!!")
        print(gamer2,"wins")
        exit()
    elif game.get(2)=='0' and game.get(5)=='0' and game.get(8)=='0':
        print("game over!!!")
        print(gamer2,"wins")
        exit()
    elif game.get(3)=='0' and game.get(6)=='0' and game.get(9)=='0':
        print("game over!!!")
        print(gamer2,"wins")
        exit()

def playing():
    #playing game
    def play():
        if game.get(position) != " ":
            print("position is already used!!!")
        else:
            if position == 7:
                game.update({7:turn})
            elif position == 8:
                game.update({8:turn})
            elif position == 9:
                game.update({9:turn})
            elif position == 4:
                game.update({4:turn})
            elif position == 5:
                game.update({5:turn})
            elif position == 6:
                game.update({6:turn})
            elif position == 1:
                game.update({1:turn})
            elif position == 2:
                game.update({2:turn})
            elif position == 3:
                game.update({3:turn})
            else:
                print("Invalid position!!!")
    position = int(input("\n Enter your position: "))
    play()
    creating_board()

for i in range(9):
    playing()
    if turn == player1:
        turn=player2
    else:
        turn = player1 
    check()