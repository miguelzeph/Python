from __future__ import division
from visual.controls import *
import os
from time import clock # to identify a doubleclick

# Bruce Sherwood, begun Spring 2002, major revision Spring 2006.
# Based on "EM Field" by David Trowbridge and Bruce Sherwood,
# which won first prize in the 1991 Educational Software Contest
# of the journal Computers in Physics.

# Originally written in the cT programming language and distributed
# by Physics Academic Software (http://webassign.net/pas).
# See the cT archives at vpython.org.
# Feel free to use this code in any way you like.

# Omissions: The original program "EM Field" displayed field lines and equipotentials,
# and it contained some explanatory displays about how the integrals were computed.

print """
Drag charges or currents out of the storage boxes at top of screen.
Drag charges or currents into storage boxes to remove from active sources.
Drag charge or current to reposition.
Click or drag with left button away from charges or currents to show field.
Drag with left button to create
  a Gaussian surface around a long charged rod,
  or an Amperian contour around a line current,
  or in 3D (electric) a round-trip potential (line integral).
Positive charge is red, negative charge is blue.
Current out of screen is magenta, current into screen is green.
"""

def resetscene():
    scene.up = (0,1,0)
    scene.forward = (0,0,-1)
    
scene.x = scene.y = 0
wscene = 700
hscene = 700
scene.background = color.white
scene.foreground = color.white
scene.height = hscene
scene.width = wscene
scene.range = 10
scene.fov = 0.001 # look at charged rods or currents end-on
##scene.show_rendertime = 1

# Main modes
ELECTRIC = 1; MAGNETIC = 2
# Types of measurement (or SOURCE if dragging a charge)
SOURCE = 1; VECTOR = 2; UNITVECTOR = 3; LINE = 4; SURFACE = 5

# Initial settings:
dim = 2 # 2 for 2D, 3 for 3D
mode = ELECTRIC
measure = VECTOR

k = 1 # electric or magnetic constant
q = 1 # elementary charge
rq = 0.3 # radius of charge or wire
constrain = False # constrain sources and vectors to be placed on integer grid
Qpos = color.red
Qneg = color.blue
Ipos = color.magenta
Ineg = color.green
Ecolor = color.orange # electric field color
Mcolor = color.cyan # magnetic field color
EFcolor = (0.73, 0.62, 0) # flux color for E Gaussian surface
MFcolor = (0, 0.7, 0.7) # flux color for B Gaussian surface
Fcolor = EFcolor # initially
Eshaft = 0.3
Escale = 10
Gscale = 5 # for Gauss's law
Ascale = 1 # for Ampere's law
Gtolerance = 0.5 # shortest dl for Gaussian surface
dz = vector(0,0,0.1) # place curves in front of flux etc.
offset = vector(1.5,0,0) # for label on line/surface integrals
rcurve = 0.07
sources = [] # list of sources now on screen
fields = [] # list of field vectors now on screen
Gmeasures = [] # list of all the current Gaussian surfaces or Amperian loops

def save_file(file_extensions=None, x=100, y=100, title="Save", mode='w', maxfiles=20):
    if maxfiles < 5: maxfiles = 5
    if mode[0] != 'w':
        raise ValueError, "To save a file, mode must start with 'w'."
    if file_extensions is not None:
        if isinstance(file_extensions, (list,tuple)):
            raise ValueError, "Only one file extension can be specified."
        file_extensions = [file_extensions]
    return filedialog(file_extensions=file_extensions,
                   x=x, y=y, title=title, mode=mode, maxfiles=maxfiles)

def get_file(file_extensions=None, x=100, y=100, title="Open", mode='rU', maxfiles=20):
    if maxfiles < 5: maxfiles = 5
    if mode[0] != 'r' and mode != 'U':
        raise ValueError, "To read a file, mode must start with 'r'."
    if file_extensions is not None:
        if not isinstance(file_extensions, (list,tuple)):
            file_extensions = [file_extensions]
    return filedialog(file_extensions=file_extensions,
                   x=x, y=y, title=title, mode=mode, maxfiles=maxfiles)

