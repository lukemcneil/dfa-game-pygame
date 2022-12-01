import pygame
import math
from draw_dfa import drawDFA, RADIUS
from dfa_types import State, DFA

pygame.init()

canvas = pygame.display.set_mode((500, 500))

pygame.display.set_caption("DFA main board")
exit = False

dfa = DFA([])
clicked_circle : "State | None" = None
dragged_state : "State | None" = None
selected_letter : str = "0"

def canPutCircleHere(location):
	for circle in dfa.states:
		distance = math.sqrt((circle.position[0] - location[0])**2 + (circle.position[1] - location[1])**2)
		if distance < 2*RADIUS + (RADIUS / 2):
			return False
	return True

def getCircleAtPosition(location):
	for circle in dfa.states:
		distance = math.sqrt((circle.position[0] - location[0])**2 + (circle.position[1] - location[1])**2)
		if distance <= RADIUS:
			return circle

def removeEdges(removedState):
	for state in dfa.states:
		for letter in list(state.edges.keys()):
			if state.edges[letter] == removedState:
				state.edges.pop(letter)

drawDFA(canvas, dfa, selected_letter)
while not exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #left click
			mouse_position = pygame.mouse.get_pos()
			if canPutCircleHere(mouse_position):
				new_state = State(list(mouse_position))
				dfa.states.append(new_state)
				if len(dfa.states) == 1:
					dfa.start_state = new_state
				dragged_circle = None
			else:
				dragged_state = getCircleAtPosition(mouse_position)
			if clicked_circle:
				clicked_circle.selected = False
				clicked_circle = None
		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				dragged_state = None
		elif event.type == pygame.MOUSEMOTION:
			if (dragged_state):
				dx, dy = event.rel
				dragged_state.position[0] += dx
				dragged_state.position[1] += dy
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2: # middle click
			state_middle_clicked = getCircleAtPosition(pygame.mouse.get_pos())
			if state_middle_clicked:
				dfa.states.remove(state_middle_clicked)
				removeEdges(state_middle_clicked)
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: #right click
			mouse_position = pygame.mouse.get_pos()
			if clicked_circle:
				circle_two = getCircleAtPosition(mouse_position)
				if circle_two:
					clicked_circle.edges[selected_letter] = circle_two
				clicked_circle.selected = False
				clicked_circle = None
			else:
				clicked_circle = getCircleAtPosition(mouse_position)
				if clicked_circle:
					clicked_circle.selected = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_0:
				selected_letter = "0"
			elif event.key == pygame.K_1:
				selected_letter = "1"
			elif event.key == pygame.K_e:
				circle_at_pos = getCircleAtPosition(pygame.mouse.get_pos())
				if circle_at_pos:
					circle_at_pos.is_accept_state = not circle_at_pos.is_accept_state
			elif event.key == pygame.K_s:
				dfa.start_state = getCircleAtPosition(pygame.mouse.get_pos())
			elif event.key == pygame.K_RETURN:
				print(dfa.run("001"))

	drawDFA(canvas, dfa, selected_letter)

	pygame.display.update()
