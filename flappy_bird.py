# Using the Object Oriented Procedure to create the objects in the game window such as bird, background, pipes, base..
# Using the installed pygame module

import pygame
import os
import time

# Initializing font inside game window
pygame.font.init()
STAT_FONT = pygame.font.SysFont("comicsans", 50)
END_FONT = pygame.font.SysFont("comicsans", 70)


# Parameters to create the game window
WIN_WIDTH = 288
WIN_HEIGHT = 512
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
FPS = 30

# Loading the images into the game window
BIRD_IMAGES = [ pygame.image.load(os.path.join("images", "bird1.png")),
                pygame.image.load(os.path.join("images", "bird2.png")),
                pygame.image.load(os.path.join("images", "bird3.png")) ]
PIPE_IMAGE = pygame.image.load(os.path.join("images", "pipe.png"))
BASE_IMAGE = pygame.image.load(os.path.join("images", "base.png"))
BG_IMAGE = pygame.image.load(os.path.join("images", "bg.png"))

# Creating the Bird class
class Bird:
    IMAGES = BIRD_IMAGES
    MAX_ROTATION = 25   # Degrees
    ROT_VELOCITY = 20   # How much we rotate the bird every time we move it
    ANIMATION_TIME = 5  # How long we are going to show each bird animation (How fast bird flaps the wings)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y  # (x,y) represent the starting position of the bird on the game window
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMAGES[0]
        
    def jump(self):
        self.vel = -10.5    # Positive directions are towards right and down from top-left corner
        self.tick_count = 0
        self.height = self.y
        
    def move(self):
        self.tick_count += 1
        d = self.vel*self.tick_count + 1.5*self.tick_count**2   # Parabolic arc movement for the bird to reperesent gravity
        
        if d >= 16:
            d = 16
            
        if d <= 0:
            d -= 2
            
        self.y = self.y + d
        
        # Tilting the bird according to its position and movement on the game window
        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VELOCITY
                
    def draw(self, win):
        self.img_count += 1
        # Deciding which image to show based on the current img_count
        # Gives the Flapping Animation of the bird if we show in the order (0-1-2-1-0)
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMAGES[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMAGES[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMAGES[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMAGES[1]
        elif self.img_count < self.ANIMATION_TIME*4 + 1:
            self.img = self.IMAGES[0]
            self.img_count = 0
        
        if self.tilt <= -80:        # When Nose-diving downward
            self.img = self.IMAGES[1]
            self.img_count = self.ANIMATION_TIME*2
        
        # Rotate the image with the helper function
        blitRotateCenter(win, self.img, (self.x, self.y), self.tilt)
     
    # Function for pixel perfect collision between pipes and bird   
    def get_mask(self):
        return pygame.mask.from_surface(self.img)
        

# Rotate the image with the recieved parameters
def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    
    surf.blit(rotated_image, new_rect.topleft)

def draw_window(win, bird):         # blit simply means draw as a pygame function
    win.blit(BG_IMAGE, (0,0))
    bird.draw(win)
    pygame.display.update()
    
def main():
    bird = Bird(50,200)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(win, bird)
        
    pygame.quit()
    quit()
    
main()