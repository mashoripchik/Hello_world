# Определить степень вероятности получения водителем штрафа за перегруз маршрутки

n = int(input("Вместимость маршрутки"))
n1 = int(input("Количество пассажиров во время поездки"))
v = int(input("Вероятность остановки сотрудниками ГАИ на маршруте"))
if n >= n1:
    print("Маршрутка не перегруженна, штраф отменяется")
elif n < n1:
    print("Маршрутка перегруженна")
    if v >= 0 and v < 25:
        print("Вероятность получения штрафа минимальная")
    elif v >= 25 and v < 50:
        print("Вероятность получения штрафа средняя")
    elif n < n1 and v >= 50 and v < 75:
        print("Вероятность получения штрафа высокая")
    else:
        print("Вероятность получения штрафа 100 процентная")