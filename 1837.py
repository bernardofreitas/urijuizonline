# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from decimal import Decimal


def main():
    a, b = map(Decimal, input().split())
    q, r = int(Decimal(a / b)), int(Decimal(a % b))
    print(q, r)


if __name__ == '__main__':
    main()
