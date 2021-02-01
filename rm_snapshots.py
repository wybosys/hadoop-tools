#!/usr/bin/env python3

from config import *
import list_snapshots
import argparse


def delete(dir: str, ss: str, docker: bool) -> bool:
    cmd = "%s/bin/hdfs dfs -deleteSnaphost %s/.snapshot %s" % (
        HDP_HOME, dir, ss)
    res = Run(cmd, docker)
    return res != None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="删除指定目录下的snapshot")
    parser.add_argument(dest='target')
    parser.add_argument('-d', dest='docker',
                        action='store_true', help='docker模式')
    args = parser.parse_args()
    res = list_snapshots.all(args.target, args.docker)
    for each in res:
        inp = input("确认删除 %s [N/Y]? " % each)
        if inp == 'Y':
            delete(args.target, each, args.docker)
