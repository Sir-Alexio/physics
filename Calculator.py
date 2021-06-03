from tkinter import *
from tkinter.ttk import Combobox

import math


class Calculator:
    def __init__(self):
        self.__window = Tk()
        self.__temperature_resist_button = Button(self.__window, text="Термометры сопротивления")
        self.__termopara_button = Button(self.__window, text="Термопары")
        self.__frame = Frame(self.__window, width=800, height=400)
        self.__combo = Combobox(self.__frame, width=40)
        self.__txt_temperature = Entry(self.__frame, width=10)
        self.__electric_force = Entry(self.__frame, width=10)
        self.__result_button = Button(self.__frame, text="Расчитать")
        self.__zero_resist = Entry(self.__frame, width=10)
        self.__resist = Entry(self.__frame, width=10)
        self.__result_button = Button(self.__frame, text="Расчитать")
        self.__exit_button = Button(self.__window, text="Выход")
        self.__result = 0
        self.__is_termopara = False
        self.__is_temperature_resist = False
        self.__flag = True

    def get_window(self):
        return self.__window

    def get_temperature_resist_button(self):
        return self.__temperature_resist_button

    def get_termopara_button(self):
        return self.__termopara_button

    def get_resul_button(self):
        return self.__result_button

    def get_exit_button(self):
        return self.__exit_button

    def exit(self, event):
        self.__window.destroy()

    def function(self, a, b, c, d, x):
        return a + b * int(x.get()) + c * math.pow(int(x.get()), 2) + d * math.pow(int(x.get()), 3)

    def print_result(self):
        Label(self.__frame, text=('%.2f' % self.__result), font=("Arial Bold", 15), width=25) \
            .grid(row=5, column=1, pady=20)

    def calculate(self, event):
        if self.__is_temperature_resist:
            if self.__combo.get() == "Платиновые ТС и ЧЭ, α = 0,00385 °С-1":

                a = 3.9083 * 10e-4
                b = -5.775 * 10e-9
                c = -4.183 * 10e-16

                if -200 <= int(self.__txt_temperature.get()) < 0:

                    self.__result = float(self.__zero_resist.get()) * (
                            1 + a * int(self.__txt_temperature.get().get()) + b * math.pow(
                        int(self.__txt_temperature.get().get()), 2) + c * (
                                    int(self.__txt_temperature.get().get()) - 100) * math.pow(
                        int(self.__txt_temperature.get().get()), 3))

                    self.print_result()

                elif 0 <= int(self.__txt_temperature.get()) <= 850:

                    self.__result = float(self.__zero_resist.get()) * (
                            1 + a * int(self.__txt_temperature.get()) + b * math.pow(int(self.__txt_temperature.get()),
                                                                                     2))

                    self.print_result()
            elif self.__combo.get() == "Платиновые ТС и ЧЭ, α = 0,00391 °С-1":

                a = 3.9690 * 10e-4
                b = -5.841 * 10e-9
                c = -4.330 * 10e-16

                if -200 <= int(self.__txt_temperature.get()) < 0:

                    self.__result = float(self.__zero_resist.get()) * (
                            1 + a * int(self.__txt_temperature.get()) + b * math.pow(int(self.__txt_temperature.get()),
                                                                                     2) + c * (
                                    int(self.__txt_temperature.get()) - 100) * math.pow(
                        int(self.__txt_temperature.get()), 3))

                    self.print_result()

                elif 0 < int(self.__txt_temperature.get()) <= 850:

                    self.__result = float(self.__zero_resist.get()) * (
                            1 + a * int(self.__txt_temperature.get()) + b * math.pow(int(self.__txt_temperature.get()),
                                                                                     2))

                    self.print_result()
            elif self.__combo.get() == "Медные ТС и ЧЭ, α = 0,00428 °С-1":

                a = 4.28 * 10e-4
                b = -6.2032 * 10e-9
                c = 8.5154 * 10e-13

                if -180 <= int(self.__txt_temperature.get()) < 0:

                    self.__result = float(self.__zero_resist.get()) * (
                            1 + a * int(self.__txt_temperature.get()) + b * int(self.__txt_temperature.get()) * (
                            int(self.__txt_temperature.get()) + 6.7) + c * math.pow(
                        int(self.__txt_temperature.get()), 3))

                    self.print_result()

                elif 0 < int(self.__txt_temperature.get()) <= 200:

                    self.__result = float(self.__zero_resist.get()) * (1 + a * int(self.__txt_temperature.get()))

                    self.print_result()
            elif self.__combo.get() == "Никелевые ТС и ЧЭ, α = 0,00617 °С-1":

                a = 5.4963 * 10e-4
                b = 6.7556 * 10e-7
                c = 9.2004 * 10e-12

                if -60 <= int(self.__txt_temperature.get()) < 100:

                    self.__result = float(self.__zero_resist.get()) * (
                            1 + a * int(self.__txt_temperature.get()) + b * math.pow(int(self.__txt_temperature.get()),
                                                                                     2))

                    self.print_result()

                elif 100 < int(self.__txt_temperature.get()) <= 180:

                    self.__result = float(self.__zero_resist.get()) * (
                            1 + a * int(self.__txt_temperature.get()) + b * math.pow(int(self.__txt_temperature.get()),
                                                                                     2) + c * math.pow(
                        int(self.__txt_temperature.get()), 2) * (
                                    int(self.__txt_temperature.get()) - 100))
                    self.print_result()
        elif self.__is_termopara:
            if not self.__electric_force.get():
                if self.__combo.get() == "Тип термопары L":

                    a = 0.13355
                    b = 0.0623
                    c = 5.43 * 10e-5
                    d = -3.61 * 10e-8
                    self.__result = self.function(a,b,c,d,self.__txt_temperature)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары S":

                    a = 10.9408
                    b = 129.71771
                    c = -3.66195
                    d = 0.09393

                    self.__result = self.function(a, b, c, d, self.__txt_temperature)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары M":

                    a = 0.46739
                    b = 22.65393
                    c = -0.78186
                    d = 0.11786

                    self.__result = self.function(a, b, c, d, self.__txt_temperature)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары N":

                    a = -18.90302
                    b = 39.20541
                    c = -0.57067
                    d = 0.0071

                    self.__result = self.function(a, b, c, d, self.__txt_temperature)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары K":

                    a = -15.78005
                    b = 28.48037
                    c = -0.22017
                    d = 0.003

                    self.__result = self.function(a, b, c, d, self.__txt_temperature)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары R":

                    a = 15.24549
                    b = 123.03099
                    c = -3.64165
                    d = 0.08343

                    self.__result = self.function(a, b, c, d, self.__txt_temperature)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары T":

                    a = 0.69421
                    b = 29.25358
                    c = -1.11665
                    d = 0.03168

                    self.__result = self.function(a, b, c, d, self.__txt_temperature)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары B":

                    a = 146.44839
                    b = 272.34942
                    c = -22.77337
                    d = 0.87502

                    self.__result = self.function(a, b, c, d, self.__txt_temperature)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары E":

                    a = -16.15782
                    b = 18.35188
                    c = -0.1646
                    d = 0.00133

                    self.__result = self.function(a, b, c, d, self.__txt_temperature)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары J":

                    a = -9.00789
                    b = 20.70519
                    c = -0.09652
                    d = 6.9624E-4

                    self.__result = self.function(a, b, c, d, self.__txt_temperature)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары A-1/A-2/A-3":

                    a = 5.9579
                    b = 68.84126
                    c = -1.00607
                    d = 0.03415

                    self.__result = self.function(a, b, c, d, self.__txt_temperature)
                    self.print_result()

            elif not self.__txt_temperature.get():
                if self.__combo.get() == "Тип термопары L":

                    a1 = 0.13355
                    b1 = 0.0623
                    c1 = 5.42674E-5
                    d1 = -3.6148E-8

                    self.__result = self.function(a1, b1, c1, d1, self.__electric_force)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары S":

                    a1 = -0.0265
                    b1 = 0.00684
                    c1 = 3.64777E-6
                    d1 = -8.54455E-10

                    self.__result = self.function(a1, b1, c1, d1, self.__electric_force)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары M":

                    a1 = 2.02568E-6
                    b1 = 0.04264
                    c1 = 5.03527E-5
                    d1 = -4.9441E-8

                    self.__result = self.function(a1, b1, c1, d1, self.__electric_force)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары N":

                    a1 = 0.15603
                    b1 = 0.02522
                    c1 = 1.96738E-5
                    d1 = -8.63967E-9

                    self.__result = self.function(a1, b1, c1, d1, self.__electric_force)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары K":

                    a1 = 0.45636
                    b1 = 0.0353
                    c1 = 1.31371E-5
                    d1 = -7.41683E-9

                    self.__result = self.function(a1, b1, c1, d1, self.__electric_force)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары R":

                    a1 = -0.02656
                    b1 = 0.00674
                    c1 = 4.91809E-6
                    d1 = -1.10375E-9

                    self.__result = self.function(a1, b1, c1, d1, self.__electric_force)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары T":

                    a1 = -0.02123
                    b1 = 0.03847
                    c1 = 4.70201E-5
                    d1 = -3.22231E-8

                    self.__result = self.function(a1, b1, c1, d1, self.__electric_force)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары B":

                    a1 = 0.03346
                    b1 = -5.75046E-4
                    c1 = 6.4871E-6
                    d1 = -1.09397E-9

                    self.__result = self.function(a1, b1, c1, d1, self.__electric_force)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары E":

                    a1 = 0.28466
                    b1 = 0.0564
                    c1 = 4.80952E-5
                    d1 = -2.90413E-8

                    self.__result = self.function(a1, b1, c1, d1, self.__electric_force)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары J":

                    a1 = 0.34739
                    b1 = 0.04808
                    c1 = 1.52514E-5
                    d1 = -5.93024E-9

                    self.__result = self.function(a1, b1, c1, d1, self.__electric_force)
                    self.print_result()
                elif self.__combo.get() == "Тип термопары A-1/A-2/A-3":

                    a1 = -0.40884
                    b1 = 0.01686
                    c1 = 2.17244E-7
                    d1 = -6.14901E-10

                    self.__result = self.function(a1, b1, c1, d1, self.__electric_force)
                    self.print_result()

    def paint_button(self, button, row, column):
        button.pack()

    def make_frame_temperature_resist(self, event):

        if self.__flag:
            #self.__frame = Frame(self.__window, width=800, height=400)
            self.__combo['values'] = (
                "Выберите тип термопапары:", "Платиновые ТС и ЧЭ, α = 0,00385 °С-1",
                "Платиновые ТС и ЧЭ, α = 0,00391 °С-1",
                "Медные ТС и ЧЭ, α = 0,00428 °С-1", "Никелевые ТС и ЧЭ, α = 0,00617 °С-1")
            self.__combo.current(0)

            self.__combo.grid(row=1, column=1, columnspan=2, pady=20)
            Label(self.__frame, text="Температура:", font=("Arial Bold", 10)) \
                .grid(row=2, column=0, pady=20)

            self.__txt_temperature.grid(row=2, column=1, pady=20)

            Label(self.__frame, text="Сопротивление при 0:", font=("Arial Bold", 10)) \
                .grid(row=3, column=0, pady=20)

            self.__zero_resist.grid(row=3, column=1, pady=20)

            Label(self.__frame, text="Сопротивление темпопреобр.", font=("Arial Bold", 10)) \
                .grid(row=4, column=0, pady=20)

            self.__resist.grid(row=4, column=1, pady=20)

            Label(self.__frame, text="Результат:", font=("Arial Bold", 10)) \
                .grid(row=5, column=0, pady=20)
            self.__result_button.grid(column=1, row=6)
            self.__frame.pack()
            self.__exit_button.pack(pady=20)
            self.__flag = False
            self.__is_temperature_resist = True
            self.__termopara_button.destroy()
            self.__temperature_resist_button.destroy()

    def make_frame_termopara(self, event):

        if self.__flag:

            self.__combo = Combobox(self.__frame, width=40)

            self.__combo['values'] = ("Выберите тип термопары",
                                      "Тип термопары L", "Тип термопары S", "Тип термопары M",
                                      "Тип термопары N", "Тип термопары K", "Тип термопары R",
                                      "Тип термопары T", "Тип термопары B", "Тип термопары E",
                                      "Тип термопары J", "Тип термопары A-1/A-2/A-3")

            self.__combo.current(0)
            self.__combo.grid(row=1, column=1, columnspan=2, pady=20)
            Label(self.__frame, text="Температура:", font=("Arial Bold", 10)) \
                .grid(row=2, column=0, pady=20)

            self.__txt_temperature.grid(row=2, column=1, pady=20)

            Label(self.__frame, text="Термо-ЭДС", font=("Arial Bold", 10)) \
                .grid(row=4, column=0, pady=20)

            self.__electric_force.grid(row=4, column=1, pady=20)

            Label(self.__frame, text="Результат:", font=("Arial Bold", 10)) \
                .grid(row=5, column=0, pady=20)

            self.__result_button.grid(column=1, row=6)
            self.__frame.pack()
            self.__exit_button.pack(pady=20)
            self.__flag = False
            self.__is_termopara = True
            self.__termopara_button.destroy()
            self.__temperature_resist_button.destroy()