def filedialog(file_extensions=None, x=100, y=100, title="Open", mode='rU', maxfiles=20):
    # file_extensions is a list of types (reading) or a 1-element list (writing)
    writing =  not (mode[0] == 'r' or mode == 'U')
    filecolor = color.black
    dircolor = (0,0.5,0.5)
    selectcolor = (.7,1,1)
    inactivecolor = (0.8,0.8,0.8)
    activecolor = (0.6,0.6,0.6)
    winwidth = 300
    hitem = 20 # pixel height of each menu listing
    ctrls = 20 # button area
    hcanvas = hitem*(maxfiles+3)+ctrls # approx height without title bar
    currentdisplay = display.get_selected()
    menus = display(background=color.white, foreground=color.black, exit=0, range=100,
                       x=x, y=y, title=title, fov=0.001,
                       # allow 30 pixels for title bar
                       width=winwidth, height=30+hcanvas+ctrls)
    if menus.width >= hcanvas+ctrls:
        hmenu = 200.*hitem/menus.width
        ytop = 100.*hcanvas/menus.width-2*hmenu
        ybottom = ytop-maxfiles*hmenu
        ytopscroll = 100.*(hcanvas+ctrls)/menus.width
        ybottomscroll = -ytopscroll
        xmax = 100.
        xmin = -xmax
        scroll_edge = 87.
        okaypos = (20,ybottom-1.2*hmenu,0.1)
        cancelpos = (60,ybottom-1.2*hmenu,0.1)
        okaysize = (35,1.1*hmenu,0.1)
    else:
        hmenu = 200.*hitem/hcanvas
        ytop = 100.-2*hmenu
        ybottom = ytop-maxfiles*hmenu
        ytopscroll = 100.
        ybottomscroll = -ytopscroll
        xmax = 100.*menus.width/(hcanvas+ctrls)
        xmin = -xmax
        scroll_edge = xmax-14*menus.width/hcanvas
        okaypos = (20.*menus.width/hcanvas,ybottom-1.2*hmenu,0.1)
        cancelpos = (60.*menus.width/hcanvas,ybottom-1.2*hmenu,0.1)
        okaysize = (35.*menus.width/hcanvas,1.1*hmenu,0.1)
    okay = box(pos=okaypos, size=okaysize, color=inactivecolor)
    if writing:
        t = 'Save'
    else:
        t = 'Open'
    okaylabel = label(pos=okaypos, text=t, color=color.black, opacity=0, box=0)
    cancel = box(pos=cancelpos, size=okaysize, color=inactivecolor)
    label(pos=cancelpos, text='Cancel', color=color.black, opacity=0, box=0)
    go_up = box(pos=(cancel.pos.x,ytop+hmenu,0), size=okaysize, color=inactivecolor)
    go_up_arr = arrow(pos=(go_up.pos.x,go_up.pos.y-0.4*hmenu,0), axis=(0,0.9*hmenu,0),
          fixedwidth=1, shaftwidth=0.3*hmenu, color=(0.9,0,0))
    showdir = label(pos=(xmin+0.2*(xmax-scroll_edge),ytop+hmenu,0), text='',
                    color=dircolor, opacity=0, xoffset=1, box=0, line=0)
    if writing:
        # A bug in Visual 3 makes it necessary not to allow len(getname.text) < 1
        getname = label(pos=(xmin+0.5*(xmax-scroll_edge),okay.y,0), border = 2,
                        text='|', box=0, xoffset=1, line=0, opacity=0)
        z = 0.1
        curve(pos=[(getname.x,getname.y-0.5*hmenu,z), (getname.x,getname.y+0.5*hmenu,z),
                   (okay.x-1.2*0.5*okay.length,getname.y+0.5*hmenu,z), 
                   (okay.x-1.2*0.5*okay.length,getname.y-0.5*hmenu,z),
                   (getname.x,getname.y-0.5*hmenu,z)])

    labels = []
    for n in range(maxfiles):
        labels.append(label(pos=(xmin+0.5*(xmax-scroll_edge),ytop-n*hmenu),
                            text='', opacity=0, box=0,
                            xoffset=1, line=0))
        
    scrolltrack = box(pos=(0.5*(scroll_edge+xmax),0,0.02),
                      color=color.white, size=(xmax-scroll_edge,200,0.001), visible=0)
    scrollside = curve(pos=[(scroll_edge,100,.03),(scroll_edge,-100,.03)],
                       color=(0.8,0.8,0.8), visible=0)
    scroll = box(pos=(0.5*(scroll_edge+xmax),0,0.04), offset=vector(0,0,0),
                 color=inactivecolor, size=((xmax-scroll_edge+1),0,0.1), visible=0)
    
    shade = box(pos=(0,0,0), color=(.95,.95,.95), size=(200,hmenu,0.01), visible=0)
    select = box(pos=(0,0,0.01), color=selectcolor, size=(200,hmenu,0.01), visible=0)
    clicktime = -1

    while menus.visible:
        shade.visible = 0
        select.visible = 0
        highlighted = None
        selected = None
        changedir = False
        drag = False
        topmenu = 0
        showdir.text = os.path.split(os.getcwd())[-1]
        allfiles = os.listdir(os.curdir)
        files = []
        for f in allfiles:
            is_a_dir = os.path.isdir(f)
            if is_a_dir or (file_extensions is None):
                files.append([f,is_a_dir,False]) # file name, whether a directory, whether selected
            else:
                period = f.rfind('.')
                if period:
                    if f[period:] in file_extensions:
                        files.append([f,is_a_dir,False])
        Nfiles = len(files)
        need_to_scroll = (Nfiles > maxfiles)
        if need_to_scroll:
            Nfiles = maxfiles
            hscroll = (ytopscroll-ybottomscroll)*maxfiles/len(files)
            if hscroll < hmenu:
                hscroll = hmenu
            dy = (ytopscroll-ybottomscroll-hscroll)/(len(files)-maxfiles)
            scrolltrack.visible = 1
            scrollside.visible = 1
            scroll.y = ytopscroll-0.5*hscroll
            scroll.height = hscroll
            scroll.visible = 1
        else:
            scrolltrack.visible = 0
            scrollside.visible = 0
            scroll.visible = 0

        for n in labels:
            n.text = ''
        for n, f in enumerate(files[:Nfiles]):
            lcolor = filecolor
            if f[1]: lcolor = dircolor
            labels[n].text = f[0]
            labels[n].color = lcolor

        if writing:
            getname.text = '|'
            ending = '|'
        blink = clock()
        blinkon = True
        while menus.visible:
            rate(50)
            # A bug in Visual 3 makes it necessary not to allow len(getname.text) < 1
            if writing and clock()-blink > 0.5:
                blink = clock()
                blinkon = not blinkon
                if blinkon:
                    ending = '|'
                else:
                    ending = ' '
                if getname.text == '':
                    getname.text = ending
                elif getname.text == '|' or getname.text == ' ':
                    getname.text = ending
                elif getname.text[-1] == '|' or getname.text[-1] == ' ':
                    getname.text = getname.text[:-1]+ending 
                else:
                    getname.text += ending
            mpos = menus.mouse.pos
            if writing and menus.kb.keys: # event waiting to be processed?
                s = menus.kb.getkey() # get keyboard info; make sure string length never 0
                if s == '\n':
                    shade.visible = 0
                    select.visible = 0
                    ret = finish_save(getname.text, file_extensions, mode, menus, labels, currentdisplay)
                    if ret:
                        return ret
                    if highlighted: shade.visible = 1
                    if selected: select.visible = 1
                elif len(s) == 1 and s != '|':
                    if getname.text == '': # should never happen
                        getname.text = s+ending
                    elif getname.text[-1] == ending:
                        getname.text = getname.text[:-1]+s+ending
                    else:
                        getname.text = getname.text+s+ending # add new character
                elif s == 'backspace' or s == 'delete':
                    if getname.text == '': # should never happen
                        getname.text = ending
                    elif getname.text[-1] == ending:
                        getname.text = getname.text[:-2]+ending # erase character
                    else:
                        if len(getname.text) <= 1: # should never happen
                            getname.text = ending
                        else:
                            getname.text = getname.text[:-1]+ending # erase character
                elif s == 'shift+delete' or s == 'shift+backspace':
                    getname.text = ending # erase all text
            if menus.mouse.events:
                m = menus.mouse.getevent()
                mpos = m.pos
                nmenu = int((ytop+0.5*hmenu-mpos.y)/hmenu)
                if mpos.y > ytop+0.5*hmenu: nmenu = -1
                if drag and m.release == 'left':
                    drag = False
                elif need_to_scroll and m.pick == scroll:
                    scroll.color = dircolor
                    scroll.offset = scroll.y-mpos.y
                    drag = True
                elif m.click == 'left':

                    # Check for clicking go up or open or cancel
                    if m.pick == go_up or m.pick == go_up_arr:
                        os.chdir('../')
                        changedir = True
                        break
                    if m.pick == cancel:
                        return finish_get(None, mode, menus, currentdisplay)
                    elif m.pick == okay:
                        if writing and getname.text != '|':
                            shade.visible = 0
                            select.visible = 0
                            ret = finish_save(getname.text, file_extensions, mode, menus, labels, currentdisplay)
                            if ret:
                                return ret
                            if highlighted: shade.visible = 1
                            if selected: select.visible = 1
                        if selected is not None:
                            filename, is_a_dir, s = files[selected]
                            if is_a_dir:
                                os.chdir(filename)
                                changedir = True
                                break
                            elif not writing:
                                return finish_get(filename, mode, menus, currentdisplay)
                        
                    # Handle doubleclick on a name
                    clicktime = clock()-clicktime
                    if topmenu+nmenu == selected and clicktime < 0.5:
                        filename, is_a_dir, s = files[selected]
                        if is_a_dir:
                            os.chdir(filename)
                            changedir = True
                            break
                        else:
                            if writing:
                                getname.text = filename+'|'
                            else:
                                return finish_get(filename, mode, menus, currentdisplay)
                        
                    # Handle singleclick on a name
                    if (0 <= nmenu <= Nfiles-1):
                        select.y = ytop-nmenu*hmenu
                        select.visible = 1
                        if selected:
                            files[selected][2] = False
                        selected = topmenu+nmenu
                        files[selected][2] = True
                        if writing:
                            if files[selected][1]:
                                okaylabel.text = 'Open'
                            else:
                                okaylabel.text = 'Save'
                        clicktime = clock()
                    elif selected:
                        select.visible = 0
                        files[selected][2] = False
                        selected = 0
                        if writing:
                            okaylabel.text = 'Save'
                        
            if drag:
                newy = mpos.y+scroll.offset
                if newy+0.5*hscroll >= ytopscroll:
                    scroll.y = ytopscroll-0.5*hscroll
                    scroll.offset = scroll.y-mpos.y
                elif newy-0.5*hscroll <= ybottomscroll:
                    scroll.y = ybottomscroll+0.5*hscroll
                    scroll.offset = scroll.y-mpos.y
                else:
                    scroll.y = newy
                newtopmenu = int((ytopscroll-0.5*hscroll-scroll.y)/dy)
                if newtopmenu != topmenu:
                    topmenu = newtopmenu
                    select.visible = 0
                    for n, lab in enumerate(labels):
                        lab.text = files[n+topmenu][0]
                        if files[n+topmenu][2]:
                            select.y = ytop-n*hmenu
                            select.visible = 1
                        elif files[n+topmenu][1]:
                            lab.color = dircolor
                        else:
                            lab.color = filecolor
            else:
                if need_to_scroll:
                    if menus.mouse.pick == scroll:
                        scroll.color = activecolor
                    else:
                        scroll.color = inactivecolor
                        
                if menus.mouse.pick == go_up or menus.mouse.pick == go_up_arr:
                    go_up.color = activecolor
                else:
                    go_up.color = inactivecolor
                    
                if menus.mouse.pick == cancel:
                    cancel.color = activecolor
                else:
                    cancel.color = inactivecolor
                    
                if menus.mouse.pick == okay:
                    okay.color = activecolor
                else:
                    okay.color = inactivecolor
                    
                if need_to_scroll and mpos.x >= scroll_edge:
                    shade.visible = 0
                    highlighted = None
                else:
                    nmenu = int((ytop+0.5*hmenu-mpos.y)/hmenu)
                    if mpos.y > ytop+0.5*hmenu: nmenu = -1
                    if mpos.y < ytop+0.5*hmenu-hmenu*Nfiles: nmenu = -1
                    if (0 <= nmenu <= Nfiles):
                        shade.y = ytop-nmenu*hmenu
                        shade.visible = 1
                        highlighted = nmenu
                    else:
                        shade.visible = 0
                        highlighted = None
        if changedir: continue
        break
    currentdisplay.select()
    return None

