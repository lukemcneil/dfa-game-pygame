import pygame
import math
from drawDFA import drawDFA, RADIUS

pygame.init()

canvas = pygame.display.set_mode((500, 500))

pygame.display.set_caption("DFA main board")
exit = False

class State:
	def __init__(self, position):
		self.position : list[int, int] = position
		self.selected : bool = False
		self.dragging : bool = False

class Edge:
	def __init__(self, start_state, end_state, letter):
		self.start_state : State = start_state
		self.end_state : State = end_state
		self.letter : str = letter

states : "list[State]" = []
edges : "list[Edge]" = []
clicked_circle : State = None
dragged_state : State = None
selected_letter : str = "0"

offset_x = 0
offset_y = 0

def canPutCircleHere(location):
	for circle in states:
		distance = math.sqrt((circle.position[0] - location[0])**2 + (circle.position[1] - location[1])**2)
		if distance < 2*RADIUS + (RADIUS / 2):
			return False
	return True

def getCircleAtPosition(location):
	for circle in states:
		distance = math.sqrt((circle.position[0] - location[0])**2 + (circle.position[1] - location[1])**2)
		if distance <= RADIUS:
			return circle

def removeEdges(removedState):
	global edges
	new_edges = []
	for edge in edges:
		if edge.start_state != removedState and edge.end_state != removedState:
			new_edges.append(edge)
	edges = new_edges

drawDFA(canvas, states, edges, selected_letter)
while not exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #left click
			mouse_position = pygame.mouse.get_pos()
			if canPutCircleHere(mouse_position):
				new_state = State(list(mouse_position))
				states.append(new_state)
				dragged_circle = None
			else:
				dragged_state = getCircleAtPosition(mouse_position)
				if dragged_state:
					dragged_state.dragging = True
					mouse_x, mouse_y = mouse_position
					offset_x = dragged_state.position[0] - mouse_x
					offset_y = dragged_state.position[1] - mouse_y
			if clicked_circle:
				clicked_circle.selected = False
				clicked_circle = None
		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:            
				dragged_state = False
		elif event.type == pygame.MOUSEMOTION:
			if (dragged_state):
				mouse_x, mouse_y = pygame.mouse.get_pos()
				dragged_state.position[0] = mouse_x + offset_x
				dragged_state.position[1] = mouse_y	+ offset_y
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2: # middle click
			state_middle_clicked = getCircleAtPosition(pygame.mouse.get_pos())
			states.remove(state_middle_clicked)
			removeEdges(state_middle_clicked)
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: #right click
			mouse_position = pygame.mouse.get_pos()
			if clicked_circle:
				circle_two = getCircleAtPosition(mouse_position)
				if circle_two:
					edges.append(Edge(clicked_circle, circle_two, selected_letter))
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
	drawDFA(canvas, states, edges, selected_letter)

	pygame.display.update()
