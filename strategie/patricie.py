
from random import randrange

def tah_pocitace(pole, symbol):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    if symbol == 'o':
        symbol_soupere = 'x'
    else:
        symbol_soupere = 'o'
    
    if not '-' in pole:
        raise ValueError

    # mám šanci vyhrát
    elif symbol + '-' + symbol in pole:
        cislo_policka = pole.index(symbol + '-' + symbol) + 1
    elif '-' + symbol + symbol in pole:
        cislo_policka = pole.index('-' + symbol + symbol)
    elif symbol + symbol + '-' in pole:
        cislo_policka = pole.index(symbol + symbol + '-') + 2

    # soupeř má šanci vyhrát
    elif symbol_soupere + '-' + symbol_soupere in pole:
        cislo_policka = pole.index(symbol_soupere + '-' + symbol_soupere) + 1
    elif '-' + symbol_soupere + symbol_soupere in pole:
        cislo_policka = pole.index('-' + symbol_soupere + symbol_soupere)
    elif symbol_soupere + symbol_soupere + '-' in pole:
        cislo_policka = pole.index(symbol_soupere + symbol_soupere + '-') + 2

    # hraju k sobě
    elif '--' + symbol in pole:
        cislo_policka = pole.index('--' + symbol) + 1
    elif symbol + '--' in pole:
        cislo_policka = pole.index(symbol + '--') + 1

    elif '--' + symbol_soupere + '-' in pole:
        cislo_policka = pole.index('--' + symbol_soupere + '-') + 1
    elif '-' + symbol_soupere + '--' in pole:
        cislo_policka = pole.index('-' + symbol_soupere + '--') + 2
    elif '--' + symbol_soupere in pole:
        cislo_policka = pole.index('--' + symbol_soupere) + 1
    elif symbol_soupere + '--' in pole:
        cislo_policka = pole.index(symbol_soupere + '--') + 1

    elif '-' + symbol in pole:
        cislo_policka = pole.index('-' + symbol)
    elif symbol + '-' in pole:
        cislo_policka = pole.index(symbol + '-') + 1

    else:
        while True:    
            cislo_policka = randrange(len(pole))
            if '-' == pole[cislo_policka]:
                break

    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
