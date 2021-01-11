def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    while wall_in_front() and wall_on_right():
        turn_left()
    while wall_in_front():
        turn_right()
 
while not at_goal():
        if front_is_clear():
            move()
        else:
            hurdle()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
