import os
from assets.XML import xmltodict
from assets.XML import xml_elements
from assets.scripts import *

class LevelLoader(object):
    def __init__(self, main):
        globals()["pygame"] = main.pygame
        self.main = main
        self.screen = self.main.screen
        self.loading = pygame.transform.smoothscale(\
            self.main.load_image("Screens/startscreens/loading_flat.nmt"), \
            self.main.settings["size"])
        self.modules = {}
        for key, value in globals().iteritems():
            if type(value).__name__ == "module":
                if value.__file__.find("assets"+os.sep+"scripts") != -1:
                    self.modules[key] = value
        names = filter(lambda k: k[:2]!="__", dir(xml_elements))
        self.parse_funcs = dict(zip([n.lower() for n in names], [xml_elements.__dict__[n] for n in names]))

    def load_file(self, filename):
        self.current_level_file = ("assets."+filename).replace(".", os.sep)+".xml"
        level_obj = open(self.current_level_file)
        self.current_level = xmltodict.parse(level_obj.read())
        level_obj.close()
        assert(self.current_level.keys() == ["page"])
        self.current_level = self.current_level["page"]
        self.script = self.current_level["@script"]
        assert(self.script in self.modules.keys())
        self.level_source = self.current_level["@source"]
        self.parse_source()
        for key in self.current_level.keys():
            if key in self.parse_funcs:
                if type(self.current_level[key]) != list:
                    self.parse_funcs[key](self.current_level[key])
                else:
                    for i in self.current_level[key]:
                        self.parse_funcs[key](i)

    def parse_source(self):
        source_obj = self.main.load_file("assets/"+self.level_source)
        self.current_source = xmltodict.parse(source_obj.read())
        source_obj.close()

    def run(self, events):
        pass
