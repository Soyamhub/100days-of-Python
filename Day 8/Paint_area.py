import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")


test_h = int(input("Write the height of the room\n"))
test_w = int(input("Write the width of the room\n"))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)