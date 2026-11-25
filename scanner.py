import socket

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
    # shortcut: one port at a time, slow on big ranges; use threads if you need speed
    for port in range(start, end + 1):
        if scan_port(host, port):
            print("OPEN:", port)
    print("Done")