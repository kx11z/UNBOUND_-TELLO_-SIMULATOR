from tello_sim import Simulator

d = Simulator()

d.takeoff()
d.forward(100)
d.ccw(90)
d.flip("l")
d.forward(100)
d.land()

# Keep the 3D plot open and interactive — click-drag to rotate, scroll to zoom.
d.show()
