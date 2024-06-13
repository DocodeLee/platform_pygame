import sys
import pygame

from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEntity

class Game:
    def __init__(self):
        pygame.init()
        
        # set the window title
        pygame.display.set_caption("Platform Runner")
        ## the window size
        self.screen = pygame.display.set_mode((640, 480))
        ## where i actually render
        self.display = pygame.Surface((320, 240))
        
        #help to track the time
        self.clock = pygame.time.Clock()
        
        self.movement = [False, False]
        
        self.assets ={
            "decor" : load_images('tiles/decor'),
            "player" : load_image('entities/player.png')
        }
        
        self.player = PhysicsEntity(self,'player',(50,50),(8, 15))
        #to

    def run(self):
        while True:
            #clearing the background is necessary
            self.display.fill((14,210,247))
            
            self.player.update((self.movement[1] - self.movement[0],0))
            self.player.render_player(self.display)
            
            ##In SDL user has to handle the input, if you didn't pygame doesnt respond
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                        
            #showing the screen(transform the scale to the screen size)
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()),(0, 0))
            #update the display, at the screen var we set the display and update by this
            pygame.display.update()
            self.clock.tick(60) #60fps
            
## since you define at the class you need to make instance
game = Game()
game.run()