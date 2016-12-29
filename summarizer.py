#!/usr/bin/env python
"""Summarizes smaps
"""
import collections
import sys

class SmapsParser(object):
    
    SECTION_HEIGHT=16

    def __init__(self):
        self.path = None
        self.size_map = collections.defaultdict(
            lambda:collections.defaultdict(lambda:0))

    def parse(self, f):
        for i, line in enumerate(f):
            if i % self.SECTION_HEIGHT == 0:
                self.handle_header(line)
            elif 1 <= i % self.SECTION_HEIGHT < 15:
                self.handle_proportion(line)
        self.handle_done()

    def handle_header(self, line):
        fields = line.strip().split()
        path = None
        if len(fields) == 5:
            address, permissions, offset, device, inode = fields
        else:  # len(fields) == 6
            address, permissions, offset, device, inode, path = fields
        if path:
            self.path = path

    def handle_proportion(self, line):
        category, size, unit = line.strip().split()
        category = category[:-1]
        size = int(size)
        assert unit == "kB"
        self.size_map[self.path][category] += size

    def handle_done(self):
        entries = self.size_map.items()
        entries.sort()
        for entry, sizes in entries:
            print entry
            sizes = sizes.items()
            sizes.sort()
            for category, size in sizes:
                print category, size


def main(argv=None):
    if argv is None:
        argv = sys.argv
    parser = SmapsParser()
    parser.parse(sys.stdin)


if __name__ == "__main__":
    sys.exit(main())
