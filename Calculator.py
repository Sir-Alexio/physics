from tkinter import *
from tkinter.ttk import Combobox


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
        self.__zero_Resist = Entry(self.__frame, width=10)
        self.__resist = Entry(self.__frame, width=10)
        self.__result_button = Button(self.__frame, text="Расчитать")
        self.__exit_button = Button(self.__window, text="Выход")
        self.__flag = True

    def get_window(self):
        return self.__window

    def get_temperature_resist_button(self):
        return self.__temperature_resist_button

    def get_termopara_button(self):
        return self.__termopara_button

    def paint_button(self, button, row, column):
        button.pack()

    def make_frame_temperature_resist(self, event):
        if self.__flag:
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

            self.__zero_Resist.grid(row=3, column=1, pady=20)

            Label(self.__frame, text="Сопротивление темпопреобр.", font=("Arial Bold", 10)) \
                .grid(row=4, column=0, pady=20)

            self.__resist.grid(row=4, column=1, pady=20)

            Label(self.__frame, text="Результат:", font=("Arial Bold", 10)) \
                .grid(row=5, column=0, pady=20)
            self.__frame.pack()
            self.__exit_button.pack(pady=20)
            self.__flag = False

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
