# Using the Object Oriented Procedure to create the objects in the game window such as bird, background, pipes, base..
# Using the installed pygame module

import pygame
import os
import random

# Initializing font inside game window to draw useful info like score and how many birds are alive at each generation
pygame.font.init()
STAT_FONT = pygame.font.SysFont("comicsans", 20)
END_FONT = pygame.font.SysFont("comicsans", 30)


# Parameters to create the game window
WIN_WIDTH = 288
WIN_HEIGHT = 512
FLOOR = 450
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

# Creating the Pipe Class
class Pipe:
    GAP = 100   #? Gap between the two pipes
    VEL = -5     # Velocity at which the pipe should be moved towards the bird
    
    def __init__(self, x):
        self.x = x
        self.height = 0
        
        self.top = 0        # Co-ordinates for the TOP PIPE
        self.bottom = 0     # Co-ordinates for the BOTTOM PIPE
        self.PIPE_BOTTOM = PIPE_IMAGE
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMAGE, False, True)  # Flips the pipe image to get the top pipe
        
        self.passed = False
        self.set_height()   # Create the gaps in the pipe randomly with helper function
        
    def set_height(self):
        self.height = random.randrange(30, 300) #?
        self.top = self.height - self.PIPE_TOP.get_height()     # TP CO-ordinates
        self.bottom = self.height + self.GAP                    # BP CO-ordinates
        
    def move(self):
        self.x += self.VEL
        
    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))
        
    # Pixel Perfect Collision between pipe edges and Bird using the masks concept where the actual pixels are
    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))
        
        bottom_collision = bird_mask.overlap(bottom_mask, bottom_offset)
        top_collision = bird_mask.overlap(top_mask, top_offset)
        
        # Checks for collision and returns true if there is collision
        if top_collision or bottom_collision:
            return True
        return False
        

# Creating the Base Class        
class Base:
    VEL = -5        # Same as that of the pipe
    WIDTH = BASE_IMAGE.get_width()
    IMG = BASE_IMAGE
    
    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
        
    def move(self):
        self.x1 += self.VEL
        self.x2 += self.VEL
        
        
        # If a picture has completed the rotation, get it back to the third picture's back
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH
            
            
    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))
        
        

# Rotate the image with the recieved parameters
def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    
    surf.blit(rotated_image, new_rect.topleft)

def draw_window(win, bird, pipes, base, score):         # blit simply means draw as a pygame function
    win.blit(BG_IMAGE, (0,0))
    
    for pipe in pipes:
        pipe.draw(win)
    
    text = STAT_FONT.render("Score: " + str(score), 1, (255,255,255))
    win.blit(text, (WIN_WIDTH - 5 - text.get_width(), 5))
        
    base.draw(win)
    
    bird.draw(win)
    pygame.display.update()
    
def main():
    score = 0
    bird = Bird(50,200)
    base = Base(FLOOR)
    pipes = [Pipe(400)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #bird.move()
        add_pipe = False
        remove_pipes = []
        
        # Move pipes
        for pipe in pipes:
            if pipe.collide(bird):      # Modify later
                pass
            
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                remove_pipes.append(pipe)
            
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True
                
            pipe.move()
            
        if add_pipe:
            score += 1
            pipes.append(Pipe(300))
            
        for r in remove_pipes:
            pipes.remove(r)
        
        if bird.y + bird.img.get_height() >= FLOOR:
            pass                                        # Modify
        
        # Move Base
        base.move()
        
        draw_window(win, bird, pipes, base, score)
        
    pygame.quit()
    quit()
    
main()