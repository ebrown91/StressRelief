#run gui
#run prompt for size, chromium content, and heat number
from GUI import *

def app():

    gui_window = Gui()
    gui_window.launch()

    dpg.start_dearpygui()


app()



