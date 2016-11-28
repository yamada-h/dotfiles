#!/usr/bin/env python
# coding: utf-8

import os
from subprocess import call

def create_vdi(name):
  return call(['dog', 'vdi', 'create', name, '1G'])

def write_vdi_data(name):
  data = '/tmp/data.1G'
  if not os.path.exists(data):
    call('dd if=/dev/urandom of=%s bs=1M count=1024' % data, shell=True)
  return call('cat %s | dog vdi write %s' % (data, name), shell=True)

for i in range(500):
  name = '%04d' % i
  rc = create_vdi(name)
  if rc == 0:
    write_vdi_data(name)
