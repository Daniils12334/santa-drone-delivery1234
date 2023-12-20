from djitellopy import Tello

# Uzdevums: Iziet trasi ar koda palidzību
# Noteikumi:
# - secīgi jaiziet cauri visiem vārtiem
# - jaapmeklē visas platformas
# - jaātgriezas atpakaļ
# - caur vārtiem drīkst līdot tikai taisni (ar kāmeru priekšā)

# Dokumentācija un piemēri
# https://github.com/damiafuentes/DJITelloPy/tree/master
# https://github.com/damiafuentes/DJITelloPy/blob/master/examples/simple.py

tello = Tello()
tello.connect()
tello.set_speed(20)
tello.takeoff(72)
tello.rotate_clockwise(180)
tello.land(72)
tello.takeoff(72)
tello.move_forward(70)
tello.rotate_counter_clockwise(90)
tello.move_forward(86)
tello.land(72)
tello.takeoff(72)
tello.rotate_counter_clockwise(90)
tello.move_forward(62)
tello.rotate_counter_clockwise(90)
tello.move_forward(86)
tello.rotate_clockwise(90)
tello.move_forward(126)
tello.land(72)
