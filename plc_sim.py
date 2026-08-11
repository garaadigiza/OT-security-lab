#!/usr/bin/env python3
# Simulated PLC - Modbus TCP server on port 502
from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock

# The PLC's memory:
#   coils (co)            = ON/OFF outputs, e.g. a Pump
#   holding registers (hr)= numeric values, e.g. a Tank Level
store = ModbusSlaveContext(
    co=ModbusSequentialDataBlock(0, [0] * 100),    # coil 0 = Pump (starts OFF)
    hr=ModbusSequentialDataBlock(0, [50] * 100),   # register 0 = Tank Level (starts 50)
)
context = ModbusServerContext(slaves=store, single=True)

print("=" * 50)
print(" Simulated PLC running - Modbus TCP on port 502")
print(" Coil 0    = Pump (0=OFF, 1=ON)")
print(" Register 0 = Tank Level")
print(" Press Ctrl+C to stop")
print("=" * 50)

StartTcpServer(context, address=("0.0.0.0", 502))
