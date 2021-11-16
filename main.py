import random
import time



def zvaigznajs():
        global points
        if input('Kā saucās ikgada V2V balva, kuru dod par izciliem saniegumies? ') == 'zvaigznājs':
            time.sleep(2)
            print('Pareizi!')
            points +=1

        else:
            time.sleep(2)
            print('Diemžēl nepareizi. :(')

        time.sleep(2)
        if input('Kas bija rakstīts uz 2019 gada zvaigznāja? ') == 'per aspera ad astra':
            time.sleep(2)
            print('Pareizi!')
            points += 1

        else:
            time.sleep(2)
            print('Diemžēl nepareizi. :(')



def skolotaji():
    global points
    if input('Kā tu domā cik pedagogi strādā skolā? ') == '60':
        time.sleep(2)
        print('Precīzi!')
        points += 1

    else:
        time.sleep(2)
        print('Diemžēl nepareizi. :(')
    time.sleep(2)

    if input('Kuru priekšmetu vada skolas direktors? ') == 'sportu':
        time.sleep(2)
        print('Precīzi!')
        points += 1

    else:
        time.sleep(2)
        print('Diemžēl nepareizi. :(')
    time.sleep(2)


def vesture():
    global points
    if input('Gads kurā mūsu skola ieguva vidusskolas statusu. ') == '1950':
        time.sleep(2)
        print('Pareizi!')
        points += 1

    else:
        time.sleep(2)
        print('Diemžēl nepareizi. :(')
    time.sleep(2)

    if input('Pirmais skolas avīzes izdevums tika veltīts skolas jubilejai, cik gadu jubileja tā bija? ') == '50':
        time.sleep(2)
        print('Pareizi!')
        points += 1

    else:
        time.sleep(2)
        print('Diemžēl nepareizi. :(')
    time.sleep(2)



def gramatas():
    global points
    if input('Kura valsts uzdāvināja vārdnīcas un enciklopēdijas skolas bibliotēkai? ') == 'krievija':
        time.sleep(2)
        print('Pareizi!')
        points += 1

    else:
        time.sleep(2)
        print('Diemžēl nepareizi. :(')
    time.sleep(2)

    if input('Kā saucās skolas avīze? ') == 'svoja':
        time.sleep(2)
        print('Pareizi!')
        points += 1

    else:
        time.sleep(2)
        print('Diemžēl nepareizi. :(')
    time.sleep(2)








if __name__ == '__main__':
    points = 0
    


    rand = 0
    varianti = ['zvaigznajs', 'skolotaji', 'gramatas', 'vesture']
    print('Labdien! Mani sauc par viktorīnu Pēterīti.')
    time.sleep(2)
    vards = input('Kā tevi sauc?')
    time.sleep(2)
    try:
        if vards[-1] == 'a' or vards[-1] == 's':
            print('Prieks iepazīties, ' + vards + '!')
        else:
            print('īpašs vārds?')
    except:
        print('Labi, paliec anonīms')

    time.sleep(2)
    print('Jebkurā gdījumā gatavojies viktorīnai.')
    print('')
    print('Noteikumi:')
    print('1. Visas atbildes raksti latviski, gramatiski pareizi, un ar mazo burtu.')
    print('2. Pēc šīs viktorīnas tu saņemsi savu rezultātu')
    time.sleep(2)
    for i in range(0, 4):
        rand = random.randint(0, len(varianti))
        eval(varianti[rand] + '()')
        varianti.pop(rand)
    if points > 4:
        print('Apsveicu tu ieguvi ' + str(points) + ' punktus!')
    else:
        print('Tu ieguvi ' + str(points) + ', turpini mācīties.')
    time.sleep('5')

    












