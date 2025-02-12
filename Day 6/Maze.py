#This is a python code for a maze game website known as 'Reeborg's world' and by this link
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#you can go to the website and test it.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
while at_goal() == False:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()