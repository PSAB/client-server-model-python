import pygame

width = 500
height = 500
window = pygame.display.set_mode((width, height)) # Set up window instance
pygame.display.set_caption("Client") # Window caption

clientNumber = 0  # Keeps track of number of connected clients

def redrawWindow():
    window.fill(255,255,255)
    pygame.display.update()