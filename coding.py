import math

def mk_freq(stri):
    r = {}  # создаётся пустой массив r который будет
    # содержать каждую частоту символа в строке
    for a in stri:
        if r.get(a) is None:
            r[a] = 1  # если символа нет в r его частота равна 1
        else:
            r[a] = r[a] + 1  # если есть, то увеличиваем на 1
    return r


def ar_pack(stri):
    d = mk_freq(stri)
    # создаём массив d с частотой каждого символа
    s = sum(d.values())  # вычисляем сумму всех значений в d
    # построение системы интервалов

    interv = {}

    left = 0  # левая граница зоны буквы k
    for k in d.keys():
        v = d[k]  # v - частота буквы k
        right = left + v / s  # правая граница для k

        interv[k] = (left, right)  # для символа к устан. интервал и добавляю в список
        left = right  # левая граница каждого символа это правая граница последующ.

    left = 0  # уст. начальные значения границ
    right = 1  #

    for a in stri:
        a_left = interv[a][0]  # получаю левую границу символа
        a_right = interv[a][1]  # получаю правую его границу

        size = right - left  # вычисляю размер текущего интервала

        left = left + size * a_left  # обновляю левую границу
        right = left + size * (a_right - a_left)  # и правую

    return 0.5 * (left + right)



def shannon_entropy(text):
    d = mk_freq(text)
    s = sum(d.values())

    entropy = 0
    for count in d.values():
        pi = count / s
        entropy -= pi * math.log2(pi)

    return entropy


with open('text.txt', 'r') as f:
    text = f.read()
with open('result.txt', 'w') as file:
    result = str(ar_pack(text))
    result = result.replace('0.', '')
    file.writelines('Код в десятичной системе:' + result + '\n')
    result = int(result)
    result = bin(result)
    H = str(shannon_entropy(text))
    # print(H)
    file.writelines('Код в двоичной системе:' + result + '\n')
    file.writelines('Энтропия по формуле Шеннона:'+ H + '\n')


# print(H)
