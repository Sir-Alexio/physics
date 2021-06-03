from tkinter import *
from tkinter.ttk import Combobox

import Calculator

calculator = Calculator.Calculator()

calculator.get_window().title("Calculator")
calculator.get_window().geometry('800x500')

calculator.paint_button(calculator.get_temperature_resist_button(), 0, 1)
calculator.paint_button(calculator.get_termopara_button(), 0, 2)

calculator.get_termopara_button().bind('<Button-1>', calculator.make_frame_termopara)
calculator.get_temperature_resist_button().bind('<Button-1>', calculator.make_frame_temperature_resist)

calculator.get_resul_button().bind('<Button-1>', calculator.calculate)

calculator.get_exit_button().bind('<Button-1>', calculator.exit)

calculator.get_window().mainloop()
