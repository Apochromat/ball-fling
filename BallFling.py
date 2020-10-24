#   Ball Fling
#   by Markridge
#   2020


# Импорт
import sys
import math
from PyQt5 import QtWidgets
from design import Ui_MainWindow  # импорт нашего дизайн-файла
import numpy as np

# Переменные, константы и флаги
data = [0, 0, 0, 0]
graphArray = []
V0 = 0
A = 0
S = 0
H = 0
L = 0.0
T = 0.0
G = 9.81
flagCollectionSuccess = True

# Построение окна
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


# Функции
def getdata():
    global V0, A, S, H, data, flagCollectionSuccess
    try:
        V0 = int(ui.V0_lineEdit.text())  # Читаем поле и переводим в целочисленное
        ui.V0_lineEdit.setStyleSheet("background-color: rgb(255, 254, 217);")  # Заливаем поле кремовым
        data[0] = V0
        if V0 <= 0:
            ui.V0_lineEdit.setStyleSheet("background-color: rgb(255, 0, 0);")  # Заливаем поле красным
            flagCollectionSuccess = False
            ui.statusBar.showMessage("V0 не может быть отрицательным или 0")  # Вывод ошибки в статус-бар
    except ValueError:
        ui.V0_lineEdit.setStyleSheet("background-color: rgb(255, 0, 0);")  # Заливаем поле красным
        ui.statusBar.showMessage("V0 должен быть числом")  # Вывод ошибки в статус-бар
        flagCollectionSuccess = False

    try:
        A = int(ui.A_lineEdit.text())  # Читаем поле и переводим в целочисленное
        ui.A_lineEdit.setStyleSheet("background-color: rgb(255, 254, 217);")  # Заливаем поле кремовым
        data[1] = A
        if (A <= 0) | (A >= 90):
            ui.A_lineEdit.setStyleSheet("background-color: rgb(255, 0, 0);")  # Заливаем поле красным
            flagCollectionSuccess = False
            ui.statusBar.showMessage("А должен принадлежать (0; 90) ")  # Вывод ошибки в статус-бар
    except ValueError:
        ui.A_lineEdit.setStyleSheet("background-color: rgb(255, 0, 0);")  # Заливаем поле красным
        flagCollectionSuccess = False
        ui.statusBar.showMessage("А должен быть числом")  # Вывод ошибки в статус-бар

    try:
        S = int(ui.S_lineEdit.text())  # Читаем поле и переводим в целочисленное
        ui.S_lineEdit.setStyleSheet("background-color: rgb(255, 254, 217);")  # Заливаем поле кремовым
        data[2] = S
        if S <= 0:
            ui.S_lineEdit.setStyleSheet("background-color: rgb(255, 0, 0);")  # Заливаем поле красным
            flagCollectionSuccess = False
            ui.statusBar.showMessage("S не может быть отрицательным или 0")  # Вывод ошибки в статус-бар
    except ValueError:
        ui.S_lineEdit.setStyleSheet("background-color: rgb(255, 0, 0);")  # Заливаем поле красным
        flagCollectionSuccess = False
        ui.statusBar.showMessage("S должен быть числом")  # Вывод ошибки в статус-бар

    try:
        H = int(ui.H_lineEdit.text())  # Читаем поле и переводим в целочисленное
        ui.H_lineEdit.setStyleSheet("background-color: rgb(255, 254, 217);")  # Заливаем поле кремовым
        data[3] = H
        if H <= 0:
            ui.H_lineEdit.setStyleSheet("background-color: rgb(255, 0, 0);")  # Заливаем поле красным
            flagCollectionSuccess = False
            ui.statusBar.showMessage("H не должен быть отрицательныи или 0")  # Вывод ошибки в статус-бар
    except ValueError:
        ui.H_lineEdit.setStyleSheet("background-color: rgb(255, 0, 0);")  # Заливаем поле красным
        flagCollectionSuccess = False
        ui.statusBar.showMessage("H должен быть числом")  # Вывод ошибки в статус-бар


def calculation():
    global V0, A, S, H, T, L, flagCollectionSuccess, graphArray
    # Очищаем вывод
    ui.result_lineEdit.setText(" ")
    ui.result_lineEdit.setStyleSheet("background-color: rgb(221, 252, 255);")  # Кремовый
    ui.L_lineEdit.setText(" ")

    getdata()  # Получаем данные
    if flagCollectionSuccess:  # Если данные пришли без ошибок
        ui.statusBar.showMessage("OK")
        V0 = float(data[0])
        A = float(data[1])
        A = A * math.pi / 180  # Перевод из градусов в радианы
        S = float(data[2])
        H = float(data[3])
        T = S / (V0 * math.cos(A))  # Вычисление времени приземления
        L = round(S * math.tan(A) - (G * S * S) / (2 * math.pow(V0, 2) * math.pow(math.cos(A), 2)), 2)
        # Вычисление высоты в точке S

        if (L > 0) & (L <= H):
            ui.result_lineEdit.setText("Попадание")
            ui.result_lineEdit.setStyleSheet("background-color: rgb(190, 255, 0);")  # Лаймовый
        elif L > H:
            ui.result_lineEdit.setText("Перелет")
            ui.result_lineEdit.setStyleSheet("background-color: rgb(255, 36, 0);")  # Красный
        elif L < 0:
            ui.result_lineEdit.setText("Недолет")
            ui.result_lineEdit.setStyleSheet("background-color: rgb(255, 36, 0);")  # Красный
            L = 0
        ui.L_lineEdit.setText(str(L))  # Вывод L

        # Создание массива для вывода графика
        sArray = np.arange(0, S, 0.05)  # Массив значений оси OX
        graphArray = np.zeros((len(sArray), 2))  # Пустой массив вывода
        for i in range(0, len(sArray)):  # Заполняем массив вывода
            OX = sArray[i]
            graphArray[i, 0] = OX  # OX
            OY = OX * math.tan(A) - (G * OX * OX) / (2 * math.pow(V0, 2) * math.pow(math.cos(A), 2))
            if OY > 0:
                graphArray[i, 1] = OY  # OY
            else:
                graphArray[i, 1] = 0  # OY
    else:
        flagCollectionSuccess = True  # Сбрасываем флаг


def visualization():
    ui.graphicsView.clear()  # Очищаем график
    ui.graphicsView.setMouseEnabled(x=False, y=False)  # Запрещаем перемещать график (добавлено в design)
    ui.graphicsView.setMenuEnabled(enableMenu=False, enableViewBoxMenu='same')  # Отключаем меню (добавлено в design)
    ui.graphicsView.plot(graphArray, title="Graph")  # Выводим график


# Привязывание кнопок к функциям

ui.calculate_Button.pressed.connect(calculation)  # Кнопка Посчитать
ui.visualize_Button.pressed.connect(visualization)  # Кнопка Отобразить

# Обработка выхода
sys.exit(app.exec_())
