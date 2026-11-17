# 1 Juku kinno
# Programm küsib eesnime. Kui nimi on Juku, kuvatakse „Lähme Jukuga kinno!“, 
# muidu teatatakse, et täna kinno ei minda.
# Programm peab Juku ära tundma ka siis, 
# kui nimi on kirjutatud suurtähtedega (JUKU) või väiketähtedega (juku).
# Kui nimi on kirjutatud ainult suurtähtedega, 
# lisa märkus „Ära karju, Juku!“.
#Kasuta: lower(), isupper(), istitle(),upper(), title()
from curses.ascii import isalpha, isdigit


eesnimi=input("Sisesta eesnimi: ")
if eesnimi.lower() == "juku":
    print("Lähme Jukuga kinno!")
    if eesnimi.isupper():
        print("Ära karju, Juku!")
    elif eesnimi.islower():
        print("Ära sosista, Juku!")
    #Kui kinno läheb Juku, küsi tema vanus ja otsusta, millist piletit on vaja osta:
    #Kontrolli enne, kas sisestatud vanus on täisarv. 
    #Kui ei ole, kuva veateade.
    vanus=input(f"Kui vana on {eesnimi}? ")
    if vanus.isdigit():
        vanus=int(vanus)
        if 0<vanus<6:
            pilet="tasuta pilet"
        elif 6<=vanus<14:
            pilet="lapsepilet"
        elif 14<=vanus<65:
            pilet="täispilet"
        elif 65<=vanus<=100:
            pilet="sooduspilet"
        else:
            pilet="tundmatu pilet"
        print(f"{eesnimi} vajab {pilet}.")
    else:
        print("Viga andmedega")
else:
    print("Täna kinno ei minda.")
# 2 Pinginaabrid
# Küsi kahe inimese nimed. Kontrolli, kas mõlemad nimed koosnevad ainult tähtedest. 
# Kui jah, teata kasutajale, kas nad on täna pinginaabrid või mitte. 
# Kui mõnes nimes on numbreid või muid märke, kuva veateade.
# Otsusta ise, kuidas „pinginaabrid“ määratakse, 
# näiteks juhuslikult või nimede algustähtede järgi.
# Kasuta: isalpha(), capitalize()
pinginaabrid=["Mati","Kati"]
nimi1=input("Sisesta nimi: ")
nimi2=input("Sisesta nimi: ")
if nimi1.isalpha() and nimi2.isalpha():
    print(f"Tere {nimi1.capitalize()} ja {nimi2.capitalize()}")
    nimi1=nimi1.capitalize()
    if nimi1 in pinginaabrid and nimi2.capitalize() in pinginaabrid:
        print(f"{nimi1} ja {nimi2} on pinginaabrid")
    else:
        print("Nad ei ole pinginaabrid")

else:
    print("Viga: nimed on valesti sisestatud! Kasuta ainult tähed")

# 3. Remont
# Küsi ristkülikukujulise toa pikkus ja laius ning arvuta põranda pindala.
# Seejärel küsi, kas kasutaja soovib remonti teha. Kui vastus on jaatav, 
# küsi ruutmeetri hind ja arvuta põranda vahetamise hind.
# Lisaküsimus: kas kasutaja teeb remondi ise või kasutab professionaali abi? 
# Professionaali puhul küsi ka töö hind ruutmeetri kohta ja 
# arvuta remondi koguhind koos tööga.
# Kasuta: float(), lower() 
# (vastuse „Jah“, „JAH“, „jah“ äratundmiseks), round()
try:
    pikkus=float(input("Sisesta pikkus: "))
    laius=float(input("Sisesta laius: "))
    pindala=round(pikkus*laius,2) #ümardamine 
    print(f"Pindala on {pindala}")
    remont=input("Kas soovid remonti teha? (jah/ei)").lower() #tähed on väikesed
    if remont=="jah":
        print("Teeme remonti!")
        try:
            rm_hind=float(input("Sisesta ruutmeetri hind: "))
            hind=round(pindala*rm_hind,2)
            print(f"Põranda vahetamise hind on {hind} €")
            ise=input("Kas teeb remondi is?(jah/ei)").lower()
            if ise=="jah":
                print(f"Põranda vahetamise hind on sama {hind} €")
            else:
                try:
                    töö_hind=float(input("Töö hind: "))
                    koguhind=round(hind+pindala*töö_hind,2)
                    print(f"Remondi koguhind koos tööga on {koguhind}")
                except ValueError:
                    print("Tööhind on ujukomarv")
        except ValueError:
            print("Viga: ruutmeetri hind on arv")
    else:
        print("Remonti ei tehta!")
except ValueError:
    print("Viga: kasuta numbreid pikkuse ja laiuse sisestamiseks")