def finish_get(filename, mode, menus, currentdisplay):
    menus.visible = 0
    del menus
    currentdisplay.select()
    if filename is None:
        return None
    return open(str(filename), mode)

def finish_save(filename, file_extensions, mode, menus, labels, currentdisplay):
    if filename == '':
        return None
    if filename[-1] == '|' or filename[-1] == ' ':
        filename = filename[:-1]
    if filename == '':
        return None
    t = filename.split(".")
    ext = ''
    if len(t) > 0:
        ext = '.'+t[-1]
    elif t[0] == '':
        return None
    if file_extensions is not None:
        if ext != file_extensions[0]:
            filename += file_extensions[0]
    try:
        fd = open(str(filename), 'r') # see whether file already exists
    except:
        menus.visible = 0
        del menus
        currentdisplay.select()
        return open(str(filename), mode)
    fd.close()
    for a in labels:
        a.visible = 0
    inactivecolor = (0.8,0.8,0.8)
    activecolor = (0.6,0.6,0.6)
    templabel = label(pos=(0,15,0.3), text="%s already exists" % filename, box=0, opacity=0)
    overwrite = box(pos=(-30,-5,0.4), size=(50,15,.1), color=inactivecolor)
    overlabel = label(pos=overwrite.pos, text="Overwrite", box=0, opacity=0)
    cancel = box(pos=(30,-5,0.4), size=(50,15,.1), color=inactivecolor)
    cancellabel = label(pos=cancel.pos, text="Cancel", box=0, opacity=0)
    while menus.visible:
        rate(50)
        if menus.mouse.events:
            m = menus.mouse.getevent()
            if m.click == 'left':
                if m.pick == overwrite:
                    menus.visible = 0
                    del menus
                    currentdisplay.select()
                    return open(str(filename), mode)
                if m.pick == cancel:
                    templabel.visible = 0
                    overwrite.visible = 0
                    overlabel.visible = 0
                    cancel.visible = 0
                    cancellabel.visible = 0
                    del templabel
                    del overwrite
                    del overlabel
                    del cancel
                    del cancellabel
                    for a in labels:
                        a.visible = 1
                    return None
        if menus.mouse.pick == overwrite:
            overwrite.color = activecolor
        else:
            overwrite.color = inactivecolor
        if menus.mouse.pick == cancel:
            cancel.color = activecolor
        else:
            cancel.color = inactivecolor
    return None

