import matplotlib
from Tkinter import *
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.widgets import Slider

class PlotWidget( Frame ):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.figure = Figure(figsize=(5,4), dpi=75)
        self.canvas = FigureCanvasTkAgg(self.figure, self)

        self.frame = self.canvas.get_tk_widget()
        self.frame.pack(side=TOP, fill=BOTH, expand=1)
        self.canvas.show()

    def add_slider(self):
       a = self.figure.add_axes([0.25, 0.1, 0.65, 0.03], axisbg='lightgoldenrodyellow')
       s = Slider( a, 'range', 0.1, 30.0, valinit=5)
       self.canvas.show()



root = Tk()

option = 1

if option == 1 or option == 2:
     w =  PlotWidget(root)
     w.pack()
     figure = w.figure
else:
     f = Frame(root, bd = 6, bg='red')
     figure = matplotlib.figure.Figure(figsize=(5,4), dpi=75)
     canvas = FigureCanvasTkAgg(figure, f)
     canvas.get_tk_widget().pack()
     canvas.show()
     f.pack()


if option == 1:
    w.add_slider()
else:
    a = figure.add_axes([0.25, 0.1, 0.65, 0.03], axisbg='lightgoldenrodyellow')   
    s = Slider( a, 'range', 0.1, 30.0, valinit=5)

root.mainloop()