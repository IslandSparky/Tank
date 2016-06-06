# write and test is_aim_ok

# general purpose robot routine to see if the target is in the
# angle range of the direction we are pointed. Returns True if we are
# on target.

def is_aim_ok(direction,direction_to_target,tolerance):


    # first fix any issues with crossing the zero axis.

    if (  (direction > 0 & (direction < 90)) &
            (direction_to_target >270) ):

            direction += 180  # move to left quantrant
            direction_to_target -= 180

    elif ( (direction_to_target > 0 & (direction_to_target < 90) ) &
            (direction > 270) ):

           direction_to_target += 180 # move to left quantrant
           direction -= 180

    # that possible problem fixed, now do the compare and return
    # either true or false

    print ('direction,direction_to_target=',direction,direction_to_target)
    if ( abs(direction - direction_to_target) <= tolerance ):
        return True
    else:
        return False

print (is_aim_ok(50,51,3))
print (is_aim_ok(50,54,3))
print (is_aim_ok(1,359,3) )
print (is_aim_ok(359,1,3) )
           
           
                
