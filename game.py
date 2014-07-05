class Game():
    def __init__(self, main, pygame):
        #Add the pygame module to the global variable list
        globals()["pygame"] = pygame
        globals()["main"] = main
        self.tile_grid_size = (10,6)
        input_im = pygame.image.load("Backgrounds/0.png")
        im_x, im_y = input_im.get_size()
        self.ims = []
        for x in range(1, im_x, 25):
            for y in range(1, im_y, 25):
                surf = pygame.Surface((24,24))
                surf.blit(input_im, (1-x,1-y))
                self.ims.append(surf)
            
    def run(self, events):
        for i in range(len(self.ims)):
                main.screen.blit(self.ims[i], (i*24,0))