class ChargeBox(object):
    def __init__(self, center, sign):
        w = 1.5
        h = 1.5
        t = 0.2
        d = 0.2
        self.icon = None
        self.center = center
        self.region = (center.x-w/2,center.y-h/2,center.x+w/2,center.y+h/2)
        self.sign = sign
        self.frame = frame(pos=center)
        for x in (-w/2,w/2):
            box(frame=self.frame, pos=(x,0,0), size=(t,h+t,d), color=color.black)
        for y in (-h/2,h/2):
            box(frame=self.frame, pos=(0,y,0), size=(w,t,d), color=color.black)
        self.update()

    def update(self):
        if self.sign > 0:
            if mode == ELECTRIC:
                c = Qpos
            else:
                c = Ipos
        else:
            if mode == ELECTRIC:
                c = Qneg
            else:
                c = Ineg
        if self.icon:
            self.icon.visible = 0
        if dim == 3:
            self.icon = sphere(frame=self.frame, radius=rq, color=c)
        else:
            self.icon = cylinder(frame=self.frame, radius=rq, axis=(0,0,rq), color=c)

    def visible(self, vis):
        self.icon.visible = vis

    def inbox(self, point):
        return ( (self.region[0] <= point.x <= self.region[2]) and (self.region[1] <= point.y <= self.region[3]) )

