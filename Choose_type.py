import math
#import  Graphic_interface


def make_choice(number_of_termo, temperature, zero_resist):


        if number_of_termo == 1:

            a = 3.9083 * 10e-4
            b = -5.775 * 10e-9
            c = -4.183 * 10e-16

            if -200 <= temperature < 0:

                result = zero_resist * (
                        1 + a * temperature + b * math.pow(temperature, 2) + c * (temperature - 100) * math.pow(
                    temperature, 3))



            elif 0 < temperature <= 850:

                result = zero_resist * (1 + a * temperature + b * math.pow(temperature, 2))

                print(result)

        elif number_of_termo == 2:

            a = 3.9690 * 10e-4
            b = -5.841 * 10e-9
            c = -4.330 * 10e-16

            print("Введите нулевое сопротивление: ", end='')
            zero_resist = float(input())

            print("Введите температуру: ", end='')
            temperature = float(input())

            if -200 <= temperature < 0:

                result = zero_resist * (
                        1 + a * temperature + b * math.pow(temperature, 2) + c * (temperature - 100) * math.pow(
                    temperature, 3))

                print(result)

            elif 0 < temperature <= 850:

                result = zero_resist * (1 + a * temperature + b * math.pow(temperature, 2))

                print(result)
        elif number_of_termo == 3:

            a = 4.28 * 10e-4
            b = -6.2032 * 10e-9
            c = 8.5154 * 10e-13

            print("Введите нулевое сопротивление: ", end='')
            zero_resist = float(input())

            print("Введите температуру: ", end='')
            temperature = float(input())

            if -180 <= temperature < 0:

                result = zero_resist * (
                        1 + a * temperature + b * temperature * (temperature + 6.7) + c * math.pow(
                    temperature, 3))

                print(result)

            elif 0 < temperature <= 200:

                result = zero_resist * (1 + a * temperature)

                print(result)
        elif number_of_termo == 4:

            a = 5.4963 * 10e-4
            b = 6.7556 * 10e-7
            c = 9.2004 * 10e-12

            print("Введите нулевое сопротивление: ", end='')
            zero_resist = float(input())

            print("Введите температуру: ", end='')
            temperature = float(input())

            if -60 <= temperature < 100:

                result = zero_resist * (1 + a * temperature + b * math.pow(temperature, 2))

                print(result)

            elif 100 < temperature <= 180:

                result = zero_resist * (
                        1 + a * temperature + b * math.pow(temperature, 2) + c * math.pow(temperature, 2) * (
                        temperature - 100))

                print(result)
