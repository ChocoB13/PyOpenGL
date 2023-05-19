import math

def moveobject(object, input_object, delta_time, units_per_second=5, degrees_per_second=60):
        move_amount = units_per_second * delta_time
        rotate_amount = degrees_per_second * (math.pi / 180) * delta_time
        if input_object.is_key_pressed('i'):
            object.translate(0, 0, -move_amount)
        if input_object.is_key_pressed('k'):
            object.translate(0, 0, move_amount)
        if input_object.is_key_pressed('j'):
            object.translate(-move_amount, 0, 0)
            #object.set_position([-5, 0, 0])
        if input_object.is_key_pressed('l'):
            object.translate(move_amount, 0, 0)
            #object.set_position([5, 0, 0])
        if input_object.is_key_pressed('y'):
            object.translate(0, move_amount, 0)
        if input_object.is_key_pressed('h'):
            object.translate(0, -move_amount, 0)
        if input_object.is_key_pressed('u'):
            object.rotate_y(-rotate_amount)
        if input_object.is_key_pressed('o'):
            object.rotate_y(rotate_amount)
        if input_object.is_key_pressed('up'):
            object.rotate_x(rotate_amount)
        if input_object.is_key_pressed('down'):
            object.rotate_x(-rotate_amount)
        if input_object.is_key_pressed('left'):
            object.rotate_z(-rotate_amount)
        if input_object.is_key_pressed('right'):
            object.rotate_z(rotate_amount)