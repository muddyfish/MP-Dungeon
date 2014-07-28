import tiles

class Game():
    def __init__(self, main, pygame):
        #Add the pygame module to the global variable list
        globals()["pygame"] = pygame
        globals()["main"] = main
        tiles.set_pygame(pygame)
        self.tile_grid_size = (13,7)
        self.grid = [[tiles.Fire() for i in range(self.tile_grid_size[0])] for j in range(self.tile_grid_size[1])]
            
    def run(self, events):
        main.screen.fill((122,0,0))
        for i, value in enumerate(self.grid):
            for j, sprite in enumerate(value):
                sprite.tile_tick()
                sprite.blit(main.screen, (j*sprite.im.get_size()[0],i*sprite.im.get_size()[1]))
