# Tron
# A remake of the classic arcade gamer Tron
# Date 7/7/24
# Created by: Yoshi Gamer 360

# -- Player 1 uses WASD to move
# -- Player 2 uses arrow keys to move
# -- Player 3 uses UHJK keys to move
# -- Player 4 uses TFGH keys to move

# Libraries
import pygame, time

# Start game engine
pygame.init()

# Define colour variables
colourBackground = (1, 4, 59)
colourPlayer1 = (0, 255, 17)
colourPlayer2 = (255, 234, 0)
colourPlayer3 = (0, 247, 255)
colourPlayer4 = (255, 0, 212)
colourWalls = (0, 1, 10)
colourText = (221, 222, 240)

# Player class
class Player:
    def __init__(self, x, y , bearing , colour, alive=True):
        self.x = x
        self.y = y
        self.bearing = bearing
        self.colour = colour
        self.speed = 1
        self.rect = pygame.Rect(self.x -1, self.y -1, 2, 2)
        self.alive = alive

    def draw(self):
        self.rect = pygame.Rect(self.x -1, self.y -1, 2, 2)
        pygame.draw.rect(screen, self.colour, self.rect, 0)

    def move(self):
        if self.alive:
            self.x += self.bearing[0]
            self.y += self.bearing[1]

# New game function - to create players
def newGame():
    newP1 = Player(50, height / 2, (2, 0), colourPlayer1)
    newP2 = Player(width - 50, height / 2, (-2, 0), colourPlayer2)
    newP3 = Player(width / 2, height - 50, (0, -2), colourPlayer3)
    newP4 = Player(width / 2, 50, (0, 2), colourPlayer4)
    return newP1, newP2, newP3, newP4

# Set up the game window
width, height = 600, 600
offset = 0
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tron by Yoshi_Gamer_360")

# Font and clock
font = pygame.font.SysFont("Centaur", 72)
clock = pygame.time.Clock()
checkTime = time.time()
