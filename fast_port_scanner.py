import socket
from concurrent.futures import ThreadPoolExecutor

def get_service(port):
    common = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL"
    }
    return common.get(port, "Unknown")

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            service = get_service(port)

            try:
                banner = s.recv(1024).decode().strip()
            except:
                banner = "Unknown"

            print(f"[OPEN] Port {port} → {service} | {banner}")

        s.close()
    except:
        pass

def start_scan(target, start_port, end_port):
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda p: scan_port(target, p), range(start_port, end_port + 1))


if __name__ == "__main__":
    print("=== Advanced Port Scanner ===")

    target = input("Enter target IP or domain: ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

    start_scan(target, start_port, end_port)
