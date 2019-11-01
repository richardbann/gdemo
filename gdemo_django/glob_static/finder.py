import os
import glob

from django.contrib.staticfiles import finders
from django.utils._os import safe_join


class GlobFileSystemFinder(finders.FileSystemFinder):
    def find_location(self, root, path, prefix=None):
        if prefix:
            prefix = '%s%s' % (prefix, os.sep)
            if not path.startswith(prefix):
                return None
            path = path[len(prefix):]
        path = safe_join(root, path)
        matching = glob.glob(path)
        if matching:
            return matching[0]
