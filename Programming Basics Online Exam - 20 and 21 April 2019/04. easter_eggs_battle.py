player_one = int(input())
player_two = int(input())

input_line = input()
while input_line != "End":

    if input_line != "one":
        player_one -= 1
    else:
        player_two -= 1
    if player_one == 0:
        print(f"Player one is out of eggs. Player two has {player_two} eggs left.")
        break
    elif player_two == 0:
        print(f"Player two is out of eggs. Player one has {player_one} eggs left.")
        break
    input_line = input()
if input_line == "End":
    print(f"Player one has {player_one} eggs left.")
    print(f"Player two has {player_two} eggs left.")
