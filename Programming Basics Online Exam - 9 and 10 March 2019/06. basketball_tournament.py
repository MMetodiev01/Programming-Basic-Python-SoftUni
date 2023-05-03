name_of_tournament = input()

count_wins = 0
count_losses = 0
count_matches = 0
while name_of_tournament != "End of tournaments":
    number_of_matches = int(input())
    for i in range(1, number_of_matches + 1):
        team_desi_points = int(input())
        enemy_team_points = int(input())
        count_matches += 1
        if team_desi_points > enemy_team_points:
            count_wins += 1
            print(f"Game {i} of tournament {name_of_tournament}: win with {abs(team_desi_points - enemy_team_points)} points.")

        if enemy_team_points > team_desi_points:
            count_losses += 1
            print(f"Game {i} of tournament {name_of_tournament}: lost with {abs(enemy_team_points - team_desi_points)} points.")

    name_of_tournament = input()
    if name_of_tournament == "End of tournaments":
        break
percent_wins = count_wins / count_matches * 100
percent_losses = count_losses / count_matches * 100
print(f"{percent_wins:.2f}% matches win")
print(f"{percent_losses:.2f}% matches lost")
