def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    while True:
        if 'o-o' in pole:
            cislo_policka = pole.index('o-o') + 1
        elif '-oo' in pole:
            cislo_policka = pole.index('-oo')
        elif 'oo-' in pole:
            cislo_policka = pole.index('oo-') + 2
        elif 'x-x' in pole:
            cislo_policka = pole.index('x-x') + 1
        elif '-xx' in pole:
            cislo_policka = pole.index('-xx')
        elif 'xx-' in pole:
            cislo_policka = pole.index('xx-') + 2
        elif '-o' in pole:
            cislo_policka = pole.index('-o')
        elif 'o-' in pole:
            cislo_policka = pole.index('o-') + 1
        else:
            cislo_policka = randrange(20)
        
        if '-' == pole[cislo_policka]:
            return tah(pole, cislo_policka, 'o')