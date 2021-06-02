from tkinter import *
from tkinter.ttk import Combobox

import math


def print_result(result):
    Label(window, text=('%.2f' % result), font=("Arial Bold", 15), width=25) \
        .grid(row=5, column=1, pady=20)


def function(a, b, c, d, x):
    return a + b * int(x.get()) + c * math.pow(int(x.get()), 2) + d * math.pow(int(x.get()), 3)


def make_choice_temperature(event):
    if not electric_force.get():
        if combo.get() == "Тип термопары L":

            a = 0.13355
            b = 0.0623
            c = 5.43 * 10e-5
            d = -3.61 * 10e-8

            print_result(function(a, b, c, d, txt_tempetature))
        elif combo.get() == "Тип термопары S":

            a = 10.9408
            b = 129.71771
            c = -3.66195
            d = 0.09393

            print_result(function(a, b, c, d, txt_tempetature))
        elif combo.get() == "Тип термопары M":

            a = 0.46739
            b = 22.65393
            c = -0.78186
            d = 0.11786

            print_result(function(a, b, c, d, txt_tempetature))
        elif combo.get() == "Тип термопары N":

            a = -18.90302
            b = 39.20541
            c = -0.57067
            d = 0.0071

            print_result(function(a, b, c, d, txt_tempetature))
        elif combo.get() == "Тип термопары K":

            a = -15.78005
            b = 28.48037
            c = -0.22017
            d = 0.003

            print_result(function(a, b, c, d, txt_tempetature))
        elif combo.get() == "Тип термопары R":

            a = 15.24549
            b = 123.03099
            c = -3.64165
            d = 0.08343

            print_result(function(a, b, c, d, txt_tempetature))
        elif combo.get() == "Тип термопары T":

            a = 0.69421
            b = 29.25358
            c = -1.11665
            d = 0.03168

            print_result(function(a, b, c, d, txt_tempetature))
        elif combo.get() == "Тип термопары B":

            a = 146.44839
            b = 272.34942
            c = -22.77337
            d = 0.87502

            print_result(function(a, b, c, d, txt_tempetature))
        elif combo.get() == "Тип термопары E":

            a = -16.15782
            b = 18.35188
            c = -0.1646
            d = 0.00133

            print_result(function(a, b, c, d, txt_tempetature))
        elif combo.get() == "Тип термопары J":

            a = -9.00789
            b = 20.70519
            c = -0.09652
            d = 6.9624E-4

            print_result(function(a, b, c, d, txt_tempetature))
        elif combo.get() == "Тип термопары A-1/A-2/A-3":

            a = 5.9579
            b = 68.84126
            c = -1.00607
            d = 0.03415

            print_result(function(a, b, c, d, txt_tempetature))

    elif not txt_tempetature.get():
        if combo.get() == "Тип термопары L":

            a1 = 0.13355
            b1 = 0.0623
            c1 = 5.42674E-5
            d1 = -3.6148E-8

            print_result(function(a1, b1, c1, d1, electric_force))
        elif combo.get() == "Тип термопары S":

            a1 = -0.0265
            b1 = 0.00684
            c1 = 3.64777E-6
            d1 = -8.54455E-10

            print_result(function(a1, b1, c1, d1, electric_force))
        elif combo.get() == "Тип термопары M":

            a1 = 2.02568E-6
            b1 = 0.04264
            c1 = 5.03527E-5
            d1 = -4.9441E-8

            print_result(function(a1, b1, c1, d1, electric_force))
        elif combo.get() == "Тип термопары N":

            a1 = 0.15603
            b1 = 0.02522
            c1 = 1.96738E-5
            d1 = -8.63967E-9

            print_result(function(a1, b1, c1, d1, electric_force))
        elif combo.get() == "Тип термопары K":

            a1 = 0.45636
            b1 = 0.0353
            c1 = 1.31371E-5
            d1 = -7.41683E-9

            print_result(function(a1, b1, c1, d1, electric_force))
        elif combo.get() == "Тип термопары R":

            a1 = -0.02656
            b1 = 0.00674
            c1 = 4.91809E-6
            d1 = -1.10375E-9

            print_result(function(a1, b1, c1, d1, electric_force))
        elif combo.get() == "Тип термопары T":

            a1 = -0.02123
            b1 = 0.03847
            c1 = 4.70201E-5
            d1 = -3.22231E-8

            print_result(function(a1, b1, c1, d1, electric_force))
        elif combo.get() == "Тип термопары B":

            a1 = 0.03346
            b1 = -5.75046E-4
            c1 = 6.4871E-6
            d1 = -1.09397E-9

            print_result(function(a1, b1, c1, d1, electric_force))
        elif combo.get() == "Тип термопары E":

            a1 = 0.28466
            b1 = 0.0564
            c1 = 4.80952E-5
            d1 = -2.90413E-8

            print_result(function(a1, b1, c1, d1, electric_force))
        elif combo.get() == "Тип термопары J":

            a1 = 0.34739
            b1 = 0.04808
            c1 = 1.52514E-5
            d1 = -5.93024E-9

            print_result(function(a1, b1, c1, d1, electric_force))
        elif combo.get() == "Тип термопары A-1/A-2/A-3":

            a1 = -0.40884
            b1 = 0.01686
            c1 = 2.17244E-7
            d1 = -6.14901E-10

            print_result(function(a1, b1, c1, d1, electric_force))


def make_choice_resist(event):
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
# -----------------------------------------------------------------------------------------------------------------------
title_combo.current(1)  # изменить тип калькулятора: 0 - термометры сопротивления, 1 - термопары
# -----------------------------------------------------------------------------------------------------------------------
title_combo.grid(row=0, column=1, pady=20)

if title_combo.get() == "Термометры сопротивления":
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
    result_button.bind('<Button-1>', make_choice_resist)

    i.set(0)
    j.set(0)
    k.set(0)
else:
    combo = Combobox(window, width=40)
    combo['values'] = ("Выберите тип термопары",
                       "Тип термопары L", "Тип термопары S", "Тип термопары M",
                       "Тип термопары N", "Тип термопары K", "Тип термопары R",
                       "Тип термопары T", "Тип термопары B", "Тип термопары E",
                       "Тип термопары J", "Тип термопары A-1/A-2/A-3")
    combo.current(0)
    combo.grid(row=1, column=1, columnspan=2, pady=20)

    lbl = Label(window, text="Температура:", font=("Arial Bold", 10)) \
        .grid(row=2, column=0, pady=20)

    txt_tempetature = Entry(window, width=10)
    txt_tempetature.grid(row=2, column=1, pady=20)

    Label(window, text="Температура окружающей среды", font=("Arial Bold", 10)) \
        .grid(row=3, column=0, pady=20)

    outside_temperature = Entry(window, width=10)
    outside_temperature.grid(row=3, column=1, pady=20)

    Label(window, text="Термо-ЭДС", font=("Arial Bold", 10)) \
        .grid(row=4, column=0, pady=20)

    electric_force = Entry(window, width=10)

    electric_force.grid(row=4, column=1, pady=20)

    Label(window, text="Результат:", font=("Arial Bold", 10)) \
        .grid(row=5, column=0, pady=20)

    result_button = Button(window, text="Расчитать")

    result_button.grid(column=1, row=6)

    result_button.bind('<Button-1>', make_choice_temperature)

window.mainloop()
