import pygame
from gameObject import gameObject
from typing import List
class window:
    def __init__(self, h:int, w:int, name:str, objlist:List[gameObject]):
        self.h = h
        self.w = w
        self.name = name
        self.running = True
        self.objlist = objlist
        self.clock = pygame.time.Clock()
        pygame.init()
        screen = pygame.display.set_mode((self.h, self.w))
        pygame.display.set_caption(self.name)
        for obj in self.objlist:
            obj.surf = screen
        while self.running:
            self.clock.tick(10)
            pygame.display.flip()
            screen.fill((0,0,0))
            for obj in self.objlist:
                obj.draw()
            for obj in self.objlist:
                obj.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()