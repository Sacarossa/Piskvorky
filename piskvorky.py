import ai
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

def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"

    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]

def tah_hrace(pole):
    "Vrátí herní pole se zaznamenaným tahem hráče"
    while True:
        cislo_policka = int(input('Kterou pozici od 0 do 19 si zabíráš? '))

        if cislo_policka >= 0 and cislo_policka < 20 and '-' == pole[cislo_policka]:
            return tah(pole, cislo_policka, 'x')

from random import randrange

def piskvorky1d(pole):
    
    while True:
        pole = tah_hrace(pole)
        pole = tah_pocitace(pole)
        print(pole)
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








    


                
            

                

        


    








