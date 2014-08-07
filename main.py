import pygame, glob, json, os, sys
from level_loader import LevelLoader

class Main:  
    def __init__(self):
        #Init pygame
        pygame.init()
        self.pygame = pygame
        self.load_settings()
        if self.settings["fullscreen"]: self.full = pygame.FULLSCREEN
        else: self.full = 0
        #Create the display
        self.screen = pygame.display.set_mode(tuple(self.settings["size"]), self.full) 
        pygame.display.set_caption("Fortix 2")
        self.font=pygame.font.SysFont("vervanda", 12)
        self.fps_colour = pygame.Color(255,255,255)
        self.clock=pygame.time.Clock()
        self.level_loader = LevelLoader(self)
        self.started = False
        self.copyright = pygame.transform.smoothscale(\
            self.load_image("Screens/startscreens/nemesys_flat.nmt"), \
            self.settings["size"])

    def run(self):
        while 1:
            self.clock.tick(60)
            events = pygame.event.get()
            for event in events: #Events that are always done
                if event.type == pygame.QUIT: self.exit()
                elif event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_BACKSPACE: self.screenshot()
                    if event.key == pygame.K_ESCAPE: self.exit()
            message = self.font.render("FPS: %d"%(self.clock.get_fps()), True, self.fps_colour)
            if not self.started: self.display_copyright()
            else: self.level_loader.run(events)
            self.screen.blit(message, (10, 10))
            pygame.display.flip()

    def display_copyright(self):
        self.screen.fill((0,0,0))
        ticks = pygame.time.get_ticks()
        if 1000 < ticks < 4000:
            self.copyright.set_alpha((1500-max(abs(2500.0-ticks), 500))*0.256)
            self.screen.blit(self.copyright, (0,0))
        self.started = True#9000 < ticks
        if self.started: self.level_loader.load_file("menu_steam.main_menu")

    def screenshot(self):
        print("Screenshot")
        screenshots = [int(screenshot[25:-4]) for screenshot in glob.glob("./Screenshots/screenshot_*.png")]
        if screenshots == []: screenshot_num = 1
        else: screenshot_num = max(screenshots)
        pygame.image.save(self.screen, "Screenshots/screenshot_%s.png" %(screenshot_num))

    def exit(self):
        pygame.quit()
        sys.exit()

    def load_settings(self):
        file_obj = open("settings.json")
        self.settings = json.load(file_obj)
        file_obj.close()

    def save_settings(self, data):
        file_obj = open("settings.json", "w")
        self.settings = json.dump(file_obj)
        file_obj.close()

    def load_file(self, filename_orig):
        return open(filename_orig.replace("/", os.sep))

    def load_image(self, texture_location):
        if texture_location[0] == "/": texture_location = texture_location[1:]
        image = pygame.image.load(self.load_file("assets/textures/"+texture_location), ".tga")
        return image

def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    main = Main()
    main.run()

if __name__ == "__main__":
    main()
