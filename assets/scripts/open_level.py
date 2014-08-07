LEVEL_VERSION = 0.1

class Level(object):
    def __init__(self, main, levelname):
        self.main = main
        self.screen = self.main.screen
        self.levelname = levelname
        self.level_file = open(self.levelname)
        self.level = xmltodict.parse(self.level_file.read())
        self.parse_level()
        self.level_file.close()

    def run(self, events):
        self.screen.fill((127,0,0))

    def parse_level(self):
        assert(self.level["level"]["@version"] == str(LEVEL_VERSION))
        self.properties = self.level["level"]["properties"]["property"]
        for property in self.properties:
            if property["@key"] == "backgroundMaterial":
                self.background = property["@value"]
            if property["@key"] == "levelTime":
                self.level_time = int(property["@value"])
        self.instances = self.level["level"]["instances"]["instance"]
        for instance in self.instances:
            self.parse_instance(instance)
        print self.background, self.level_time

    def parse_instance(self, instance):
        data = {}
        data["id"] = int(instance["@iid"])
        data["name"] = instance["@name"]
        if "@group" in instance: data["group"] = instance["@group"]
        if "graphref" in instance:
            data["graph"] = self.parse_graph(instance["graphref"])
        
    def parse_graph(self, graphpath):
        graphfile = open("Assets/objects/"+graphpath["@set"]+"/"+graphpath["@filename"]+".nmg")
        graphdata = xmltodict.parse(graphfile.read())["graph"]
        graph = {"points": range(len(graphdata["points"]["point"])), \
                 "edges": []}
        for point in graphdata["points"]["point"]:
            xyz = {}
            for i in point["position"]:
                xyz[str(i[1:])] = float(point["position"][i])
            graph["points"][int(point["@id"])] = xyz
        for edge in graphdata["edges"]["edge"]:
            graph["edges"].append([edge["@start"], edge["@end"]])
        graphfile.close()
        print graph
        return graph

if __name__ == "__main__":
    import pygame, os
    print os.getcwd()
    import main
    main = main.Main()
    main.screen_controller = LevelLoader(main, "Assets/levels/classic/2/level02_1.nml")
    main.run()
