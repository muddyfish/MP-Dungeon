import dungeon, random
class Layout(object):
    def __init__(self, roomtype):
        self.roomtype = roomtype

    def init(self):
        print self.roomtype

def recurse_classes(class_, start = True):
    if start: classmap = []
    else: classmap = [class_.__name__]
    for subclass in class_.__subclasses__():
        classmap.extend(recurse_classes(subclass, False))
    return classmap

def main():
    classnames = recurse_classes(dungeon.Room)
    print classnames

if __name__ == "__main__":
    main()