class Gmeasure(object):
    def __init__(self, labelpos):
        self.elements = [] # (p1, p2, faces)
        self.curve = curve(color=FieldDrag.lcolor, radius=rcurve)
        self.curve.append(pos=labelpos)
        self.label = label(pos=labelpos+offset, box=0, opacity=1,
                           color=color.white, visible=0)
        self.measure = measure
        self.turning = 0
        self.flux = None
        
    def showsource(self):
        source = round(self.flux/(2*pi))
        if self.turning < 0:
            source = -source
        if mode == ELECTRIC:
            if self.measure == SURFACE:
                s = 'Q'
                if abs(abs(self.turning)-2*pi) > 0.001*pi:
                    self.label.text = 'Illegal surface'
                    self.label.visible = 1
                    return
            else:
                self.label.text = DVdisplay(self.flux)
                self.label.visible = 1
                return
        else:
            if self.measure == SURFACE:
                s = 'Qmonopole'
            else:
                s = 'I'
        if source > 0:
            info = '%s=+%d' % (s,source)
        elif source < 0:
            info = '%s=%d' % (s,source)
        else:
            info = '%s=0' % s
        self.label.text = info
        self.label.visible = 1

    def update(self):
        self.flux = 0
        for G in self.elements:
            p1 = G[0]
            p2 = G[1]
            points, dflux = Integralpoints(self.measure, p1, p2)
            self.flux += dflux
            G[2].pos = points
            if self.measure == LINE:
                Gcolor = color.red
                if dflux < 0:
                    Gcolor = color.blue
                G[2].color = Gcolor
        self.showsource()

    def Integral(self, p1, p2, final):
        newdir = norm(p2-p1)
        if self.flux is None:
            self.flux = 0
            initialdir = newdir
            self.curve.append(pos=p2+dz)
        else:
            olddir = self.curve.pos[-1]-self.curve.pos[-2]
            self.turning += turn(olddir,newdir)
            self.curve.append(pos=p2+dz)
            if final:
                # Calculate turning angle from last segment to first segment
                initdir = self.curve.pos[1]-self.curve.pos[0]
                self.turning += turn(newdir,initdir)
        points, dflux = Integralpoints(self.measure, p1,p2)
        self.flux += dflux
        if self.measure == SURFACE:
            Gcolor = FieldDrag.fcolor
        else:
            if mode == ELECTRIC: # display DV as we drag
                if dflux < 0:
                    Gcolor = color.red
                else:
                    Gcolor = color.blue
                self.label.pos = p2+offset
                self.label.text = DVdisplay(self.flux)
                self.label.visible = 1
            else:
                if dflux > 0:
                    Gcolor = color.red
                else:
                    Gcolor = color.blue
        self.elements.append((p1, p2,
            faces(pos=points, color=Gcolor, normal=[(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1)])))

    def visible(self, vis):
        self.curve.visible = vis
        self.label.visible = vis
        for el in self.elements:
            el[2].visible = vis
            
        
def CalcField(pos):
    field = vector(0,0,0)
    if mode == ELECTRIC:
        for Q in sources:
            r = pos-Q.pos
            if mag(r) > Q.radius:
                if dim == 3:
                    field += k*Q.source*norm(r)/mag(r)**2
                else:
                    field += k*Q.source*norm(r)/mag(r)
            else:
                return vector(0,0,0)
    else:
        for I in sources:
            r = pos-I.pos
            if mag(r) > I.radius:
                field += k*I.source*cross(vector(0,0,1),norm(r))/mag(r)
            else:
                return vector(0,0,0)
    return field

def DVdisplay(DV):
    if DV > 0:
        sign='-'
    else:
        sign='+'
    return 'DV = %s%0.1f' % (sign,-10*DV)

def FieldUpdate():
    for f in fields:
        if f[0] == VECTOR:
            f[1].axis = Escale*CalcField(f[1].pos)
        else:
            f[1].axis = norm(CalcField(f[1].pos))           
    for G in Gmeasures:
        G.update()
    
def Integralpoints(measuretype, p1, p2): # used for both SURFACE and LINE integrals
    # For LINE integrals, "flux" is actually dot(field,dl).
    field = CalcField(0.5*(p1+p2))
    if measuretype == SURFACE:
        G = Gscale*field
        if cross(G,p2-p1).z > 0:
            points = [p1, p1+G, p2+G, p1, p2+G, p2]
        else:
            points = [p1, p2+G, p1+G, p1, p2, p2+G]
        return (points, cross(field, p2-p1).z)
    else:
        Bdl = dot(field,p2-p1)
        if Bdl:
            A = Ascale*abs(Bdl/mag(p2-p1))
        else:
            A = 0
        rhat = norm(cross(p2-p1,vector(0,0,1)))
        points = [p1-A*rhat, p1+A*rhat, p2+A*rhat, p1-A*rhat, p2+A*rhat, p2-A*rhat]
        return (points, Bdl)

