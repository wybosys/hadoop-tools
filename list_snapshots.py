#!/usr/bin/env python3

import argparse
from typing import *
import sys
import re
from config import *


def all(dir: str, docker: bool) -> List[str]:
    cmd = "%s/bin/hdfs dfs -ls %s/.snapshot" % (HDP_HOME, dir)
    res = Run(cmd, docker)
    names = []
    if res != None:
        pat = re.compile("%s/.snapshot/(.+)" % dir)
        for each in res.split("\n"):
            fnd = pat.findall(each)
            if fnd:
                names.append(fnd[0])
    return names


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="列出指定目录下的snapshot")
    parser.add_argument(dest='target')
    parser.add_argument('-d', dest='docker',
                        action='store_true', help='docker模式')
    args = parser.parse_args()
    res = all(args.target, args.docker)
    print(res)
