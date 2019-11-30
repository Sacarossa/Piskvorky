
from util import tah
from ai import tah_pocitace

from random import randrange
def vyhodnot(pole):
    'dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec podle stavu hry'

    if 'xxx' in pole:
        return 'x'
    elif 'ooo' in pole:
        return 'o'
    elif '-' in pole:
        return '-'
    else:
        return '!'


def tah_hrace(pole):
    "Vrátí herní pole se zaznamenaným tahem hráče"
    while True:
        cislo_policka = int(input('Kterou pozici od 0 do 19 si zabíráš? '))

        if cislo_policka >= 0 and cislo_policka < 20 and '-' == pole[cislo_policka]:
            return tah(pole, cislo_policka, 'x')


def piskvorky1d(pole):
    
    while True:
        pole = tah_hrace(pole)
        pole = tah_pocitace(pole, 'o')
        print(pole)
        print('01234567890123456789')
        stav = vyhodnot(pole)
        if stav == 'x':
            print('Vyhrál jsi.')
            break
        elif stav == 'o':
            print('Vyhrál počítač.')
            break
        elif stav == '!':
            print('Je to remíza.')
            break








    


                
            

                

        


    








