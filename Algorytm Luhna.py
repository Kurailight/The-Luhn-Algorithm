import numpy as np
#pierwotny_numer= [5,4,3,2,1,0,1,2,3,4,6,7,8,9,8,7]
num= input("Podaj numer karty, który chcesz sprawdzić(wpisz cyfry ciągiem, bez spacji oraz przecinków): ")
pierwotny_numer = list(map(int, list(num)))

def przypisanie_wagi(pierwotny_numer):
    for i in range(len(pierwotny_numer)-1,-1,-2):
        pierwotny_numer[i]=pierwotny_numer[i]*1
        if pierwotny_numer[i]>9:
            pierwotny_numer[i]= sum(int(cyfra) for cyfra in str(pierwotny_numer[i]))
            
    for i in range(len(pierwotny_numer)-2,-1,-2):
        pierwotny_numer[i]=pierwotny_numer[i]*2
        if pierwotny_numer[i]>9:
            pierwotny_numer[i]= sum(int(cyfra) for cyfra in str(pierwotny_numer[i]))
            
    numer_przemnozony=list(pierwotny_numer.copy())
    return numer_przemnozony
numer_przemnozony= przypisanie_wagi(pierwotny_numer)
print(numer_przemnozony)# kolejność ważna (najpierw)
#przypisujesz wartość do zmiennej a potem drukujesz, wtedy nie tracisz wyniku.
def checksum(numer_przemnozony):
    suma = sum(numer_przemnozony)
    return suma
s= checksum(numer_przemnozony)
print(s)

def modten(s):
    if s%10==0:
        print(f'Podany numer karty {pierwotny_numer} jest prawidłowy.')
    else:
        print(f'Podany numer karty {pierwotny_numer} nie jest prawidłowy.')
modten(s)

