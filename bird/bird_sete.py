#bird_sete

worm_captured = False

def heading(angle):
    print('new angle = ' + angle)

def does_not_have_worm():
    if worm_captured:
        return False
    else:
        return True

def get_y_position():
    print('the current y position should be returned here.')

if get_y_position() > 50:
    heading(225)

elif does_not_have_worm():
    heading(315)
    
else:
    heading(180)
