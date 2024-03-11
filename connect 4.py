#author : hesham mohamed koutp fahmy
#id: 20230458
#task: number6 bouns 2 game number 2 connect 4 game
#purpose:first player can get any 4 (x or o ) by  row , column and diagonally win won 0
#version: 4
#date: 2024 / 3 / 2
game_list = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]
counter=0                 # when it became 42 then will draw
def check_win():
    for i in range(len(game_list)):
        for j in range(7):
            if game_list[i][j] != '#':  # If the cell is not empty
                symbol = game_list[i][j]

                # Check horizontally
                if j + 3 < len(game_list[0]) and all(game_list[i][j+k] == symbol for k in range(4)):
                    print("Player 1 wins!" if symbol == "x" else "Player 2 wins!")
                    main_menu()

                # Check vertically
                if i + 3 < len(game_list) and all(game_list[i+k][j] == symbol for k in range(4)):
                    print("Player 1 wins!" if symbol == "x" else "Player 2 wins!")
                    main_menu()

                # Check diagonally (down-right)
                if i + 3 < len(game_list) and j + 3 < len(game_list[0]) and all(game_list[i+k][j+k] == symbol for k in range(4)):
                    print("Player 1 wins!" if symbol == "x" else "Player 2 wins!")
                    main_menu()

                # Check diagonally (down-left)
                if i + 3 < len(game_list) and j - 3 >= 0 and all(game_list[i+k][j-k] == symbol for k in range(4)):
                    print("Player 1 wins!" if symbol == "x" else "Player 2 wins!")
                    main_menu()

    # If no winner is found and the board is full, declare a draw
    if counter == 42:
        print("Draw!")
        main_menu()


def check_column():
    i1 = i2 = i3 = i4 = i5 = i6 = i7 = 5
    counter=0
    player = 1  # Start with player 1
    while True:
        while True:
            try:
                choose = int(input(f"Player {player} input number between 1 and 7: "))
                if 1 <= choose <= 7:
                    break  # Exit the loop if the input is within the valid range
                else:
                    print("Please enter a number between 1 and 7.")
            except ValueError:
                print("Please enter a valid integer.")

        # At this point, 'choose' will contain the valid integer input between 1 and 7.

        while choose > 7 or choose < 1:
            choose = int(input("Input number between 1 and 7 \n"))
        if choose == 1:
            if i1 <= -1:
                while choose == 1:
                    print("Sorry, this column is full. Choose another column: ")
                    break
                continue
            game_list[i1][0] = "x" if player == 1 else "o"
            i1 -= 1
        elif choose == 2:
            if i2 <= -1:
                while choose == 2:
                    print("Sorry, this column is full. Choose another column: ")
                    break
                continue
            game_list[i2][1] = "x" if player == 1 else "o"
            i2 -= 1
        elif choose == 3:
            if i3 <= -1:
                while choose == 3:
                    print("Sorry, this column is full. Choose another column: ")
                    break
                continue
            game_list[i3][2] = "x" if player == 1 else "o"
            i3 -= 1
        elif choose == 4:
            if i4 <= -1:
                while choose == 4:
                    print("Sorry, this column is full. Choose another column: ")
                    break
                continue
            game_list[i4][3] = "x" if player == 1 else "o"
            i4 -= 1
        elif choose == 5:
            if i5 <= -1:
                while choose == 5:
                    print("Sorry, this column is full. Choose another column: ")
                    break
                continue
            game_list[i5][4] = "x" if player == 1 else "o"
            i5 -= 1
        elif choose == 6:
            if i6 <= -1:
                while choose == 6:
                    print("Sorry, this column is full. Choose another column: ")
                    break
                continue
            game_list[i6][5] = "x" if player == 1 else "o"
            i6 -= 1
        elif choose == 7:
            if i7 <= -1:
                while choose == 7:
                    print("Sorry, this column is full. Choose another column: ")
                    break
                continue
            game_list[i7][6] = "x" if player == 1 else "o"
            i7 -= 1

        # Switch to the other player
        player = 2 if player == 1 else 1
        for row in game_list:
            print("          ", row)
        counter += 1
        if counter==42:
            print("draw")
            exit()
        check_win()
def main_menu():
 print("hello in connect 4 game")
 print("rules: first player can get any 4 (x or o ) by  row , column and diagonally win won ")
 while True:
     print("do you want to play :")
     print("A: Play the game")
     print("B: exit the programme")
     choose2=input().upper()
     if choose2=="A":
            game_list = [
                ['#', '#', '#', '#', '#', '#', '#'],
                ['#', '#', '#', '#', '#', '#', '#'],
                ['#', '#', '#', '#', '#', '#', '#'],
                ['#', '#', '#', '#', '#', '#', '#'],
                ['#', '#', '#', '#', '#', '#', '#'],
                ['#', '#', '#', '#', '#', '#', '#']
            ]
            for row in game_list:
                print("          ", row)

            check_column()
     elif choose2=="B":
       print("thank you for using our programme ...")
       exit()
     else:
       print("invalid input")
       continue
main_menu()