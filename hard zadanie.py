#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    k = int(input("Введите k:"))
    k1 = k
    if 1 <= k <= 180:
        k1 = (k + 1) // 2
        print("Номер пары цифр:", k1)
        if 1 <= k <= 178:
            if k1 % 2 == 0:
                a1 = range(10,100)
                k2 = a1[k1]
                print("двузначное число:", k2)

            elif k1 % 2 == 1:
                a2 = range(9,100)
                k3 = a2[k1]
                print("двузначное число:", k3)

        elif k == 179 or k == 180:
            print("двузначное число: 99" )
        c = ((k / 2 - 1) % 10) * (k % 2 == 0) + (k / 20 + 1) * (k % 2 == 1)
        print("k-я цифра:", '%.0f' % c)

    else:
        print("Введите число в диапазоне от 1 до 180")
