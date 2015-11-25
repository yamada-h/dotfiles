#! /usr/bin/env python
import sys
import subprocess
import logging
logging.basicConfig(filename='fio_test.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
from datetime import datetime

def call(cmd):
  output = subprocess.check_output(cmd.split(' '))
  logging.debug(output)
  return output

def ssh(cmd):
  SSH = 'ssh root@10.0.254.249 '
  return call(SSH + cmd)

ssh('umount /sheep')
call('sudo virsh detach-device vm00 device.xml')

for i in range(3000):
  print '%s: LOOP %d' % (datetime.now(), i)
  sys.stdout.flush()
  call('dog cluster format -f -c 1')
  call('dog vdi create vol00 4G')
  call('sudo virsh attach-device vm00 device.xml')

  ssh('mkfs.xfs -f /dev/vdb')
  ssh('mount -t xfs /dev/vdb /sheep')
  ssh('fio -name=QEMU-Reproduce -rw=read -numjobs=32 -group_reporting -size=37M -ioengine=sync -directory=/sheep') 
  ssh('umount /sheep')

  call('sudo virsh detach-device vm00 device.xml')
