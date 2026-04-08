import socket
from concurrent.futures import ThreadPoolExecutor

def start_scan(target, start_port, end_port):

    open_ports = []

    def scan_port(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)

            result = s.connect_ex((target, port))

            if result == 0:
                open_ports.append(port)

            s.close()
        except:
            pass

    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_port, range(start_port, end_port + 1))

    return open_ports


if __name__ == "__main__":
    print("=== Fast Port Scanner ===")
    target = input("Enter target IP or domain: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    result = start_scan(target, start_port, end_port)

    print("\nScan Complete!")
    print("Open Ports:", result)
