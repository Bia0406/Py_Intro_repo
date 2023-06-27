
# if
piesa_faina = True

print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

# if else

# daca nr este par printam acest lucru
# altfel printam impar
nr = 4
# ce inseamna par? se imparte exact la 2
# ce inseamna ca se imparte la 2? ne da restul 0
if nr % 2 == 0:
    print('numar par')
else:
    print('numar impar')

# este un nr pozitiv?
if (nr > 0):
    print('pozitiv')
else :
    print('nr nu este pozitiv')

#if, else if, else



# cum ne saluta robotelul in functie de ora

#luam date de la tastatura
#ne asiguram ca sunt trasformate din string in int
# ora = int(input('Introdu ora'))
#     print (ora == 17)
# if ora < 0:
#     print('ora invalida, ora negativa')
# elif ora <= 11:
#     print('buna dimineata')
# elif ora <= 18:
#     print('buna ziua')
# elif ora <= 21:
#     print('buna seara')
# elif ora <= 24:
#      print('noapte buna')
# else:
#     print('ora invalida. ora mai mare decat 24')
# CTRL + /
# robotel telefonic
# optiunea = int(input('alege o optiune'))
# if optiunea == 0:
#     print('meniu anterior')
# elif optiunea == 1:
#     print('ati ales ro')
# elif optiunea == 2:
#     print('ati ales eng')
# else:
#     print('nu am identificat optiunea, mai incearca')

# daca are sub 18 ani nu poate paria

copil = int(input('Cati ani ai?'))
if copil < 0 :
    print('varsta inexistenta')
elif copil <=17:
    print ('Prea mic, ne pare rau, dar nu poti paria')
elif copil == 18:
    print ('Introduceti cotele dorite')
else :
    print('Introduceti biletul dvs')
