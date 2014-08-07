import glob, os
__all__ = [i[:-3].split(os.sep)[-1] for i in glob.glob("assets%sscripts%s*.py" %(os.sep, os.sep))]
