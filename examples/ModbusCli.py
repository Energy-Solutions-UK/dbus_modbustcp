#!/usr/bin/python
import argparse
import struct
from pymodbus.client import ModbusTcpClient

parser = argparse.ArgumentParser(description='Send modbus TCP commands.')
parser.add_argument('--dest', '-d', nargs=1, help='modbus server')
parser.add_argument('--port', '-p', nargs='?', help='tcp port', default=502)
parser.add_argument('--slave', '-s', type=int, nargs='?', help='slave address', default=1)
parser.add_argument('--register', '-r', type=int, nargs=1, help='register')
parser.add_argument('--count', '-c', type=int, nargs='?', help='count', default=1)
parser.add_argument('--type', '-t', nargs='?', help='data type (python struct syntax)', default=None)
parser.add_argument('--write', '-w', nargs='?', help='write string to multiple registers', default=None)
args = parser.parse_args()

client = ModbusTcpClient(host=args.dest[0], port=args.port)
if args.write == None:
    result = client.read_holding_registers(address=args.register[0], count=args.count, unit=args.slave)
    if result.function_code >= 0x80:
        print('Error in function_code: {} {}'.format(hex(result.function_code), hex(result.exception_code)))
    elif args.type == None:
        print(result.registers)
    else:
        bytes = b''
        for r in result.registers:
            bytes += chr(r >> 8)
            bytes += chr(r & 255)
        print(struct.unpack(args.type, bytes))
else:
    # Convert the string to a list of ASCII values
    values = [ord(c) for c in args.write]
    if len(values) % 2 == 1:
        values.append(0)
    values = [values[i] << 8 | values[i+1] for i in range(0, len(values), 2)]
    print("writing: {}".format(values))
    result = client.write_registers(address=args.register[0], values=values, unit=args.slave)
    if result.function_code >= 0x80:
        print('Error in function_code: {} {}'.format(hex(result.function_code), hex(result.exception_code)))