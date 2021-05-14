"""
Uzrakstiet programmu Python, lai aprēķinātu cilindra tilpumu un virsmas laukumu.

Piezīme: Cilindrs ir viena no visvienkāršākajām izliektajām ģeometriskajām 
formām, virsma, ko veido punkti fiksētā attālumā no noteiktās taisnes, 
cilindra ass.

Piezīme:
Ievaddati: Pamata rādiuss un cilindra augstums
Izvaddati: Cilindra virsmas laukums un tilpums 
"""
radiuss = int(input("Ievadi rādiusu: "))
augstums = int(input("Ievadi augstumu: "))

tilpums =3,14*(radiuss*radiuss)*augstums;

laukums =3,14*(radiuss*radiuss)
print("Atbilde ir "+laukums)