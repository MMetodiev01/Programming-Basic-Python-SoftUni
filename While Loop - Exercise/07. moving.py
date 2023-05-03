# width_free_space = int(input())
# length_free_space = int(input())
# height_free_space = int(input())
#
# total_space = width_free_space * length_free_space * height_free_space
# is_no_more_space = False
# input_line = input()
# while input_line != "Done":
#     current_count_boxes = int(input_line)
#
#     total_space -= current_count_boxes
#
#     if total_space <= 0:
#         is_no_more_space = True
#         break
#     input_line = input()
# if is_no_more_space:
#     print(f'No more free space! You need {abs(total_space)} Cubic meters more.')
# else:
#     print(f'{total_space} Cubic meters left.')


# width_free_space = int(input())
# length_free_space = int(input())
# height_free_space = int(input())
#
# total_space = width_free_space * length_free_space * height_free_space
#
# sum_boxes = 0
# input_line = input()
# while input_line != "Done":
#     current_count_boxes = int(input_line)
#
#     sum_boxes += current_count_boxes
#
#     if sum_boxes >= total_space:
#         break
#
#     input_line = input()
# diff = abs(total_space - sum_boxes)
# if sum_boxes >= total_space:
#     print(f'No more free space! You need {diff} Cubic meters more.')
# else:
#     print(f'{diff} Cubic meters left.')