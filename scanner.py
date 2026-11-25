import socket
from concurrent.futures import ThreadPoolExecutor
COMMON = {21: "FTP", 22: "SSH", 80: "HTTP", 135: "RPC", 443: "HTTPS", 445: "SMB"}

def scan_port(host, port, timeout=0.5):
    with socket.socket() as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0

def self_check():
    srv = socket.socket()
    srv.bind(("127.0.0.1", 0))  # 0 = let the OS pick a free port
    srv.listen()
    port = srv.getsockname()[1]
    assert scan_port("127.0.0.1", port)
    srv.close()
    assert not scan_port("127.0.0.1", port)
    print("self-check passed")

if __name__ == "__main__":
    host = input("Host (your own machine: 127.0.0.1): ")
    try:
        start = int (input("Start port: "))
        end = int (input("End port: "))
    except ValueError:
        raise SystemExit("Ports must be numbers.")
    ports = range(start, end + 1)
    with ThreadPoolExecutor(100) as pool:  # 100 ports checked at once
        for port, is_open in zip(ports, pool.map(lambda p: scan_port(host, p), ports)):
            if is_open:
                print("OPEN:", port, COMMON.get(port, ""))
   
    print("Done")