#!/usr/bin/env python
# coding: utf-8

from subprocess import call
from uuid import uuid4

for i in range(10000):
  print(i)
  name = uuid4()
  call('dog vdi create %s 1G' % name, shell=True)
  call('dog vdi delete %s' % name, shell=True)
