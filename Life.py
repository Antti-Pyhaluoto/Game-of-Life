from PIL import Image
from random import randint

#Rules to game of life
# Any live cell with fewer than two live neighbors dies, as if by under population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by overpopulation.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction

def Save(earth, iteration):
	image = Image.new("RGB", (1000, 1000), color = "white")

	for i in range(len(earth[0])):
		for j in range(len(earth)):
			if earth[j][i] == 1:
				image.paste( Image.new("RGB", (10, 10), color = "black"), (10*j, 10*i))
	#image.show()
	if iteration < 10:
		image.save("life000%d.jpg" % iteration)
	elif iteration < 100:
		image.save("life00%d.jpg" % iteration)
	elif iteration < 1000:
		image.save("life0%d.jpg" % iteration)
	else:
		image.save("life%d.jpg" % iteration)

def Evolve(earth):
	# Creating a new earth where the new iteration is recorded.
	newEarth = [0] * 100

	for i in range(100):
		newEarth[i] = [0] * 100
	
	for i in range(len(earth[0])):#height
		for j in range(len(earth)):#width
			# Creating the variables to keep track of surrounding cells and if the cell is on edge. Rules explained above.
			around = 0
			up = False
			down = False
			right = False
			left = False
			if j == 0:
				left = True
			if j == 99:
				right = True
			if i == 0:
				up = True
			if i == 99:
				down = True
			
			#print(up, down, right, left, j, i)
			
			# Calculates cases where the cell is not at edge.
			if not up and earth[j][i-1] == 1:
				around = around + 1
			if not down and earth[j][i+1] == 1:
				around = around + 1
			if not left and earth[j-1][i] == 1:
				around = around + 1
			if not right and earth[j+1][i] == 1:
				around = around + 1	
			if not up and not left and earth[j-1][i-1] == 1:
				around = around + 1
			if not up and not right and earth[j+1][i-1] == 1:
				around = around + 1
			if not down and not left and earth[j-1][i+1] == 1:
				around = around + 1
			if not down and not right and earth[j+1][i+1] == 1:
				around = around + 1
			
			#Laskevat ne tapaukset joissa jollakin laidoista niin että otetaan huomioon vastakkainen laita.
			# Calculates cases where the cell is at some edge and takes the cells at opposite side into account.
			if up:
				if left:
					if earth[99][i+1]:
						around = around + 1
					if earth[99][i]:
						around = around + 1
					if earth[99][99]:
						around = around + 1
					if earth[j][99]:
						around = around + 1
					if earth[j+1][99]:
						around = around + 1
				elif right:
					if earth[j-1][99]:
						around = around + 1
					if earth[j][99]:
						around = around + 1
					if earth[0][99]:
						around = around + 1
					if earth[0][i]:
						around = around + 1
					if earth[0][+1]:
						around = around + 1
				else:
					if earth[j-1][99]:
						around = around + 1
					if earth[j][99]:
						around = around + 1
					if earth[j+1][99]:
						around = around + 1
						
			if down:
				if left:
					if earth[j+1][0]:
						around = around + 1
					if earth[j][0]:
						around = around + 1
					if earth[99][0]:
						around = around + 1
					if earth[99][i]:
						around = around + 1
					if earth[99][i-1]:
						around = around + 1
				elif right:
					if earth[0][i-1]:
						around = around + 1
					if earth[0][i]:
						around = around + 1
					if earth[0][0]:
						around = around + 1
					if earth[j][0]:
						around = around + 1
					if earth[j-1][0]:
						around = around + 1
				else:
					if earth[j-1][0]:
						around = around + 1
					if earth[j][0]:
						around = around + 1
					if earth[j+1][0]:
						around = around + 1
			
			if left and not(up or down):
				if earth[99][i-1]:
					around = around + 1
				if earth[99][i]:
					around = around + 1
				if earth[99][i+1]:
					around = around + 1
					
			if right and not(up or down):
				if earth[0][i-1]:
					around = around + 1
				if earth[0][i]:
					around = around + 1
				if earth[0][i+1]:
					around = around + 1
			
			#Rules
			if earth[j][i] == 1 and around < 2:
				newEarth[j][i] = 0
			elif earth[j][i] == 1 and (around == 2 or around == 3):
				newEarth[j][i] = 1
			elif earth[j][i] == 1 and around > 3:
				newEarth[j][i] = 0
			elif earth[j][i] == 0 and around == 3:
				newEarth[j][i] = 1
			else:
				newEarth[j][i] = 0
	return newEarth
		
width = 100
height = 100
iteration = 0
earth = [0] * 100
first = 0
tempEarth = 0
compareEarth = 0

for i in range(100):
	earth[i] = [0] * 100

# Creating the first iteration
ratio = int(input("Give ratio for alive cells(0-100):"))
amount = int(input("Give max number of iterations:"))
for i in range(height):
	for j in range(width):
		if randint(1, 100) <= ratio:
			earth[j][i] = 1
Save(earth, iteration)
iteration = iteration + 1

compareEarth = earth
for x in range(amount):
	earth = Evolve(earth)
	Save(earth, iteration)
	iteration = iteration + 1
	if x % 100 == 0:
		print(x)
	if first == 0:
		tempEarth = earth
		first = 1
	else:
		# Compares current earth to earth 2 iteratons ago to detect when everything has settled down.
		if earth == compareEarth:
			for y in range(10):
				earth = Evolve(earth)
				Save(earth, iteration)
				iteration = iteration + 1
			print("End.")
			exit()
		else:
			compareEarth = tempEarth
			tempEarth = earth
