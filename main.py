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
        pygame.draw.circle(canvas, circle_color, circle, radius)

def drawLines(circles):
    for circle1 in circles:
        for circle2 in circles:
            if circle1 != circle2:
                pygame.draw.line(canvas, line_color, circle1, circle2, width=1)

def colliding(location):
    for circle in circles:
        distance = math.sqrt((circle[0] - location[0])**2 + (circle[1] - location[1])**2)
        if distance < 2*radius + (radius / 2):
            return False
    return True

def circlePosition(location):
    for circle in circles:
        distance = math.sqrt((circle[0] - location[0])**2 + (circle[1] - location[1])**2)
        if distance <= radius:
            return circle


while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_position = pygame.mouse.get_pos()
            if colliding(mouse_position):
                circles.append(mouse_position)
            drawCircles(circles)
            clicked_circle = None
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_position = pygame.mouse.get_pos()
            if clicked_circle:
                circle_two = circlePosition(mouse_position)
                if circle_two:
                    if clicked_circle ==  circle_two:
                        clicked_circle = [clicked_circle[0],clicked_circle[1] - radius]
                        pygame.draw.circle(canvas, line_color, clicked_circle, radius, 1)
                        lines.append([circle_two, circle_two])
                        pygame.draw.circle(canvas, circle_color, circle_two, radius)
                        clicked_circle = None
                        break
                    pygame.draw.line(canvas, line_color, clicked_circle, circle_two, width=1)
                    lines.append([clicked_circle, circle_two])
                    pygame.draw.circle(canvas, circle_color, clicked_circle, radius)
                    pygame.draw.circle(canvas, circle_color, circle_two, radius)
                    clicked_circle = None
            else:
                clicked_circle = circlePosition(mouse_position)
                if clicked_circle:
                    pygame.draw.circle(canvas, red, clicked_circle, radius)

    pygame.display.update()