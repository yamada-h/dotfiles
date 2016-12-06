#!/usr/bin/env python
# coding: utf-8

import sys
import re

prefixs = []
nodes = []
skip = True
for line in sys.stdin:
  if line.startswith('Epoch Time'):
    skip = False
    print(line.rstrip())
    continue
  if skip:
    print(line.rstrip())
    continue
  m = re.match('^(.+)\[(.+)\]', line)
  prefixs.append(m.group(1))
  nodes.append(set(map(lambda s: s.strip(), m.group(2).split(','))))

for i in range(len(prefixs)):
  if i != len(prefixs) - 1:
    plus = nodes[i] - nodes[i+1]
    minus = nodes[i+1] - nodes[i]

    line = prefixs[i]
    for p in plus:
      line += ' +%s' % p
    for m in minus:
      line += ' -%s' % m
  else:
    line = prefixs[i]
    for node in nodes[i]:
      line += ' %s' % node

  print(line)
