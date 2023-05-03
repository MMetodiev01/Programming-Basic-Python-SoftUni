first_player = input()
second_player = input()

command = input()
first_player_points = 0
second_player_player_points = 0

while command != "End of game":
    first_card = int(command)
    second_card = int(input())

    if first_card > second_card:
        first_player_points += first_card - second_card
    elif second_card > first_card:
        second_player_player_points += second_card - first_card
    elif first_card == second_card:
        print(f"Number wars!")
        first_card = int(input())
        second_card = int(input())
        if first_card > second_card:
            print(f"{first_player} is winner with {first_player_points} points")
            break
        else:
            print(f"{second_player} is winner with {second_player_player_points} points")
            break
    command = input()
    if command == "End of game":
        print(f"{first_player} has {first_player_points} points")
        print(f"{second_player} has {second_player_player_points} points")
        break
