#!/bin/bash -e

. /opt/venus/current/environment-setup-cortexa8hf-neon-ve-linux-gnueabi

mkdir -p build/dbus-modbustcp
cd build/dbus-modbustcp
qmake CXX=$CXX ../../dbus_modbustcp.pro && make
