import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import graph
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import random


temp = True;
sounds = False;

fig1 = graph.fig
matplotlib.use("TkAgg")



def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

# Define the window layout
layout = [
    [sg.Text("Current Location")],
    [sg.Canvas(key="-CANVAS-"),sg.Output(size=(30,10), key='-OUTPUT-')],
    [sg.OK(), sg.Cancel()]

]

# Create the form and show it without the plot
window = sg.Window(
    "Matplotlib Single Graph",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
)

# Add the plot to the window
ani = animation.FuncAnimation(graph.fig, graph.animate, interval=1000)
draw_figure(window["-CANVAS-"].TKCanvas, fig1)

event, values = window.read()
window.close()