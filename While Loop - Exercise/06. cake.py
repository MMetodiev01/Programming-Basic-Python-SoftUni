length = int(input())
width = int(input())

total_pieces = width * length
is_no_more_pieces = False
input_line = input()
while input_line != "STOP":
    current_piece = int(input_line)

    total_pieces -= current_piece

    if total_pieces < 0:
        is_no_more_pieces = True
        break
    input_line = input()
if is_no_more_pieces:
    print(f'No more cake left! You need {abs(total_pieces)} pieces more.')
else:
    print(f'{total_pieces} pieces are left.')