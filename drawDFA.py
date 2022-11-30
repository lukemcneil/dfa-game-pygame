import pygame
import math

pygame.init()

RADIUS = 20
LINE_WIDTH = 3
CIRCLE_COLOR = [255,255,255]
SELECTED_CIRCLE_COLOR = [255,0,0]
LINE_COLOR = [255,0,255]
BACKGROUND_COLOR = [0, 0, 0]
ARROW_HEIGHT = 10
ARROW_WIDTH = 10
FONT = pygame.font.SysFont("", 25)

def drawStates(canvas, states):
	for state in states:
		color = CIRCLE_COLOR if not state.selected else SELECTED_CIRCLE_COLOR
		pygame.draw.circle(canvas, color, state.position, RADIUS)

def translatePoint(point, angle, distance):
	return [point[0] - (distance * math.cos(angle)), point[1] + (distance * math.sin(angle))]

def drawEdges(canvas, edges):
	for edge in edges:
		start = edge.start_state.position
		end = edge.end_state.position
		if start == end:
			self_arrow_center = [start[0], start[1] - RADIUS]
			pygame.draw.circle(canvas, LINE_COLOR, self_arrow_center, RADIUS, 1)
			text_position = [self_arrow_center[0]-RADIUS/3, self_arrow_center[1] - RADIUS * 2]
			show_text(canvas, edge.letter, LINE_COLOR, text_position)
		else:
			pygame.draw.line(canvas, LINE_COLOR, start, end, width=1)
			dy = end[1] - start[1]
			dx = end[0] - start[0]
			angle = math.atan2(-dy, dx)
			point1 = translatePoint(end, angle, RADIUS)
			point2 = translatePoint(translatePoint(point1, angle - math.pi/2, ARROW_HEIGHT), angle, ARROW_WIDTH)
			point3 = translatePoint(translatePoint(point1, angle + math.pi/2, ARROW_HEIGHT), angle, ARROW_WIDTH)
			pygame.draw.polygon(canvas, LINE_COLOR, [point1, point2, point3])
			midpoint = [(start[0] + end[0]) / 2, (start[1] + end[1]) / 2]
			show_text(canvas, edge.letter, LINE_COLOR, midpoint)

def drawSelectedLetter(canvas, selected_letter):
	show_text(canvas, "letter: " + selected_letter, LINE_COLOR, [10, 10])
	pass

def show_text(canvas, msg, color, position):
	text = FONT.render( msg, True, color)
	canvas.blit(text, position)

def drawDFA(canvas, states, edges, selected_letter):
	canvas.fill(BACKGROUND_COLOR)
	drawEdges(canvas, edges)
	drawStates(canvas, states)
	drawSelectedLetter(canvas, selected_letter)