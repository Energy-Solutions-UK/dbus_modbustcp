#!/bin/bash -e

mkdir -p build/dbus-modbustcp
cd build/dbus-modbustcp
/opt/venus/current/sysroots/x86_64-ve-linux/usr/bin/qmake CXX=$CXX ../../dbus_modbustcp.pro && /opt/venus/current/sysroots/x86_64-ve-linux/usr/bin/make
