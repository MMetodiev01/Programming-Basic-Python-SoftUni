command = input()
name = ""
bestMovie = 0
counter = 0
while command != "STOP":
    current_movie = command
    counter += 1
    length = len(current_movie)

    cur_Best_movie = 0
    for i in current_movie:
        cur_letter = ord(i)
        if 97 <= cur_letter <= 122:
            cur_letter -= length * 2
            cur_Best_movie += cur_letter
        elif 65 <= cur_letter <= 90:
            cur_letter -= length
            cur_Best_movie += cur_letter
        else:
            cur_Best_movie += cur_letter
    if cur_Best_movie > bestMovie:
        bestMovie = cur_Best_movie
        name = current_movie
    if counter == 7:
        print(f"The limit is reached.")
        break
    command = input()
    if command == "STOP":
        break
print(f"The best movie for you is {name} with {bestMovie} ASCII sum.")