needed_high = int(input())

lath_height = needed_high - 30
count_jumps = 0
final_jumps = 0
is_jumped = True
for jump in range(lath_height, needed_high + 1, 5):
    for i in range(1, 3 + 1):
        current_jump = int(input())
        count_jumps += 1
        final_jumps = jump

        if current_jump > jump:
            is_jumped = True
            break

        if i == 3:
            is_jumped = False
            break
    if is_jumped is not True:
        break
if is_jumped:
    print(f"Tihomir succeeded, he jumped over {final_jumps}cm after {count_jumps} jumps.")
else:
    print(f"Tihomir failed at {final_jumps}cm after {count_jumps} jumps.")
