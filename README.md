# 🔐 Ransomware Simulation — Educational Cybersecurity Project

> ⚠️ **DISCLAIMER:** This project is strictly for **educational and authorized testing purposes only**.  
> Do NOT run this on any system without explicit permission. Unauthorized use is illegal.

---

## 📌 Overview

A controlled ransomware simulation built with **Python** and **Docker**, designed to demonstrate how ransomware operates — including file encryption, ransom note delivery, and recovery — in a safe, isolated environment.

Built as part of a **Cyber Security** undergraduate curriculum to understand attacker techniques and strengthen defensive skills.

---

## 🎯 Objectives

- Simulate the encryption behavior of real-world ransomware
- Demonstrate AES-based file encryption and decryption
- Understand attacker TTPs (Tactics, Techniques & Procedures)
- Practice incident response and recovery in a controlled lab
- Safely test endpoint detection without causing actual damage

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Simulation Logic | Python 3 |
| Encryption | AES (via `cryptography` / `pycryptodome`) |
| Containerization | Docker + Docker Compose |
| Target Environment | Isolated victim container |

---

## 🏗️ Architecture
```bash
ransomware-simulation/
│
├── victim/                  # Isolated victim environment
│   ├── Dockerfile           # Victim container setup
│   ├── encrypt.py           # Encryption simulation script
│   ├── decrypt.py           # Decryption / recovery script
│   └── sample_files/        # Dummy files for encryption demo
│
├── docker-compose.yml       # Orchestrates attacker-victim setup
├── requirements.txt         # Python dependencies
├── DISCLAIMER.md            # Legal & ethical notice
└── README.md
```

---

## ⚙️ Setup & Usage

### Prerequisites
- Docker & Docker Compose installed
- Python 3.8+

### Run the Simulation

```bash
# Clone the repository
git clone https://github.com/heetgohil28-dev/ransomware-simulation.git
cd ransomware-simulation

# Build and start the containers
docker-compose up --build

# The victim container will simulate encryption of files in /victim/sample_files
```

### Decrypt / Recover Files

```bash
# Run decryption inside the victim container
docker exec -it victim python decrypt.py
```

---

## 🔬 How It Works

1. **Encryption Phase** — The simulation script scans a target directory and encrypts each file using AES symmetric encryption. A key is generated and stored (simulating C2 key storage).
2. **Ransom Note** — A `README_IMPORTANT.txt` is dropped in the target directory simulating real ransomware behavior.
3. **Decryption Phase** — Using the stored key, files are restored — demonstrating that controlled recovery is possible in a simulation environment.

---

## 🧠 Key Concepts Demonstrated

- AES symmetric encryption (CBC/GCM mode)
- File I/O manipulation in Python
- Docker container isolation for malware sandboxing
- Ransomware attack lifecycle (Encryption → Demand → Recovery)
- Incident response workflow

---

## 🚨 Ethical & Legal Notice

This tool was created **solely for educational purposes** as part of academic coursework in Cyber Security.

- ✅ Run only in isolated, controlled environments (Docker containers, VMs)
- ✅ Only use on systems you own or have written permission to test
- ❌ Never deploy against real infrastructure
- ❌ Never use for unauthorized access or extortion

The author assumes **no liability** for misuse of this tool.

---

## 📚 References & Further Reading

- [MITRE ATT&CK — Ransomware TTPs](https://attack.mitre.org/techniques/T1486/)
- [NIST Ransomware Guidance](https://www.nist.gov/ransomware)
- [Python Cryptography Library](https://cryptography.io/en/latest/)

---

## 👨‍💻 Author

**Heet Gohil**  
B.Tech. Cyber Security — Shah & Anchor Kutchhi Engineering College  
[LinkedIn](https://linkedin.com/in/heetgohil) | [GitHub](https://github.com/heetgohil28-dev)

