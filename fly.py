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
tello.set_speed(15)
tello.takeoff()
tello.rotate_clockwise(180)
tello.move_forward(60)
tello.rotate_counter_clockwise(90)
tello.move_forward(78)
tello.land()
tello.takeoff()
tello.rotate_counter_clockwise(90)
tello.move_forward(56)
tello.rotate_counter_clockwise(90)
tello.move_forward(78)
tello.rotate_clockwise(90)
tello.move_forward(126)
tello.land()
