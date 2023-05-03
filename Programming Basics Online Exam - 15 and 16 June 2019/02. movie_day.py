import math

time_for_photos = int(input())
stages_count = int(input())
time_on_stage = int(input())

prepare_for_photos = time_for_photos * 0.15
time_for_scene = stages_count * time_on_stage
needed_time = prepare_for_photos + time_for_scene
diff = abs(needed_time - time_for_photos)
if time_for_photos > needed_time:
    print(f"You managed to finish the movie on time! You have {math.ceil(diff)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {math.ceil(diff)} minutes.")