def GetMouseEvent(m):
    global drag, dragpos, initialpos, pick
    if m.events:
        m = scene.mouse.getevent()
        if m.click == 'left' and m.pick not in sources and m.pos.y < 7.4:
            pos = m.pos
            if constrain:
                pos = vector(round(m.pos.x),round(m.pos.y),round(m.pos.z))
            if measure == VECTOR or measure != UNITVECTOR:
                fields.append((VECTOR, arrow(pos=pos, axis=Escale*CalcField(pos),
                                    color=FieldDrag.color, shaftwidth=Eshaft)))
            elif measure == UNITVECTOR:
                fields.append((UNITVECTOR, arrow(pos=pos, axis=norm(CalcField(pos)),
                                    color=FieldDrag.color, shaftwidth=Eshaft)))
        elif m.drag == 'left':
            if m.pick in sources: # drag an existing source
                pick = m.pick
                drag = SOURCE
                dragpos = m.pickpos
                FieldDrag.axis = vector(0,0,0) # turn off FieldDrag while dragging source
            elif not m.pick:
                drag = measure
                pick = None
                dragpos = initialpos = m.pos
                if measure == LINE or measure == SURFACE:
                    Gmeasures.append(Gmeasure(dragpos))
            elif m.pick in [PosBox.icon, NegBox.icon]: # drag source out of storage box
                if m.pick is PosBox.icon:
                    PosBox.visible(0)
                    newq = q
                else:
                    NegBox.visible(0)
                    newq = -q
                createsource(m.pos, newq)
                pick = sources[-1]
                drag = SOURCE
                dragpos = m.pos
        elif m.drop: # finished dragging
            if drag == SOURCE:
                if PosBox.inbox(m.pos) or NegBox.inbox(m.pos): # dropped back into storage box
                    sources.remove(pick)
                    pick.visible = 0
                    del pick
                if constrain:
                    pick.pos = vector(round(pick.x),round(pick.y),round(pick.z))
                drag = None
                PosBox.visible(1)
                NegBox.visible(1)
                pick = None # dropped the source at a new location
                FieldUpdate() # make sure all fields correspond to final source position
                dragpos = None
            elif drag == VECTOR or drag == UNITVECTOR:
                # at end of showing E, leave an arrow at this location:
                pos = FieldDrag.pos
                if constrain:
                    pos = vector(round(FieldDrag.x),round(FieldDrag.y),round(FieldDrag.z))
                if drag == VECTOR:
                    fields.append((VECTOR, arrow(pos=pos, axis=Escale*CalcField(pos),
                                        color=FieldDrag.color, shaftwidth=Eshaft)))
                else:
                    fields.append((UNITVECTOR, arrow(pos=pos, axis=norm(CalcField(pos)),
                                        color=FieldDrag.color, shaftwidth=Eshaft)))                
                FieldDrag.axis = vector(0,0,0)
                drag = None
                dragpos = None
            elif drag == SURFACE or drag == LINE: # must complete the round trip if not DV measurement
                drag = None
                FieldDrag.axis = vector(0,0,0)
                if mode == ELECTRIC and measure == LINE: return # if measuring DV
                r = initialpos-dragpos
                nsteps = int((mag(r)/Gtolerance))+1
                dr = r/nsteps
                final = False
                for nn in range(nsteps):
                    if nn == nsteps-1:
                        final = True
                    Gmeasures[-1].Integral(dragpos,dragpos+dr,final)
                    dragpos = dragpos + dr # was += dr, which causes reference trouble
                Gmeasures[-1].showsource()
                dragpos = None

def Drag(m):
    global dragpos, drag
    if drag == SOURCE:
        pick.pos += m.pos-dragpos
        dragpos = pick.pos
        FieldUpdate()
    elif drag == VECTOR or drag == UNITVECTOR:
        FieldDrag.pos = m.pos
        if drag == VECTOR:
            FieldDrag.axis = Escale*CalcField(m.pos)
        else:
            FieldDrag.axis = norm(CalcField(m.pos))
        dragpos = m.pos
    elif drag == LINE or drag == SURFACE:
        if len(Gmeasures[-1].elements)>2 and (mag(m.pos-initialpos) <= Gtolerance):
            drag = None
            Gmeasures[-1].Integral(dragpos,initialpos,True)
            Gmeasures[-1].showsource()
            FieldDrag.axis = vector(0,0,0)
            dragpos = None
        elif mag(m.pos-dragpos) > Gtolerance:
            newpos = m.pos
            Gmeasures[-1].Integral(dragpos,newpos,False)
            dragpos = newpos
            FieldDrag.pos = newpos
            FieldDrag.axis = Escale*CalcField(newpos)

def turn(v1,v2):
    # angle to turn from vector v1 to v2
    # counterclockwise is positive
    c = dot(v1,v2)
    s = cross(v1,v2).z
    return atan2(s,c)

def createsource(newpos, newq):
    global sources
    if mode == ELECTRIC:
        if newq > 0:
            newcolor = Qpos
        else:
            newcolor = Qneg
    else:
        if newq > 0:
            newcolor = Ipos
        else:
            newcolor = Ineg
    if dim == 3:
        sources.append(sphere(pos=newpos, radius=rq, color=newcolor, source=newq))
    else:
        sources.append(cylinder(pos=newpos, axis=(0,0,rq), radius=rq, color=newcolor, source=newq))

class Grid(object):
    def __init__(self):
        self.points = []
        for x in range(-9,10):
            for y in range(-9,8):
                self.points.append(sphere(pos=(x,y), radius=0.05, color=color.black))

    def visible(self, vis):
        for s in self.points:
            s.visible = vis

def clearmeasures():
    global Gmeasures, fields
    for obj in fields:
        obj[1].visible = 0
    fields = []
    for obj in Gmeasures:
        obj.visible(0)
    Gmeasures = []

def clearall():
    global sources
    for obj in sources:
        obj.visible = 0
    sources = []
    clearmeasures()
    setmeasure(VECTOR)
    FieldDrag.axis = vector(0,0,0)
    FieldDrag.visible = 1

def setFielddragcolor():
    if mode == ELECTRIC:
        FieldDrag.color = Ecolor
        FieldDrag.fcolor = EFcolor
        FieldDrag.lcolor = color.cyan
    else:
        FieldDrag.color = Mcolor
        FieldDrag.fcolor = MFcolor
        FieldDrag.lcolor = color.yellow

def setdim():
    global dim
    scene.userspin = 0
    if bdim.value:
        if mode == MAGNETIC:
            bdim.value = 0
            return # can't toggle to 3D for magnetic fields
        dim = 3
        scene.userspin = 1
    else:
        dim = 2
        resetscene()
    PosBox.update()
    NegBox.update()
    setmode()
    clearall()

