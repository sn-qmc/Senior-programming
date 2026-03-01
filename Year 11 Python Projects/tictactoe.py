# 0 is empty, 1 is x, 2 is o
placed_tokens = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def main():
    for i in range(len(placed_tokens)):
        line = ""
        for j in range(len(placed_tokens[i])):
            line += "["
            if(placed_tokens[i][j]==0):
                line+=" "
            elif(placed_tokens[i][j]==1):
                line+="x"
            else:
                line+="o"
            line += "]"
        print(line)

def newTokenPlacement(who_is_playing):
    player_input = ""
    print("Please enter where you want to place the token: ")
    print("[1][2][3]\n[4][5][6]\n[7][8][9]")
    
    while True:
        player_input = input("A number from 1-9:")
        if player_input.isnumeric():
            player_input = int(player_input)
            if(player_input >= 1 and player_input <=9):
                break
            else:
                print("Please enter a value for 1-9")
        else:
            print("Please enter a real number!")
    row = 0
    column = 0
    if(player_input == 7 or player_input == 8 or player_input == 9):
        row = 2
        column = player_input - 7
    elif(player_input == 4 or player_input == 5 or player_input == 6):
        row = 1
        column = player_input - 4
    else:
        column = placed_tokens - 1
        
    placed_tokens[row][column] = who_is_playing
    
main()