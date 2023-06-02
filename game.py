import pygame
import sys
from alchemy import * 


pygame.init()

screen = pygame.display.set_mode((1000,800))
sidebar_rect = pygame.Rect(900, 0, 200, 800)  # x, y, width, height

element_pos = [400,300]
dragging = False
scroll_offset = 0
scrollbar = ScrollBar((880, 0), sidebar_rect.height)

#loop
# ... Rest of your game.py code ...

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for element in elements:
                    if element.sidebar_rect and element.sidebar_rect.collidepoint(event.pos):
                        if element.unlocked:
                            element.dragging = True
                        break  # Stop checking other elements
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                for element in elements:
                    if element.dragging:
                        element.dragging = False
                        break  # Stop checking other elements
        elif event.type == pygame.MOUSEMOTION:
            for element in elements:
                if element.dragging:
                    element.position = list(event.pos)

    screen.fill((48, 25, 52))
    sidebar_color = (60, 40, 70)
    pygame.draw.rect(screen, sidebar_color, sidebar_rect)

    # Draw elements and the scrollbar
    for ele in elements:
        if ele.unlocked:
            ele.draw_in_sidebar(screen, ele.sidebar_position)
            if ele.dragging:
                ele.position = pygame.mouse.get_pos()
                ele.draw(screen)

    scrollbar.draw(screen)

    pygame.display.update()
