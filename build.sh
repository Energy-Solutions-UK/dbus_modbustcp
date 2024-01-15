#!/bin/bash -e

mkdir -p build/dbus-modbustcp
cd build/dbus-modbustcp
export QMAKESPEC=/opt/venus/current/sysroots/x86_64-ve-linux/usr/mkspecs/linux-g++
/opt/venus/current/sysroots/x86_64-ve-linux/usr/bin/qmake CXX=$CXX ../../dbus_modbustcp.pro && make
