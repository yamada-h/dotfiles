#!/bin/bash
set -x

sudo rm /usr/lib/x86_64-linux-gnu/libzookeeper_mt.so.2
sudo ln -s /usr/lib/x86_64-linux-gnu/libzookeeper_mt.so.2.0.0.a /usr/lib/x86_64-linux-gnu/libzookeeper_mt.so.2

sudo rm /usr/lib/x86_64-linux-gnu/libzookeeper_mt.so
sudo ln -s /usr/lib/x86_64-linux-gnu/libzookeeper_mt.so.2.0.0.a /usr/lib/x86_64-linux-gnu/libzookeeper_mt.so
