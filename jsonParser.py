#!/usr/bin/env python
# simple python json parser
# by riesal@gmail.com

import sys
import re
import json
from pprint import pprint

def nilaiNya(d, patterns):
    try:
        pattern = patterns.pop(0)
    except IndexError:
        print(d)
    else:
        if isinstance(d, dict):
            keys = filter(pattern.match, d.keys())
        elif isinstance(d, list):
            keys = map(int,
                       filter(pattern.match,
                              ['%d' % i for i in range(len(d))]))
        else:
            if pattern.match(str(d)):
                pprint(d)
            return
        for item in (d[key] for key in keys):
            nilaiNya(item, patterns[:])

if __name__ == '__main__':
    try:
        j = json.loads(sys.stdin.read())
    except ValueError, e:
        print >>sys.stderr, 'Tidak dapat memanggil objek JSON dari stdin.'
        sys.exit(1)

    nilaiNya(j, map(re.compile, sys.argv[1:]))
