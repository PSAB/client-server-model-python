import pygame
from Network import Network
# from ast import literal_eval

width = 500
height = 500
window = pygame.display.set_mode((width, height))  # Set up window instance
pygame.display.set_caption("Client")  # Window caption

clientNumber = 0  # Keeps track of number of connected clients?


# Rectangle class represents rectangle that moves around the screen
class Rectangle():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height) # For ease of drawing
        self.speed = 3

    def draw(self, window):
        # Draw a rectangle that represents the user onto screen
        pygame.draw.rect(window, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed() # Returns a dictionary of all keys w/ values 1/0 if pressed/not pressed

        # Left Arrow key:
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            print((self.x, self.y))

        # Right Arrow key:
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
            print((self.x, self.y))

        # Up key
        if keys[pygame.K_UP]:
            self.y -= self.speed
            print((self.x, self.y))

        # Down key:
        if keys[pygame.K_DOWN]:
            self.y += self.speed
            print((self.x, self.y))

        self.rect = (self.x, self.y, self.width, self.height)

def read_position(str_):
    str_  = str_.split(',')
    return int(str_[0]), int(str_[1])

def make_position(tuple_):
    return str(tuple_[0]) + ',' + str(tuple_[1])

def redraw_window(window, rectangle):
    window.fill((255, 255, 255))  # Picks window color white
    rectangle.draw(window)

    pygame.display.update() # Update contents of display to the screen


def main():
    run = True
    n = Network()
    startPosition = read_position(n.getPosition()) # Starting position will arrive as tuple looking like: "(31, 74)"
    r = Rectangle(startPosition[0], startPosition[1], 100, 100, (0, 255, 0))  # Create rectangle object
    r2 = Rectangle(startPosition[0], startPosition[1], 100, 100, (0, 255, 0)) # Second rectangle object
    clock = pygame.time.Clock()



    while run:
       # Game Event handling
        for event in pygame.event.get():
            # Quitting mechanism triggers if the user click the window close button:
            if event.type == pygame.QUIT:
                print("Game has quit")
                run = False
                pygame.quit()

        r.move()  # Move Rectangle based on key being pressed
        redraw_window(window, r) # Keep updating the screen 24/7 unless game quits


main()