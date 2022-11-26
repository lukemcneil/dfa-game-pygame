import pygame
import random
import math

pygame.init()

# CREATING CANVAS
canvas = pygame.display.set_mode((500, 500))

# TITLE OF CANVAS
pygame.display.set_caption("DFA main board")
exit = False

radius = 20
line_width = 3
circle_color = [255,255,255]
line_color = [255,0,255]
red = [255,0,0]

circles = []
lines = []
clicked_circle = None

def drawCircles(circles):
    for circle in circles:
        pygame.draw.circle(canvas, circle_color, circle.position, radius)

def drawLines(circles):
    for circle1 in circles:
        for circle2 in circles:
            if circle1 != circle2:
                pygame.draw.line(canvas, line_color, circle1, circle2, width=1)

def colliding(location):
    for circle in circles:
        distance = math.sqrt((circle.position[0] - location[0])**2 + (circle.position[1] - location[1])**2)
        if distance < 2*radius + (radius / 2):
            return False
    return True

def circlePosition(location):
    for circle in circles:
        distance = math.sqrt((circle.position[0] - location[0])**2 + (circle.position[1] - location[1])**2)
        if distance <= radius:
            return circle

class State:
  def __init__(self, position):
    self.position = position

class Edge:
  def __init__(self, start_state, end_state, letter):
    self.start_state = start_state
    self.end_state = end_state
    self.letter



while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_position = pygame.mouse.get_pos()
            if colliding(mouse_position):
                new_state = State(mouse_position)
                circles.append(new_state)
            drawCircles(circles)
            clicked_circle = None
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_position = pygame.mouse.get_pos()
            if clicked_circle:
                circle_two = circlePosition(mouse_position)
                if circle_two:
                    if clicked_circle ==  circle_two:
                        self_arrow_center = [clicked_circle.position[0],clicked_circle.position[1] - radius]
                        pygame.draw.circle(canvas, line_color, self_arrow_center, radius, 1)
                        lines.append([circle_two.position, circle_two.position])
                        pygame.draw.circle(canvas, circle_color, circle_two.position, radius)
                        clicked_circle = None
                        break
                    pygame.draw.line(canvas, line_color, clicked_circle.position, circle_two.position, width=1)
                    lines.append([clicked_circle, circle_two])
                    pygame.draw.circle(canvas, circle_color, clicked_circle.position, radius)
                    pygame.draw.circle(canvas, circle_color, circle_two.position, radius)
                    clicked_circle = None
                else:
                    pygame.draw.circle(canvas, circle_color, clicked_circle.position, radius)
                    clicked_circle = None
            else:
                clicked_circle = circlePosition(mouse_position)
                if clicked_circle:
                    pygame.draw.circle(canvas, red, clicked_circle.position, radius)

    pygame.display.update()
