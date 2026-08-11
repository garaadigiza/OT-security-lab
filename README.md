# OT / ICS Security Lab — Modbus Attack, Detection & Incident Response

A hands-on operational technology (OT) / industrial control system (ICS) security lab built in a virtualized environment. This project simulates an industrial control device, executes a realistic attack against it, detects the attack through network traffic analysis, and documents the full incident-response lifecycle.

> **Purpose:** Demonstrate practical OT security skills — industrial protocol analysis, attack detection, and incident response using the PICERL framework — in an isolated, reproducible lab.

---

## Overview

The lab recreates a miniature industrial environment:

| Component | Role | Technology |
|---|---|---|
| **PLC** | The control device (a pump + tank) | Python Modbus TCP server, port 502 |
| **HMI Dashboard** | Live operator view | Python (tkinter), polls the PLC each second |
| **Attacker** | Threat actor | Python Modbus client (command injection) |
| **Monitoring** | Detection | Wireshark packet capture |

**Platform:** VirtualBox — Kali Linux (PLC + attacker + monitoring) and Windows 10, on an isolated host-only network.

---

## What This Project Demonstrates

- **Industrial protocol knowledge** — Modbus TCP (function codes, coils, registers) on port 502.
- **The core OT security flaw** — Modbus has no authentication or encryption, so any host that can reach the PLC can both read and *change* physical process state.
- **Attack execution** — a false-command-injection ("manipulation of control") attack that forces a control output with no authorization.
- **Detection & analysis** — distinguishing normal read traffic (function codes 1, 3) from anomalous write commands (function code 5); extracting indicators of compromise (IOCs).
- **Incident response** — containment via firewall rules, followed by a full **PICERL** write-up (see `incident-report.pdf`).
- **Defensive controls** — segmentation, allow-listing, and continuous monitoring for legacy OT protocols.

---

## Repository Contents

```
├── README.md              This file
├── incident-report.pdf    Full PICERL incident report
├── scripts/
│   ├── plc_sim.py         Simulated PLC (Modbus TCP server)
│   ├── read_plc.py        Reads PLC state (normal operator activity)
│   ├── attack.py          False-command-injection attack
│   └── dashboard.py       Live visual HMI dashboard
└── screenshots/           Dashboard, Wireshark capture, blocked attack
```

---

## The Attack, Step by Step

1. **Baseline** — the HMI dashboard polls the PLC every second using read commands (Modbus function codes 1 and 3). This is the normal traffic pattern.
2. **Attack** — `attack.py` sends a **Write Single Coil** command (function code 5) that forces the pump ON, with no authentication.
3. **Detection** — Wireshark captures the anomalous write among the normal reads. The IOC is extracted: function code 5, target coil 0 (pump), value `FF 00` (ON), with a timestamp.
4. **Containment** — a firewall rule blocks the attacker from reaching the PLC on port 502; the attack is re-run and fails.
5. **Response & lessons** — documented end-to-end in `incident-report.pdf` using PICERL, concluding with segmentation, allow-listing, and monitoring as preventive controls.

---

## Key Takeaway

Legacy OT protocols such as Modbus cannot secure themselves — they have no built-in authentication or encryption. Security must therefore be enforced by the surrounding architecture: **network segmentation, allow-listing, and continuous monitoring.** This lab demonstrates that principle from attack through to defense.

---

## Mapping to CompTIA SecOT+ Domains

| Activity | Domain |
|---|---|
| PLC, Modbus, coils/registers, safety-first model | 1.0 OT Systems & Safety |
| Security-vs-availability trade-off in containment | 2.0 OT Risk Management |
| IOC extraction, anomaly vs. baseline | 3.0 / 5.0 Threat Intel & Security Ops |
| Segmentation, allow-listing, zones & conduits | 4.0 OT Architecture & Design |
| Detection via traffic analysis | 5.0 OT Security Operations |
| PICERL response, process validation | 6.0 OT Incident Management |

---

## Disclaimer

All components in this lab are **simulated and fully isolated** on a host-only network. No production system, real industrial device, or external network was involved. These techniques are demonstrated for educational purposes on systems the author owns.
