#!/usr/bin/env python3

import argparse
import list_snapshots
import rm_snapshots
from config import *


def make(dir: str, docker: bool) -> bool:
    cmd = "%s/bin/hdfs dfs -createSnapshot %s" % (HDP_HOME, dir)
    res = Run(cmd, docker)
    return res != None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="生成制定目录下的snapshot")
    parser.add_argument(dest='target')
    parser.add_argument('-d', dest='docker',
                        action='store_true', help='docker模式')
    parser.add_argument('-c', dest='count', action='store',
                        help='最多有几个历史版本', default=-1, type=int)
    args = parser.parse_args()

    if args.count > 0:
        res = list_snapshots.all(args.target, args.docker)
        while len(res) > args.count:
            print("移除 %s" % res[0])
            rm_snapshots.delete(args.target, res[0], args.docker)
            res = res[1:]

    print("生成新的")
    make(args.target, args.docker)
