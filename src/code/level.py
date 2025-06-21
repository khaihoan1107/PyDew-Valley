import pygame 
from settings import *
from player import Player
import random

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        
        # sprite setup
        self.set_up()
        
    def set_up(self):
        self.player = Player((640, 360), self.all_sprites)

    def run(self,dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)