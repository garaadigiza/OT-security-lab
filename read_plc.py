rom pymodbus.client.sync import ModbusTcpClient

c = ModbusTcpClient('127.0.0.1', port=502)
c.connect()

pump = c.read_coils(0, 1)          # read coil 0 (Pump)
level = c.read_holding_registers(0, 1)  # read register 0 (Tank Level)

print(f"Pump state:  {pump.bits[0]}")
print(f"Tank Level:  {level.registers[0]}")
c.close()
