


from visual import *
scene.range = 5 # fixed size, no autoscaling
ball = sphere(pos=(-3,0,0), color=color.cyan)
cube = box(pos=(+3,0,0), size=(2,2,2), color=color.red)
pick = None # no object picked out of the scene yet
while True: 
    if scene.mouse.events: 
        m1 = scene.mouse.getevent() # get event
        if m1.drag and m1.pick == ball: # if touched ball
            drag_pos = m1.pickpos # where on the ball
            pick = m1.pick # pick now true (not None) 
        elif m1.drop: # released at end of drag
            pick = None # end dragging (None is false)
    if pick:
        # project onto xy plane, even if scene rotated:
        new_pos = scene.mouse.project(normal=(0,0,1)) 
        if new_pos != drag_pos: # if mouse has moved
            # offset for where the ball was clicked:
            pick.pos += new_pos - drag_pos 
            drag_pos = new_pos # update drag position