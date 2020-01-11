import pygame

width = 500
height = 500
window = pygame.display.set_mode((width, height)) # Set up window instance
pygame.display.set_caption("Client") # Window caption

clientNumber = 0  # Keeps track of number of connected clients

# Player class represents rectangle that moves around the screen
class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)

    def draw(self, window):
        # Draw a rectangle that represents the player onto screen
        pygame.draw.rect(window, self.color, self.rect)

    


def redrawWindow():
    window.fill((255,255,255)) # Picks window color white
    pygame.display.update()


def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        redrawWindow()