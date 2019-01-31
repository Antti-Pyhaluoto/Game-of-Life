from PIL import Image
from random import randint

#Rules to game of life
# Any live cell with fewer than two live neighbors dies, as if by under population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by overpopulation.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction

def Tallenna(maa, mones):
	kuva = Image.new("RGB", (1000, 1000), color = "white")

	for i in range(len(maa[0])):
		for j in range(len(maa)):
			if maa[j][i] == 1:
				kuva.paste( Image.new("RGB", (10, 10), color = "black"), (10*j, 10*i))
	#kuva.show()
	if mones < 10:
		kuva.save("life000%d.jpg" % mones)
	elif mones < 100:
		kuva.save("life00%d.jpg" % mones)
	elif mones < 1000:
		kuva.save("life0%d.jpg" % mones)
	else:
		kuva.save("life%d.jpg" % mones)

def Kehity(maa):
	#Jos solu on jossain laidassa ei yritetä laskea laidan yli meneviä soluja.
	#Luodaan muuttujat joilla pidetään kirjaa ympärillä olevista soluista ja onko solu jossain laidassa. Säännöt selitetty ylempänä.
	ylhaalla = False
	alhaalla = False
	oikealla = False
	vasemmalla = False
	ymparilla = 0
	
	#Luodaan uusi maa johon kirjataan uusi sukupolvi.
	uusiMaa = [0] * 100

	for i in range(100):
		uusiMaa[i] = [0] * 100
	
	for i in range(len(maa[0])):#korkeus
		for j in range(len(maa)):#leveys
			# Jos solu on jossain laidassa ei yritetä laskea laidan yli meneviä soluja.
			#Luodaan muuttujat joilla pidetään kirjaa ympärillä olevista soluista ja onko solu jossain laidassa. Säännöt selitetty ylempänä.
			ymparilla = 0
			ylhaalla = False
			alhaalla = False
			oikealla = False
			vasemmalla = False
			if j == 0:
				vasemmalla = True
			if j == 99:
				oikealla = True
			if i == 0:
				ylhaalla = True
			if i == 99:
				alhaalla = True
			
			#print(ylhaalla, alhaalla, oikealla, vasemmalla, j, i)
			
			#Laskevat tapaukset joissa solu ei ole raunalla
			if not ylhaalla and maa[j][i-1] == 1:
				ymparilla = ymparilla + 1
			if not alhaalla and maa[j][i+1] == 1:
				ymparilla = ymparilla + 1
			if not vasemmalla and maa[j-1][i] == 1:
				ymparilla = ymparilla + 1
			if not oikealla and maa[j+1][i] == 1:
				ymparilla = ymparilla + 1	
			if not ylhaalla and not vasemmalla and maa[j-1][i-1] == 1:
				ymparilla = ymparilla + 1
			if not ylhaalla and not oikealla and maa[j+1][i-1] == 1:
				ymparilla = ymparilla + 1
			if not alhaalla and not vasemmalla and maa[j-1][i+1] == 1:
				ymparilla = ymparilla + 1
			if not alhaalla and not oikealla and maa[j+1][i+1] == 1:
				ymparilla = ymparilla + 1
			
			#Laskevat ne tapaukset joissa jollakin laidoista niin että otetaan huomioon vastakkainen laita.
			if ylhaalla:
				if vasemmalla:
					if maa[99][i+1]:
						ymparilla = ymparilla + 1
					if maa[99][i]:
						ymparilla = ymparilla + 1
					if maa[99][99]:
						ymparilla = ymparilla + 1
					if maa[j][99]:
						ymparilla = ymparilla + 1
					if maa[j+1][99]:
						ymparilla = ymparilla + 1
				elif oikealla:
					if maa[j-1][99]:
						ymparilla = ymparilla + 1
					if maa[j][99]:
						ymparilla = ymparilla + 1
					if maa[0][99]:
						ymparilla = ymparilla + 1
					if maa[0][i]:
						ymparilla = ymparilla + 1
					if maa[0][+1]:
						ymparilla = ymparilla + 1
				else:
					if maa[j-1][99]:
						ymparilla = ymparilla + 1
					if maa[j][99]:
						ymparilla = ymparilla + 1
					if maa[j+1][99]:
						ymparilla = ymparilla + 1
						
			if alhaalla:
				if vasemmalla:
					if maa[j+1][0]:
						ymparilla = ymparilla + 1
					if maa[j][0]:
						ymparilla = ymparilla + 1
					if maa[99][0]:
						ymparilla = ymparilla + 1
					if maa[99][i]:
						ymparilla = ymparilla + 1
					if maa[99][i-1]:
						ymparilla = ymparilla + 1
				elif oikealla:
					if maa[0][i-1]:
						ymparilla = ymparilla + 1
					if maa[0][i]:
						ymparilla = ymparilla + 1
					if maa[0][0]:
						ymparilla = ymparilla + 1
					if maa[j][0]:
						ymparilla = ymparilla + 1
					if maa[j-1][0]:
						ymparilla = ymparilla + 1
				else:
					if maa[j-1][0]:
						ymparilla = ymparilla + 1
					if maa[j][0]:
						ymparilla = ymparilla + 1
					if maa[j+1][0]:
						ymparilla = ymparilla + 1
			
			if vasemmalla and not(ylhaalla or alhaalla):
				if maa[99][i-1]:
					ymparilla = ymparilla + 1
				if maa[99][i]:
					ymparilla = ymparilla + 1
				if maa[99][i+1]:
					ymparilla = ymparilla + 1
					
			if oikealla and not(ylhaalla or alhaalla):
				if maa[0][i-1]:
					ymparilla = ymparilla + 1
				if maa[0][i]:
					ymparilla = ymparilla + 1
				if maa[0][i+1]:
					ymparilla = ymparilla + 1
			
			#Rules
			if maa[j][i] == 1 and ymparilla < 2:
				uusiMaa[j][i] = 0
			elif maa[j][i] == 1 and (ymparilla == 2 or ymparilla == 3):
				uusiMaa[j][i] = 1
			elif maa[j][i] == 1 and ymparilla > 3:
				uusiMaa[j][i] = 0
			elif maa[j][i] == 0 and ymparilla == 3:
				uusiMaa[j][i] = 1
			else:
				uusiMaa[j][i] = 0
				
			if ymparilla == 1 and uusiMaa[j][i] > maa[j][i]:
				print("Ei toimi. 1")
			if ymparilla == 2 and uusiMaa[j][i] != maa[j][i]:
				print("Ei toimi. 2")
			if ymparilla > 3 and uusiMaa[j][i] == 1:
				print("Ei kuollut.")
	return uusiMaa
		
leveys = 100
korkeus = 100
mones = 0
maa = [0] * 100
eka = 0
valiMaa = 0
vertailuMaa = 0

for i in range(100):
	maa[i] = [0] * 100

# Luodaan ensimmainen ruutu
suhde = int(input("Anna solujen luonti suhde."))
for i in range(korkeus):
	for j in range(leveys):
		if randint(1, 100) <= suhde:
			maa[j][i] = 1
Tallenna(maa, mones)
mones = mones + 1

vertailuMaa = maa
for x in range(5000):
	maa = Kehity(maa)
	Tallenna(maa, mones)
	mones = mones + 1
	if x % 100 == 0:
		print(x)
	if eka == 0:
		valiMaa = maa
		eka = 1
	else:
		if maa == vertailuMaa:
			for y in range(10):
				maa = Kehity(maa)
				Tallenna(maa, mones)
				mones = mones + 1
			print("Loppu.")
			exit()
		else:
			vertailuMaa = valiMaa
			valiMaa = maa
