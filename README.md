# 🔐 Ransomware Simulation (Safe Demo Project)

> ⚠️ **Important:** This project is made only for learning purposes.
> Please don’t run this on any real system or without permission. It is meant to be used inside a safe environment like Docker or a VM.

---

## 📌 What this project is about

This project is a simple ransomware simulation that I built to understand how ransomware actually works behind the scenes.

Instead of just reading theory, I wanted to see:

* how files get encrypted
* how a ransom note is generated
* and how recovery works using a key

Everything runs inside a controlled Docker setup, so nothing affects the real system.

---

## 🎯 Why I made this

I created this as part of my cybersecurity learning to get a more practical understanding of attacks.

While studying ransomware, I realized most examples are either too theoretical or too dangerous to try. So I made a **safe demo version** where I could test things myself without risking anything.

---

## 🛠️ Tech used

* Python 3
* AES encryption (using cryptography libraries)
* Docker & Docker Compose
* Linux-based container (victim environment)

---

## 🏗️ Project structure

```bash
ransomware-simulation/
│
├── victim/
│   ├── Dockerfile
│   ├── encrypt.py
│   ├── decrypt.py
│   └── sample_files/
│
├── docker-compose.yml
├── requirements.txt
├── DISCLAIMER.md
└── README.md
```

---

## ⚙️ How to run it

### 1. Clone the repo

```bash
git clone https://github.com/heetgohil28-dev/ransomware-simulation.git
cd ransomware-simulation
```

### 2. Start the containers

```bash
docker-compose up --build
```

This will start the victim container and run the encryption on sample files.

---

## 🔓 How to decrypt files

```bash
docker exec -it victim python decrypt.py
```

This will restore the encrypted files using the stored key.

---

## 🔬 What actually happens

* The script scans a folder (`sample_files`)
* Each file gets encrypted using AES
* A ransom note file is created in the same directory
* Decryption script uses the key to restore files

So basically it follows the same flow:
**Encrypt → Show message → Recover**

---

## 🧠 What I learned

* How AES encryption works in real use
* File handling in Python
* How ransomware targets directories
* Using Docker for safe malware testing
* Importance of backups and isolation

---

## ⚡ Challenges I faced

* Docker container path issues (this took time to fix)
* File permission errors inside container
* Making sure encryption doesn’t break file recovery
* Debugging small mistakes in file loops

---

## 🚨 Safety note

* Only run this in Docker or a virtual machine
* Don’t test on personal files
* Don’t modify it for real-world use

This is just a learning project.

---

## 🚀 Possible improvements

If I continue working on this, I might add:

* A simple GUI for ransom screen
* Timer-based simulation
* Logging system
* Better key handling

---

## 👨‍💻 Author

Heet Gohil
B.Tech Cyber Security

GitHub: https://github.com/heetgohil28-dev
LinkedIn: https://linkedin.com/in/heetgohil

---
