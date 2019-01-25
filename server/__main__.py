import socket
import sys

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", int(sys.argv[1])))
    s.listen(1)

    conn, addr = s.accept()
    print(f"Connected to: {addr}")
    
    while True:
        data = conn.recv(20)
        if not data: break
        print(data)
        conn.send(b"Hello World")

if __name__ == "__main__":
    main()
