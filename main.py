import pygame
import math

pygame.init()

canvas = pygame.display.set_mode((500, 500))

pygame.display.set_caption("DFA main board")
exit = False

RADIUS = 20
LINE_WIDTH = 3
CIRCLE_COLOR = [255,255,255]
SELECTED_CIRCLE_COLOR = [255,0,0]
LINE_COLOR = [255,0,255]
BACKGROUND_COLOR = [0, 0, 0]

class State:
	def __init__(self, position):
		self.position : list[int, int] = position
		self.selected : bool = False

class Edge:
	def __init__(self, start_state, end_state, letter):
		self.start_state : State = start_state
		self.end_state : State = end_state
		self.letter : str = letter

states : "list[State]" = []
edges : "list[Edge]" = []
clicked_circle = None
selected_letter = "0"
font = pygame.font.SysFont(None, 25)

def drawStates():
	for state in states:
		color = CIRCLE_COLOR if not state.selected else SELECTED_CIRCLE_COLOR
		pygame.draw.circle(canvas, color, state.position, RADIUS)

def drawEdges():
	for edge in edges:
		start = edge.start_state.position
		end = edge.end_state.position
		if start == end:
			self_arrow_center = [start[0], start[1] - RADIUS]
			pygame.draw.circle(canvas, LINE_COLOR, self_arrow_center, RADIUS, 1)
			text_position = [self_arrow_center[0]-RADIUS/3, self_arrow_center[1] - RADIUS * 2]
			show_text(edge.letter, LINE_COLOR, text_position)
		else:
			pygame.draw.line(canvas, LINE_COLOR, start, end, width=1)
			midpoint = [(start[0] + end[0]) / 2, (start[1] + end[1]) / 2]
			show_text(edge.letter, LINE_COLOR, midpoint)

def drawSelectedLetter():
	show_text("letter: " + selected_letter, LINE_COLOR, [10, 10])
	pass

def drawDFA():
	canvas.fill(BACKGROUND_COLOR)
	drawEdges()
	drawStates()
	drawSelectedLetter()

def getCircleCollidingWith(location):
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

def show_text( msg, color, position):
	text = font.render( msg, True, color)
	canvas.blit(text, position)

drawDFA()
while not exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #left click
			mouse_position = pygame.mouse.get_pos()
			if getCircleCollidingWith(mouse_position):
				new_state = State(list(mouse_position))
				states.append(new_state)
			if clicked_circle:
				clicked_circle.selected = False
				clicked_circle = None
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
	drawDFA()

	pygame.display.update()