def setmode():
    global mode, dim
    if bmode.value:
        mode = MAGNETIC
        Title.text = 'Drag +z or -z current-carrying wire into scene.\nThen click or drag.'
        if dim == 3:
            dim = 2
            bdim.value = 0
            scene.userspin = 0
            resetscene()
    else:
        mode = ELECTRIC
        if dim == 3:
            Title.text = 'Drag positive or negative point charge into scene.\nThen click or drag. Rotate scene for 3D.'
            scene.userspin = 1
        else:
            Title.text = 'Drag positively or negatively charged long rod into scene.\nThen click or drag.'
            scene.userspin = 0
            resetscene()
    setupmeasuremenu()
    setFielddragcolor()
    PosBox.update()
    NegBox.update()
    clearall()

def setgrid():
    global grid
    if bgrid.value:
        if not grid:
            grid = Grid()
        else:
            grid.visible(1)
    else:
        grid.visible(0)

def setconstrain():
    global constrain
    constrain = bconstrain.value

def setscale(): # slider adjusts scaling of vectors
    global Escale, Gscale, Ascale
    newscale = bscale.value
    factor = newscale/Escale
    Escale *= factor
    Gscale *= factor
    Ascale *= factor
    FieldUpdate()

# em file format: title 'sources for fields version 1.0', then 'line charges' or 'point charges' or 'currents'
#   For each source, charge/current TAB x TAB y

def getsources():
    global sources, mode, dim
    fd = get_file(file_extensions='.em', x=200, y=200)
    if fd:
        data = fd.readlines()
    else:
        return
    
    sourcetype = data[1][:-1]
    clearall()
    if sourcetype == 'currents':
        mode = MAGNETIC
        bmode.value = 1
        if dim == 3:
            dim = 2
            bdim.value = 0
    else:
        mode = ELECTRIC
        bmode.value = 0
        if sourcetype == 'point charges':
            dim = 3
            bdim.value = 1
        else:
            dim = 2
            bdim.value = 0
    setmode()
    PosBox.update()
    NegBox.update()
    for line in data[2:]:
        nums = line.split()
        newq = float(nums[0])
        x = float(nums[1])
        y = float(nums[2])
        z = 0.0
        if len(nums) == 4:
            z = float(nums[3])
        newpos = vector(x,y,z)
        createsource(newpos,newq)        

def savesources():
    fd = save_file(file_extensions='.em', x=200, y=200)
    if not fd:
        return
    fd.write('sources for fields version 1.0\n')
    if mode == ELECTRIC:
        if dim == 2:
            sourcetype = 'line charges'
        else:
            sourcetype = 'point charges'
    else:
        sourcetype = 'currents'
    fd.write(sourcetype+'\n')
    for s in sources:
        fd.write('%g\t%0.5f\t%0.5f\t%0.5f\n' % (s.source,s.x,s.y,s.z))

# mm file format: title 'measures for fields version 1.0', then
#   For each measure, code TAB x TAB y, where code tells what kind of measure
#   code = 1 (field), 2 (unit vector field), 3 (potential), 4 (equipotential)

def getmeasures():
    global sources, mode, dim
    fd = get_file(file_extensions='.mm', x=200, y=200)
    if fd:
        data = fd.readlines()
    else:
        return
    
    for line in data[1:]:
        nums = line.split()
        measuretype = int(nums[0])
        x = float(nums[1])
        y = float(nums[2])
        z = 0.0
        if len(nums) == 4:
            z = float(nums[3])
        newpos = vector(x,y,z)
        if measuretype == VECTOR:
            fields.append((VECTOR, arrow(pos=newpos, axis=Escale*CalcField(newpos),
                                color=FieldDrag.color, shaftwidth=Eshaft)))
        elif measuretype == UNITVECTOR:
            fields.append((UNITVECTOR, arrow(pos=newpos, axis=norm(CalcField(newpos)),
                                color=FieldDrag.color, shaftwidth=Eshaft)))

def savemeasures():
    fd = save_file(file_extensions='.mm', x=200, y=200)
    fd.write('measures for fields version 1.0\n')
    for s in fields:
        fd.write('%d\t%0.5f\t%0.5f\t%0.5f\n' % (s[0],s[1].x,s[1].y,s[1].z))

def setupmeasuremenu():
    bmeasuremenu.items = []
    bmeasuremenu.items.append( ["Vector", lambda: setmeasure(VECTOR)] )
    bmeasuremenu.items.append( ["Unit vector", lambda: setmeasure(UNITVECTOR)] )
    if mode == ELECTRIC:
        bmeasuremenu.items.append( ["Potential", lambda: setmeasure(LINE)] )
    else:
        bmeasuremenu.items.append( ["Ampere's law", lambda: setmeasure(LINE)] )
    if dim == 2:
        bmeasuremenu.items.append( ["Gauss's law", lambda: setmeasure(SURFACE)] )
    setmeasure(measure)

def setmeasure(measuretype):
    global measure
    for item in bmeasuremenu.items:
        if item[0][0] == '*':
            item[0] = item[0][1:]
    if measuretype == VECTOR:
        bmeasuremenu.items[0][0] = '*'+bmeasuremenu.items[0][0]
    elif measuretype == UNITVECTOR:
        bmeasuremenu.items[1][0] = '*'+bmeasuremenu.items[1][0]
    elif measuretype == LINE:
        bmeasuremenu.items[2][0] = '*'+bmeasuremenu.items[2][0]
    elif measuretype == SURFACE and len(bmeasuremenu.items) == 4:
        bmeasuremenu.items[3][0] = '*'+bmeasuremenu.items[3][0]
    measure = measuretype

