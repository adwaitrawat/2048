quit = False
size = height, width = 800, 600
side = 100
thickness = 2
state = [[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]
statep = state

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

import pygame, random

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("2048")

def left():
	for i in range(0,3):
		for j in range(0,4):
			if state[i][j] == state[i + 1][j] and state[i + 1][j] != 0 and state[i][j] != 0:
				state[i][j] += 1
				state[i + 1][j] = 0
			elif state[i + 1][j] == 0:
				pass
			elif state[i][j] == 0 and state[i + 1][j] != 0:
				state[i][j] = state[i + 1][j]
				state[i + 1][j] = 0
			
				

def right():
	for i in range(3,0,-1):
		for j in range(0,4):
			if state[i][j] == state[i - 1][j] and state[i - 1][j] != 0 and state[i][j] != 0:
				state[i][j] += 1
				state[i - 1][j] = 0
			elif state[i - 1][j] == 0:
				pass
			elif state[i][j] == 0 and state[i - 1][j] != 0:
				state[i][j] = state[i - 1][j]
				state[i - 1][j] = 0

def down():
	for i in range(0,4):
		for j in range(3,0,-1):
			if state[i][j] == state[i][j - 1] and state[i][j - 1] != 0 and state[i][j] != 0:
				state[i][j] += 1
				state[i][j - 1] = 0
			elif state[i][j - 1] == 0:
				pass
			elif state[i][j] == 0 and state[i][j - 1] != 0:
				state[i][j] = state[i][j - 1]
				state[i][j - 1] = 0

def up():
	for i in range(0,4):
		for j in range(0,3):
			if state[i][j] == state[i][j + 1] and state[i][j + 1] != 0 and state[i][j] != 0:
				state[i][j] += 1
				state[i][j + 1] = 0
			elif state[i][j + 1] == 0:
				pass
			elif state[i][j] == 0 and state[i][j + 1] != 0:
				state[i][j] = state[i][j + 1]
				state[i][j + 1] = 0

def rand_gen():
	tempx = random.randint(0,3)
	tempy = random.randint(0,3)
	if state[tempx][tempy] == 0:
		state[tempx][tempy] += 1
	else:
		rand_gen()
	

def grid():
	pygame.draw.rect(screen, White, (side, side, 4*side, 4*side), thickness)
	pygame.draw.line(screen, White, (2*side, side), (2*side, 5*side), thickness)
	pygame.draw.line(screen, White, (3*side, side), (3*side, 5*side), thickness)
	pygame.draw.line(screen, White, (4*side, side), (4*side, 5*side), thickness)
	pygame.draw.line(screen, White, (side, 2*side), (5*side, 2*side), thickness)
	pygame.draw.line(screen, White, (side, 3*side), (5*side, 3*side), thickness)
	pygame.draw.line(screen, White, (side, 4*side), (5*side, 4*side), thickness)

def display():
	screen.fill(Black)
	grid()
	for i in range(0,4):
		for j in range(0,4):
			if state[i][j] != 0:
				text = pygame.font.SysFont("comicsans",side//2)
				texts = text.render(str(pow(2,state[i][j])),True,Green)
				text_rect = texts.get_rect()
				text_rect.centerx = (i + 1)*side + side/2
				text_rect.centery = (j + 1)*side + side/2 
				screen.blit(texts, text_rect)
	pygame.display.update()

def keyboard():
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
			pygame.quit()
		if event.key == pygame.K_UP:
			for i in range(0,3):
				up()
			rand_gen()
		if event.key == pygame.K_DOWN:
			for i in range(0,3):
				down()
			rand_gen()
		if event.key == pygame.K_LEFT:
			for i in range(0,3):
				left()
			rand_gen()
		if event.key == pygame.K_RIGHT:
			for i in range(0,3):
				right()
			rand_gen()
		print(state)
		print(statep)

while True:
	display()
	for event in pygame.event.get():
		keyboard()
