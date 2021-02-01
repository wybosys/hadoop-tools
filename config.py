import os
import sys

HDP_HOME = os.getenv("HADOOP_HOME")
if HDP_HOME is None:
    HDP_HOME = '/opt/hadoop'
