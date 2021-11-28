import time

atbilde1 = []
atbilde2 = []
atbilde3 = []
atbilde4 = []
atbilde5 = []

teikums1 = ['', '', '', '', '']
teikums2 = ['', '', '', '', '']
teikums3 = ['', '', '', '', '']
teikums4 = ['', '', '', '', '']
teikums5 = ['', '', '', '', '']
print('Si ir MadText spele')
print("Speles noteikumi:")
print('Visi speletaji pec kartas atbildes')
print('Pec atbilzu sniegsanas jus redzesiet samiksetas atbildes')

atbilde1.append(input('Kads? ')+' ')
atbilde1.append(input('Kas? ')+' ')
atbilde1.append(input('Kur? ')+' ')
atbilde1.append(input('Ko darija? ')+' ')
atbilde1.append(input('Kas sanaca? ')+' ')

atbilde2.append(input('Kads? ')+' ')
atbilde2.append(input('Kas? ')+' ')
atbilde2.append(input('Kur? ')+' ')
atbilde2.append(input('Ko darija? ')+' ')
atbilde2.append(input('Kas sanāca? ')+' ')

atbilde3.append(input('Kads? ')+' ')
atbilde3.append(input('Kas? ')+' ')
atbilde3.append(input('Kur? ')+' ')
atbilde3.append(input('Ko darija? ')+' ')
atbilde3.append(input('Kas sanaca? ')+' ')

atbilde4.append(input('Kads? ')+' ')
atbilde4.append(input('Kas? '))
atbilde4.append(input('Kur? ')+' ')
atbilde4.append(input('Ko darija? ')+' ')
atbilde4.append(input('Kas sanaca? ')+' ')

atbilde5.append(input('Kads? ')+' ')
atbilde5.append(input('Kas? ')+' ')
atbilde5.append(input('Kur? ')+' ')
atbilde5.append(input('Ko darija? ')+' ')
atbilde5.append(input('Kas sanaca? ')+' ')

print(atbilde1[0]+atbilde2[1]+atbilde3[2]+atbilde4[3]+atbilde5[4])
print(atbilde2[0]+atbilde3[1]+atbilde4[2]+atbilde5[3]+atbilde1[4])
print(atbilde3[0]+atbilde4[1]+atbilde5[2]+atbilde1[3]+atbilde2[4])
print(atbilde4[0]+atbilde5[1]+atbilde1[2]+atbilde2[3]+atbilde3[4])
print(atbilde5[0]+atbilde1[1]+atbilde2[2]+atbilde3[3]+atbilde4[4])