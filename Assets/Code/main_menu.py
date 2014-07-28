import xmltodict
import xml_elements

class MainMenu(object):
    def __init__(self, main, levelname):
        globals()["pygame"] = main.pygame
        self.main = main
        self.screen = self.main.screen
        self.main_menu_file = self.main.load_file("Assets/menu_steam/main_menu.xml")
        self.main_menu = xmltodict.parse(self.main_menu_file.read())["page"]
        self.main_menu_file.close()
        assert(self.main_menu["@id"] == "main_menu")
        self.source = self.main_menu["@source"]
        for label in self.main_menu["label"]:
            self.parse_label(label)

    def parse_label(self, label):
        print label["@id"]

    def run(self, events):
        pass
