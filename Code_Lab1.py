import matplotlib.pyplot as pyplot
import control.matlab as matlab
import numpy as numpy
import math
import colorama as color

def choice():
    inertialessUnitName = 'Безынерционное звено'
    aperiodicUnitName = 'Апериодическое звено'
    integrUnitName = 'Интегрирующее звено'
    idealdiffUnitName = 'Идеальное дифференцирующее звено'
    realdiffUnitName = 'Реальное дифференцирующее звено'

    needNewChoice = True

    while needNewChoice:
        print(color.Style.RESET_ALL)
        userInput = input('Введите номер команды: \n'
                      '1 - ' + inertialessUnitName + ';\n'
                      '2 - ' + aperiodicUnitName + ';\n'
                      '3 - ' + integrUnitName + ';\n'
                      '4 - ' + idealdiffUnitName + ';\n'
                      '5 - ' + realdiffUnitName + '.\n')

        if userInput.isdigit():
            needNewChoice = False
            userInput = int(userInput)
            if userInput == 1:
                name = 'Безынерционное звено'
            elif userInput == 2:
                name = 'Апериодическое звено'
            elif userInput == 3:
                name = 'Интегрирующее звено'
            elif userInput == 4:
                name = 'Идеальное дифференцирующее звено'
            elif userInput == 5:
                name = 'Реальное дифференцирующее звено'
            else:
                print(color.Fore.RED + '\n Недопустимое значение!')
                needNewChoice = True
        else:
            print( color.Fore.RED + '\n Пожалуйста, введите числовое значение!')
            needNewChoice = True
    return name

def getUnit(name):

    needNewChoice = True
    while needNewChoice:
        print(color.Style.RESET_ALL)
        needNewChoice = False
        k = input('Пожалуйста, введите коэффициент "k": ')
        t = input('Пожалуйста, введите коэффициент "t": ')

        try:
            k = float(k)
            t = float(t)
            if name == 'Безынерционное звено':
                unit = matlab.tf([k], [1])
            elif name == 'Апериодическое звено':
                unit = matlab.tf([k], [t, 1])
            elif name == 'Интегрирующее звено':
                if t == 0:
                    unit = matlab.tf([k], [1, 0])
                else:
                    unit = matlab.tf([1], [t, 0])
            elif name == 'Идеальное дифференцирующее звено':
                if t == 0:
                    unit = matlab.tf([k, 0], [1 / 100000, 1])
                else:
                    unit = matlab.tf([t, 0], [1 / 100000, 1])
            elif name == 'Реальное дифференцирующее звено':
                unit = matlab.tf([k, 0], [t, 1])
        except:
            print(color.Fore.RED + '\n Пожалуйста, введите числовое значение!')
            needNewChoice = True
    return unit

def graph(num, title, y, x):
    pyplot.subplot(2, 1, num)
    pyplot.grid(True)
    if title == 'Переходная характеристика':
        pyplot.plot(x, y, 'purple')
    elif title == 'Импульсная характеристика':
        pyplot.plot(x, y, 'green')
    pyplot.title(title)
    pyplot.ylabel('Амплитуда')
    pyplot.xlabel('Время (с)')

unitName = choice()
unit = getUnit(unitName)

timeLine = []
for i in range(0, 1000):
    timeLine.append(i/1000)

[y, x] = matlab.step(unit, timeLine)
graph(1, 'Переходная характеристика', y, x)
[y, x] = matlab.impulse(unit, timeLine)
graph(2, 'Импульсная характеристика', y, x)
pyplot.show()
matlab.bode(unit, dB=False)
pyplot.plot()
pyplot.xlabel('Частота, Гц')
pyplot.show()

