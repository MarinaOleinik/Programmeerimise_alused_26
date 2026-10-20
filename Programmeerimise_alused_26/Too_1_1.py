from math import * #pi, sqrt()
from random import * #randint(a,b)  juhuslik täisarv a ja b vahel

# Kirjuta enda esimene programm, mis väljastab käsureale teksti: 
#     “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: 
#     “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”
#Ülesanne1
print("Tere, maailm!")
nimi=input("Mis on sinu nimi? ")
print("Tere, maailm! Tervitan sind",nimi)
try:
    vanus=int(input("Kui vana sa oled? "))
    print("Tere, maailm! Tervitan sind",nimi,"! Sa oled",vanus,"aastat vana.")
except ValueError:
    print("Palun sisesta oma vanus numbrina.")

# 
# Ülesanne 2 
# on järgnevad muutujad:
# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 16.5
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? 
# Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# Kirjuta kood tüüpide kontrollimiseks.
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis=True
print("vanus:", vanus, "tüüp:", type(vanus))
print("eesnimi:", eesnimi, "tüüp:", type(eesnimi))
print("pikkus:", pikkus, "tüüp:", type(pikkus))
print("kas_käib_koolis:", kas_käib_koolis, "tüüp:", type(kas_käib_koolis))

#Ülesanne 3
# Kirjuta enda koodis laual olevate kommide arv muutujasse
# (kommide arv on juhuslik). 
# Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
# Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. 
# Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, 
# kui palju komme laual nüüd on.

kommide_arv=randint(1,100) #1-100 vahel juhuslik täisarv
print("Laual on", kommide_arv, "kommi.")
try:
    b=int(input("Mitu kommi soovid laualt ära võtta? "))
    kommide_arv -= b #kommidearv väheneb b võrra
    print("Laual on nüüd", kommide_arv, "kommi.")
except ValueError:
    print("Palun sisesta kommid numbrina.")


#Ülesanne 4
#Puu läbimõõdu arvutamine
# Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu 
# ning teatab selle peale puu läbimõõdu.

ümbermõõt=float(input("Sisesta puu ümbermõõt: "))

läbimõõt=ümbermõõt/pi
print("Puu läbimõõt on:", läbimõõt)

#Ülesanne 5
#Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, 
#mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
N = float(input("Sisesta maatüki pikkus (N): "))
M = float(input("Sisesta maatüki laius (M): "))
diagonaal = sqrt(N**2 + M**2) #** astendamine
print("Ristkülikukujulise maatüki diagonaal on:", round(diagonaal,2)) 
#round() ümardab kahe kümnendkohani

#Ülesanne 6
#Leidke järgnevast näiteprogrammist loogiline viga:
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg # siin oli viga

print("Sinu kiirus oli " + str(kiirus) + " km/h")

#Ülesanne 7
#Koostada programm, mis arvutab aritmeetilise keskmise
# suvalisest etteantud 5 täis arvust.
#Leia nende arvude summa, jagatuna kasutaja poolt sisestatud arvuga, 
#täisarvuline osa ja jääk.
arv1=int(input("Sisesta esimene täisarv: "))
arv2=int(input("Sisesta teine täisarv: "))
arv3=int(input("Sisesta kolmas täisarv: "))
arv4=int(input("Sisesta neljas täisarv: "))
arv5=int(input("Sisesta viies täisarv: "))
summa=arv1+arv2+arv3+arv4+arv5
jagaja=int(input("Sisesta arv, millega jagada: "))
tulemus=summa/jagaja
print("Tulemus:", tulemus) #tulemus=3.75
print("Täisarvuline osa:", int(tulemus)) 
#int(3.75)=3 teine variant täisosa leidmiseks on kasutada // jagamist: summa//jagaja
print("Jääk:", summa % jagaja)
