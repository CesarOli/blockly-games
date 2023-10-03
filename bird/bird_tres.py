#bird_três

worm_captured = False

def heading(angle):
    print('new angle = ' + angle)

def does_not_have_worm():
    if worm_captured:
        return False
    else:
        return True


if does_not_have_worm():
    heading(300)

else:
    heading(60)