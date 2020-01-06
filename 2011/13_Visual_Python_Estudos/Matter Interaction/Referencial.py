from __future__ import division
from visual import *

# Trajectory of a ball thrown on a rotating space station with 'artificial gravity'
# as seen from the inertial frame and from a frame rotating with the space station.

# Bruce Sherwood, Reims, France, August 2010
# based on a suggestion of Igal Galili at a physics education conference in Reims.

scene1 = display(x=0, y=0, width=500, height=530,
                   title='Inertial Reference Frame', userspin=False, userzoom=False)
scene2 = display(x=500, y=0, width=500, height=530,
                      title='Rotating Reference Frame', userspin=False, userzoom=False)

class spacestation(object):
    def __init__(self, whichdisplay):
        N = 50 # number of boxes used to create the ring-shaped space station
        self.R = R = 10 # inner radius of space station
        self.h = h = 2 # height of release of ball above the "floor" of the space station
        thick = 0.5 # thickness of space station
        whichdisplay.select()
        self.frame = frame()
        dtheta = 2*pi/N
        paint = color.red
        red = True
        for N in list(range(N)):
            theta = N*dtheta
            b = box(frame=self.frame, pos=(R+thick/2)*vector(cos(theta),sin(theta),0),
                    size=(thick,2*(R+thick)*sin(dtheta/2),thick))
            if red:
                b.color = color.red
                red = False
            else:
                b.color = color.blue
                red = True
            b.rotate(angle=theta, axis=(0,0,1))
    
        self.person = cylinder(frame=self.frame, pos=(0,-R,0), axis=(0,h,0), radius=0.1)
        self.ball = sphere(pos=self.person.pos+self.person.axis, radius=0.2, color=color.cyan)
        self.trail = curve(color=self.ball.color)

    def reset(self):
        newpos = self.frame.frame_to_world(self.person.pos)
        angle = atan2(newpos.x,-newpos.y)
        self.frame.rotate(angle=-angle, axis=(0,0,1))
        self.ball.pos = self.person.pos+self.person.axis
        self.trail.pos = []

station1 = spacestation(scene1)
station2 = spacestation(scene2)
scene1.autoscale = scene2.autoscale = False

omega = 1 # angular speed of space station
deltat = 0.001*2*pi/omega # period of rotation is 2*pi/omega

v0 = omega*(station1.R-station1.h)
scalefactor = 5/(omega*station1.R)
v1 = arrow(display=scene1, pos=station1.ball.pos, color=color.green,
           axis=(0,0,0), shaftwidth=0.4, visible=False)
v2 = arrow(display=scene2, pos=station2.ball.pos, color=color.green,
           axis=(0,0,0), shaftwidth=0.4, visible=False)
instruct1 = label(display=scene1, pos=(0,station1.R/2,0), 
                  text="Drag this arrow to choose the initial velocity\nin the inertial frame.", visible=False)
instruct2 = label(display=scene2, pos=(0,station2.R/2,0),
                  text="Or drag this arrow to choose the initial velocity\nrelative to the rotating space station.", visible=False)
click1 = label(display=scene1, pos=(-0.88*station1.R,-0.95*station1.R,0),
               text="Click to\nstart over", visible=False)
click2 = label(display=scene2, pos=(-0.88*station1.R,-0.95*station1.R,0),
               text="Click to\nstart over", visible=False)

while True:
    station1.reset()
    station2.reset()
    v1.axis = scalefactor*vector(v0,v0,0)
    v2.axis = scalefactor*vector(0,v0,0)
    v1.visible = v2.visible = True
    instruct1.visible = instruct2.visible = True
    drag1 = drag2 = False
    while True:
        rate(50)
        if drag1:
            v1.axis = scene1.mouse.pos-v1.pos
            v2.axis = v1.axis
            v2.axis.x -= scalefactor*v0
        if drag2:
            v2.axis = scene2.mouse.pos-v2.pos
            v1.axis = v2.axis
            v1.axis.x += scalefactor*v0
        if scene1.mouse.events:
            m = scene1.mouse.getevent()
            if m.press == 'left':
                drag1 = True
            elif drag1 and (m.drop == 'left' or m.release == 'left'):
                if mag(v1.axis) <= station1.ball.radius:
                    v1.axis = (0,0,0)
                v = v1.axis/scalefactor
                break
        elif scene2.mouse.events:
            m = scene2.mouse.getevent()
            if m.press == 'left':
                drag2 = True
            elif drag2 and (m.drop == 'left' or m.release == 'left'):
                if mag(v2.axis) <= station2.ball.radius:
                    v2.axis = (0,0,0)
                v = v2.axis/scalefactor
                v.x += v0
                break

    v1.visible = v2.visible = False
    instruct1.visible = instruct2.visible = False
    click1.visible = click2.visible = True
    r = vector(station1.ball.pos) # must initialize r without making it equivalent to ball.pos
    t = 0
    finish = False
    while True:
        rate(0.5/deltat) # slow down the plotting
        if scene1.mouse.clicked:
            m = scene1.mouse.getevent()
            finish = True
            break
        if scene2.mouse.clicked:
            m = scene2.mouse.getevent()
            finish = True
            break
        station1.frame.rotate(angle=omega*deltat, axis=(0,0,1))
        r += v*deltat # update the actual position of the ball (in inertial frame)
        station1.ball.pos = r
        newr = vector(r)
        station2.ball.pos = newr.rotate(angle=-omega*t, axis=(0,0,1))
        station1.trail.append(pos=station1.ball.pos)
        station2.trail.append(pos=station2.ball.pos)
        if mag(station1.ball.pos) >= station1.R: # if ball hits floor, make it stick there
            direction = norm(station1.ball.pos)
            station1.ball.pos = station1.R*direction
            direction = norm(station2.ball.pos)
            station2.ball.pos = station2.R*direction
            break
        t += deltat

    if not finish:
        while True:
            rate(50)
            if scene1.mouse.clicked:
                scene1.mouse.getevent()
                break
            if scene2.mouse.clicked:
                scene2.mouse.getevent()
                break
    click1.visible = click2.visible = False