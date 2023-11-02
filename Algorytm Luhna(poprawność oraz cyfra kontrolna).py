num= input("Podaj numer karty, który chcesz sprawdzić lub niepełny numer karty (15 cyfr) jeśli szukasz cyfry kontrolnej (wpisz cyfry ciągiem, bez spacji oraz przecinków): ")
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
def checksum(numer_przemnozony):
    suma = sum(numer_przemnozony)
    return suma
s= checksum(numer_przemnozony)
#print(s)

def modten(s):
    if s%10==0:
        print(f'Podany numer karty {pierwotny_numer} jest prawidłowy.')
    else:
        print(f'Podany numer karty {pierwotny_numer} nie jest prawidłowy.')

def cyfra_kontrolna(s):
    if s%10!=0:
        generator = int(str(s)[-1])
        cyfra= 10- generator
    else:
        cyfra=0
    return cyfra
if len(num)==15:
    print("A więc szukasz cyfry kontrolnej")   
    print(f'Jest nią cyfra: {cyfra_kontrolna(s)}.') 
elif len(num)==16:
    modten(s)
elif len(num)!=15 and len(num)!=16:
    print("Podałeś złą ilość cyfr")
