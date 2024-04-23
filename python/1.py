slownik = {
    'okno': "window",
    'jablko': 'apple',
    'klawiatura': 'keyboard',
    'czlowiek': 'human',
    'Wojtek': 'gay',
}
slowo=input('podaj słowo po polsku: ')
if slowo in slownik:
    print(slownik[slowo])
else:
    print('w slowniku nie ma takiego slowa.')
    x = str(input('Czy chcesz je dodać?(nie/tak)'))
    if x == 'nie':
        exit()
    elif x=='tak':
            z = str(input('podaj, co znaczy to słowo po angielsku: '))
            slownik[slowo] = z
            print(slownik)
    else:
        exit()
