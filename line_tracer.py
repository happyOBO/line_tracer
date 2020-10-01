
import ev3dev.ev3 as ev3
import time
ev3.Sound.beep()

rightmotor = ev3.LargeMotor('outC')
leftmotor = ev3.LargeMotor('outB')
sp = 200
flag = 200
visit_green = False
color_sensor = ev3.ColorSensor()
arrow = True
while (True):
    try:
        #cr = color_sensor.red
        #cg = color_sensor.green
        #cb = color_sensor.blue

        #print(color_sensor.red,",",color_sensor.green,",",color_sensor.blue)
        r_sp = sp
        l_sp = sp
        if(color_sensor.color == 1):
            r_sp += flag
            l_sp -= flag
            arrow = True
            pass
        elif(color_sensor.color == 5):
            rightmotor.stop()
            leftmotor.stop()
            break
        elif( color_sensor.color == 3 and (100 <= color_sensor.green <= 150) and color_sensor.red <= 50):
            print(color_sensor.green,",", color_sensor.red)
            if( not visit_green):
                rightmotor.stop()
                leftmotor.stop()
                time.sleep(3)
                ev3.Sound.beep()
                visit_green = True
                if(not arrow):
                    r_sp += flag
                    l_sp -= flag
                else:
                    r_sp -= flag
                    l_sp += flag
        else :
            r_sp -= flag
            l_sp += flag
            arrow = False
        rightmotor.run_to_rel_pos(position_sp = 1080, speed_sp = r_sp)
        leftmotor.run_to_rel_pos(position_sp = 1080, speed_sp = l_sp)
        # color_sensor = ev3.ColorSensor()
    except :
        rightmotor.stop()
        leftmotor.stop()
        break

ev3.Sound.beep()