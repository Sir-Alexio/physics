from tkinter import *
from tkinter.ttk import Combobox

import math


def print_result(result):
    Label(window, text=str(result), font=("Arial Bold", 15)) \
        .grid(row=5, column=1, pady=20)


def make_choice(event):
    if combo.get() == "Платиновые ТС и ЧЭ, α = 0,00385 °С-1":

        a = 3.9083 * 10e-4
        b = -5.775 * 10e-9
        c = -4.183 * 10e-16

        if -200 <= int(txt_tempetature.get()) < 0:

            result = float(zero_Resist.get()) * (
                    1 + a * int(txt_tempetature.get()) + b * math.pow(int(txt_tempetature.get()), 2) + c * (
                    int(txt_tempetature.get()) - 100) * math.pow(
                int(txt_tempetature.get()), 3))

            print_result(result)

        elif 0 <= int(txt_tempetature.get()) <= 850:

            result = float(zero_Resist.get()) * (
                    1 + a * int(txt_tempetature.get()) + b * math.pow(int(txt_tempetature.get()), 2))

            print_result(result)

    elif combo.get() == "Платиновые ТС и ЧЭ, α = 0,00391 °С-1":

        a = 3.9690 * 10e-4
        b = -5.841 * 10e-9
        c = -4.330 * 10e-16

        if -200 <= int(txt_tempetature.get()) < 0:

            result = float(zero_Resist.get()) * (
                    1 + a * int(txt_tempetature.get()) + b * math.pow(int(txt_tempetature.get()), 2) + c * (
                    int(txt_tempetature.get()) - 100) * math.pow(
                int(txt_tempetature.get()), 3))

            print_result(result)

        elif 0 < int(txt_tempetature.get()) <= 850:

            result = float(zero_Resist.get()) * (
                    1 + a * int(txt_tempetature.get()) + b * math.pow(int(txt_tempetature.get()), 2))

            print_result(result)

    elif combo.get() == "Медные ТС и ЧЭ, α = 0,00428 °С-1":

        a = 4.28 * 10e-4
        b = -6.2032 * 10e-9
        c = 8.5154 * 10e-13

        if -180 <= int(txt_tempetature.get()) < 0:

            result = float(zero_Resist.get()) * (
                    1 + a * int(txt_tempetature.get()) + b * int(txt_tempetature.get()) * (
                    int(txt_tempetature.get()) + 6.7) + c * math.pow(
                int(txt_tempetature.get()), 3))

            print_result(result)

        elif 0 < int(txt_tempetature.get()) <= 200:

            result = float(zero_Resist.get()) * (1 + a * int(txt_tempetature.get()))

            print_result(result)

    elif combo.get() == "Никелевые ТС и ЧЭ, α = 0,00617 °С-1":

        a = 5.4963 * 10e-4
        b = 6.7556 * 10e-7
        c = 9.2004 * 10e-12

        if -60 <= int(txt_tempetature.get()) < 100:

            result = float(zero_Resist.get()) * (
                    1 + a * int(txt_tempetature.get()) + b * math.pow(int(txt_tempetature.get()), 2))

            print_result(result)

        elif 100 < int(txt_tempetature.get()) <= 180:

            result = float(zero_Resist.get()) * (
                    1 + a * int(txt_tempetature.get()) + b * math.pow(int(txt_tempetature.get()), 2) + c * math.pow(
                int(txt_tempetature.get()), 2) * (
                            int(txt_tempetature.get()) - 100))
            print_result(result)


window = Tk()
window.title("Calculator")

window.geometry('800x500')

title_combo = Combobox(window, width=35, font=("Arial Bold", 15))
title_combo['values'] = ("Термометры сопротивления", "Термопары")
title_combo.current(1)
title_combo.grid(row=0, column=1, pady=20)

if title_combo.get() == "Термометры сопротивления":
    combo = Combobox(window, width=35 )
    combo['values'] = (
        "Выберите тип термопапары:", "Платиновые ТС и ЧЭ, α = 0,00385 °С-1", "Платиновые ТС и ЧЭ, α = 0,00391 °С-1",
        "Медные ТС и ЧЭ, α = 0,00428 °С-1", "Никелевые ТС и ЧЭ, α = 0,00617 °С-1")
    combo.current(0)

    combo.grid(row=1, column=1, columnspan=2, pady=20)
    Label(window, text="Температура:", font=("Arial Bold", 10)) \
        .grid(row=2, column=0, pady=20)
    i = IntVar()
    txt_tempetature = Entry(window, width=10, text=i)
    txt_tempetature.grid(row=2, column=1, pady=20)

    Label(window, text="Сопротивление при 0:", font=("Arial Bold", 10)) \
        .grid(row=3, column=0, pady=20)
    j = IntVar()
    zero_Resist = Entry(window, width=10, text=j)
    zero_Resist.grid(row=3, column=1, pady=20)

    Label(window, text="Сопротивление темпопреобр.", font=("Arial Bold", 10)) \
        .grid(row=4, column=0, pady=20)
    k = IntVar()
    resist = Entry(window, width=10, text=k)

    resist.grid(row=4, column=1, pady=20)

    Label(window, text="Результат:", font=("Arial Bold", 10)) \
        .grid(row=5, column=0, pady=20)

    result_button = Button(window, text="Расчитать")

    result_button.grid(column=1, row=6)
    print(combo.get())
    result_button.bind('<Button-1>', make_choice)

    i.set(0)
    j.set(0)
    k.set(0)
else:
    combo = Combobox(window, width=35)
    combo['values'] = (
        "Выберите тип термопапары:", "Платиновые ТС и ЧЭ, α = 0,00385 °С-1", "Платиновые ТС и ЧЭ, α = 0,00391 °С-1",
        "Медные ТС и ЧЭ, α = 0,00428 °С-1", "Никелевые ТС и ЧЭ, α = 0,00617 °С-1")
    combo.current(0)

    combo.grid(row=1, column=1, columnspan=2, pady=20)
    Label(window, text="Температура:", font=("Arial Bold", 10)) \
        .grid(row=2, column=0, pady=20)
    i = IntVar()
    txt_tempetature = Entry(window, width=10, text=i)
    txt_tempetature.grid(row=2, column=1, pady=20)

    Label(window, text="Сопротивление при 0:", font=("Arial Bold", 10)) \
        .grid(row=3, column=0, pady=20)
    j = IntVar()
    zero_Resist = Entry(window, width=10, text=j)
    zero_Resist.grid(row=3, column=1, pady=20)

    Label(window, text="Сопротивление темпопреобр.", font=("Arial Bold", 10)) \
        .grid(row=4, column=0, pady=20)
    k = IntVar()
    resist = Entry(window, width=10, text=k)

    resist.grid(row=4, column=1, pady=20)

    Label(window, text="Результат:", font=("Arial Bold", 10)) \
        .grid(row=5, column=0, pady=20)

    result_button = Button(window, text="Расчитать")

    result_button.grid(column=1, row=6)
    print(combo.get())
    result_button.bind('<Button-1>', make_choice)

    i.set(0)
    j.set(0)
    k.set(0)


window.mainloop()
