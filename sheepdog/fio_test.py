#! /usr/bin/env python
import sys
import subprocess
import logging
logging.basicConfig(filename='fio_test.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
from datetime import datetime
import os

def yes(cmd):
  p = subprocess.Popen(cmd.split(' '), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  stdout, stderr = p.communicate('yes\n')
  logging.debug(stdout)
  return stdout

def call(cmd):
  output = subprocess.check_output(cmd.split(' '))
  logging.debug(output)
  return output

def ssh(cmd):
  SSH = 'ssh root@10.0.254.59 '
  if os.environ['QEMU_TEST_SSH_HOST']:
    SSH = 'ssh root@%s' % os.environ['QEMU_TEST_SSH_HOST']
  return call(SSH + cmd)

try:
  ssh('umount /sheep')
  call('sudo virsh detach-device vm00 device.xml')
except subprocess.CalledProcessError as e:
  print e

for i in range(3000):
  print '%s: LOOP %d' % (datetime.now(), i)
  sys.stdout.flush()
  yes('dog cluster format -c 1')
  call('dog vdi create vol00 4G')
  call('sudo virsh attach-device vm00 device.xml')

  ssh('mkfs.xfs -f /dev/vdb')
  ssh('mount -t xfs /dev/vdb /sheep')
  ssh('fio -name=QEMU-Reproduce -rw=read -numjobs=31 -group_reporting -size=128M -ioengine=sync -directory=/sheep') 
  ssh('umount /sheep')

  call('sudo virsh detach-device vm00 device.xml')
