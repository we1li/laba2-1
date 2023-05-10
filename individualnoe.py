#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
  import math

  x1, y1 = input("Введите координаты 1ой точки: ").split(" ")
  x2, y2 = input("Введите координаты 2ой точки: ").split(" ")
  x3, y3 = input("Введите координаты 3ой точки: ").split(" ")
  x4, y4 = input("Введите координаты 4ой точки: ").split(" ")

  a = math.sqrt(((int(x1) - int(x2)) ** 2) + ((int(y1) - int(y2)) ** 2))
  b = math.sqrt(((int(x1) - int(x4)) ** 2) + ((int(y1) - int(y4)) ** 2))
  c = math.sqrt(((int(x2) - int(x4)) ** 2) + ((int(y2) - int(y4)) ** 2))
  a1 = math.sqrt(((int(x1) - int(x3)) ** 2) + ((int(y1) - int(y3)) ** 2))
  b1 = math.sqrt(((int(x1) - int(x4)) ** 2) + ((int(y1) - int(y4)) ** 2))
  c1 = math.sqrt(((int(x3) - int(x4)) ** 2) + ((int(y3) - int(y4)) ** 2))
  p = (a + b + c) / 2
  p1 = (a1 + b1 + c1) / 2
  s = math.sqrt(p * (p - a) * (p - b) * (p - c))
  s1 = math.sqrt(p1 * (p1 - a1) * (p1 - b1) * (p1 - c1))
  sum = s + s1
  print("Площадь :", sum)
