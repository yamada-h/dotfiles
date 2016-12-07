#!/usr/bin/env python
# coding: utf-8

from subprocess import call
from uuid import uuid4

for i in range(10):
  #cmd = 'sheep --cluster zookeeper:127.0.0.1:2181 --zone %d --log level=debug --port 700%d /sheepdog/%d' % (i, i, i)
  cmd = 'sheep --cluster zookeeper:172.31.24.110:2181,172.31.24.112:2181,172.31.24.111:2181 --zone %d --log level=debug --port 700%d /sheepdog/%d' % (i, i, i)
  print(cmd)
  call(cmd, shell=True)
