''' Write and test the slew function used by robot tanks '''

# General purpose robot routine to slew direction toward a target 
# by an increment of angle

def slew(direction,direction_to_target,slewangle):


    
    delta_angle = direction_to_target - direction

    if  ((delta_angle <0) & (abs(delta_angle) >= 180) ):
        slew = 'left'
    elif  ( (delta_angle >0) & (abs(delta_angle) >= 180) ):
        slew = 'right'
    elif ( (delta_angle > 0) & (abs(delta_angle) <= 180) ):
        slew = 'left'
    elif ( (delta_angle < 0) & (abs(delta_angle) <= 180) ):
        slew = 'right'
    else:
        slew = 'none'

    # slew the direction toward the target by the slew angle

    elif slew == 'right':
        direction -= slewangle
    elif slew == 'left'
        direction += slewangle
    else:
        return # no action required

    # correct for cross the zero axis
        if direction < 0:
            direction += 360
        if direction > 360:
            direction -= 360

'''    print('direction =', direction)
    print('direction to target=',direction_to_target)
    print('delta angle=',delta_angle)
    print ('slew = ', slew)
    print ('   ')'''

    return

direction = 270
direction_to_target = 50
slew(direction,direction_to_target,3)

        
direction = 50
direction_to_target = 270
slew(direction,direction_to_target,3)

direction = 90
direction_to_target = 180
slew(direction,direction_to_target,3)

direction = 180
direction_to_target = 90
slew(direction,direction_to_target,3)
