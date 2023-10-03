import argparse
import sys
from socket import *
from threading import Semaphore, Thread

lock = Semaphore(value=1)


def connScan(host, port):
    try:
        skt = socket(AF_INET, SOCK_STREAM)
        skt.connect((host, port))
        skt.send(("hello\r\n").encode("utf-8"))
        skt.recv(100)
        lock.acquire()
        print(f"[+] {port} is open")
    except timeout:
        lock.acquire()
        print(f"[-] {port} is closed")
    finally:
        lock.release()
        skt.close()


def portScan(host, ports):
    try:
        ip = gethostbyname(host)
    except gaierror:
        print(f"Cannot resolve {host} unknown")
        sys.exit()
    try:
        name = gethostbyaddr(ip)
        print(f"Scan results for {name[0]}")
    except gaierror:
        print(f"Scan results for {ip}: ")
        sys.exit()
    setdefaulttimeout(1)
    for port in ports:
        t = Thread(target=connScan, args=(host, int(port)))
        t.start()


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-H", "--host", type=str, help="host name", default="127.0.0.1"
    )
    parser.add_argument(
        "-p", "--port", type=str, help="port number[s]", default="80"
    )
    args = parser.parse_args()
    host = args.host
    ports = args.port.split(",")
    portScan(host, ports)


if __name__ == "__main__":
    Main()
