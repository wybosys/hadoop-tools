import os
import subprocess

HDP_HOME = os.getenv("HADOOP_HOME")
if HDP_HOME is None:
    HDP_HOME = '/opt/hadoop'

DOCKER_HDP_NAME = 'xaas-hadoop'


def Run(cmd: str, docker: bool = False) -> str:
    """运行命令"""
    if docker == True:
        cmd = "docker exec %s %s" % (DOCKER_HDP_NAME, cmd)
    (st, res) = subprocess.getstatusoutput(cmd)
    if st != 0:
        print("执行失败", res)
        return None
    return res
