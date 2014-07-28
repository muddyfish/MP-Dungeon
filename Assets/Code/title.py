class Title(object):
    def __init__(self, main, levelname):
        globals()["pygame"] = main.pygame
        self.main = main
        self.screen = self.main.screen
        self.copyright = pygame.transform.smoothscale(main.load_image("Screens/startscreens/nemesys_flat.nmt"), self.screen.get_size())
        self.fortix = pygame.transform.smoothscale(main.load_image("Screens/startscreens/loading_flat.nmt"), self.screen.get_size())

    def run(self, events):
        self.screen.fill((0,0,0))
        ticks = pygame.time.get_ticks()
        if 1000 < ticks < 4000:
            self.copyright.set_alpha((1500-max(abs(2500.0-ticks), 500))*0.256)
            self.screen.blit(self.copyright, (0,0))
        if 5000 < ticks < 8000:
            self.fortix.set_alpha((1500-max(abs(6500.0-ticks), 500))*0.256)
            self.screen.blit(self.fortix, (0,0))
        if 9000 < ticks:
            self.main.set_controller("main_menu")
        for event in events:
            if event.type in [2,3,5,6]:
                self.main.set_controller("main_menu")