gotfile = None

def select_file(m):
    global gotfile
    # It would be better to use m.value, introduced with Visual 5.
    # Using nitem however is compatible with Visual 3.
    gotfile = m.nitem

def getfile(extensions=None, x=0, y=0, title='Choose a file'): # currently shows no more than 25 files
    global gotfile
    gotfile = None
    if extensions is not None:
        if not isinstance(extensions, (list,tuple)):
            extensions = [extensions]
    allfiles = os.listdir(os.curdir)
    files = []
    nfiles = 0
    for f in allfiles:
        if extensions is None:
            files.append(f)
            nfiles += 1
        else:
            period = f.rfind('.')
            if period:
                if f[period:] in extensions:
                    files.append(f)
                    nfiles += 1
        if nfiles >= 25: break
    hitem = 20 # pixel height of each menu listing
    hcanvas = hitem*(len(files)+1) # approx height without title bar
    winwidth = 300
    winheight = 30+hcanvas # allow 30 pixels for title bar
    fcontrol = controls(x=x, y=y, background=color.white, width=winwidth,
                        height=winheight, title=title)
    fcontrol.display.exit = False
    if winwidth >= winheight:
        hmenu = 200*hitem/winwidth
        y = 100*hcanvas/winwidth-hmenu/2
    else:
        hmenu = 200*hitem/hcanvas
        y = 100-hmenu/2
    m = menu(text="Choose File", width=200, height=hmenu,
             pos=(0,y,0))
    for f in files:
        m.items.append((f, lambda : select_file(m)))
    while fcontrol.display.visible and not gotfile:
        rate(10)
        fcontrol.interact()
    if gotfile:
        gotfile = m.items[m.nitem-1][0]
    fcontrol.display.visible = 0
    del fcontrol.display

def getname(title='Type the name of the new file'): # accept typed input to use as file name
    currentdisplay = display.get_selected()
    disp = display(title=title, background=color.white, foreground=color.black,
                   x=200, y=200, width=300, height=70, exit=0)
    prose = label(opacity=0, box=0) # initially blank text
    while disp.visible:
        if disp.kb.keys: # event waiting to be processed?
            s = disp.kb.getkey() # get keyboard info
            if s == '\n':
                break
            elif len(s) == 1:
                prose.text += s # append new character
            elif ((s == 'backspace' or s == 'delete') and
                    len(prose.text)) > 0:
                prose.text = prose.text[:-1] # erase letter
            elif s == 'shift+delete':
                prose.text = '' # erase all text
    if disp.visible:
        name = prose.text
    else:
        name = None
    disp.visible = 0
    del disp
    currentdisplay.select()
    return name
        
FieldDrag = arrow(axis=(0,0,0), shaftwidth=Eshaft) # for dragging field arrow
setFielddragcolor()
PosBox = ChargeBox(vector(-9,8.5), 1)
NegBox = ChargeBox(vector(9,8.5), -1)
Title = label(pos=(0,8.25), opacity=1)
grid = None
root = None
            
c = controls(x=wscene, y=0, width=1024-wscene, height=hscene)

c.display.background = color.white
c.display.foreground = color.black
bmode = toggle(pos=(-35,80), height=12, width=10, action=lambda: setmode(),
               text0='Electric', text1='Magnetic')
bdim = toggle(pos=(-10,80), height=12, width=10, action=lambda: setdim(),
               text0='2D', text1='3D')
bgrid = toggle(pos=(10,80), height=12, width=10, action=lambda: setgrid(),
               text1='Grid')
bconstrain = toggle(pos=(35,80), height=12, width=10, action=lambda: setconstrain(),
               text1='Constrain')
bclearmeasures = button(pos=(-15,40), height=30, width=30, action=lambda: clearmeasures(),
                text='Clear', color=color.red)
bclearall = button(pos=(27,40), height=30, width=30, action=lambda: clearall(),
                   text='Delete', color=color.red)

bscale = slider(pos=(-40,-60), axis=(0,120,0), min=1, max=50, width=5, action=lambda: setscale() )
label(display=c.display, pos=(-27,-65), text='Field scale factor', opacity=0, box=0)
bscale.value = Escale

bresetscene = button(pos=(10,-40), height=20, width=40, action=lambda: resetscene(),
                     text='Reset scene', color=color.red)

bfilemenu = menu(pos=(27,10), height=8, width=38, text='Read/write files')
bfilemenu.items.append( ('Get sources', lambda: getsources()) )
bfilemenu.items.append( ('Get measures', lambda: getmeasures()) )
bfilemenu.items.append( ('Save sources', lambda: savesources()) )
bfilemenu.items.append( ('Save measures', lambda: savemeasures()) )

bmeasuremenu = menu(pos=(-15,10), height=8, width=33, text='Measure type')
setupmeasuremenu()
label(display=c.display, pos=(0,-85), text='See detailed instructions in shell window', opacity=0, box=0)
setmode()
dragpos = None

while 1:
    rate(400)
    c.interact()
    m = scene.mouse
    GetMouseEvent(m)
    if dragpos and (m.pos != dragpos):
        Drag(m)