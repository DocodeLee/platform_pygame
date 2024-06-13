import pygame

BASE_IMAGE_PATH = 'data/images/'


def load_image(path):
    img = pygame.image.load(BASE_IMAGE_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    
    #if you don't do return the result will be none
    return img