from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("Calculator")

window.geometry('500x500')

Label(window, text="Термометры сопротивления", font=("Arial Bold", 15)) \
    .grid(row=0, column=1, columnspan=2, pady=10)

combo = Combobox(window, width=35)

combo['values'] = (
    "Выберите тип термопапары:", "Платиновые ТС и ЧЭ, α = 0,00385 °С-1", "Платиновые ТС и ЧЭ, α = 0,00391 °С-1",
    "Медные ТС и ЧЭ, α = 0,00428 °С-1", "Никелевые ТС и ЧЭ, α = 0,00617 °С-1")

combo.current(0)
combo.grid(row=1, column=1, columnspan=2, pady=20)

Label(window, text="Температура:", font=("Arial Bold", 10)) \
    .grid(row=2, column=0, pady=20)

txt_tempetature = Entry(window, width=10)

txt_tempetature.grid(row=2, column=1, pady=20)

Label(window, text="Сопротивление при 0:", font=("Arial Bold", 10)) \
    .grid(row=3, column=0, pady=20)

zero_resist = Entry(window, width=10)
zero_resist.grid(row=3, column=1, pady=20)

Label(window, text="Сопротивление темпопреобр.", font=("Arial Bold", 10)) \
    .grid(row=4, column=0, pady=20)

resist = Entry(window, width=10)

resist.grid(row=4, column=1, pady=20)

Label(window, text="Результат:", font=("Arial Bold", 10)) \
    .grid(row=5, column=0, pady=20)

result = Entry(window, width=10)

result.grid(row=5, column=1, pady=20, columnspan=2)

window.mainloop()
