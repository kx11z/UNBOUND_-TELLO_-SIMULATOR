from tello_sim import Simulator

d = Simulator()

d.takeoff()
d.forward(100)
d.ccw(90)
d.forward(100)
d.land()
