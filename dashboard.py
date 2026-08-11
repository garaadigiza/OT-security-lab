import tkinter as tk
from pymodbus.client.sync import ModbusTcpClient

PLC_IP = "127.0.0.1"
client = ModbusTcpClient(PLC_IP, port=502)
client.connect()

window = tk.Tk()
window.title("PLC Operator Dashboard")
window.geometry("400x300")
canvas = tk.Canvas(window, width=400, height=300, bg="black")
canvas.pack()

def update():
    pump = client.read_coils(0, 1).bits[0]
    level = client.read_holding_registers(0, 1).registers[0]

    canvas.delete("all")

    color = "green" if pump else "red"
    canvas.create_oval(50, 50, 120, 120, fill=color)
    canvas.create_text(85, 140, text="PUMP", fill="white")

    canvas.create_rectangle(200, 50, 280, 250, outline="white")
    fill_height = 250 - (level * 2)
    canvas.create_rectangle(200, fill_height, 280, 250, fill="cyan")
    canvas.create_text(240, 270, text=f"Level: {level}", fill="white")

    window.after(1000, update)

update()
window.mainloop()
