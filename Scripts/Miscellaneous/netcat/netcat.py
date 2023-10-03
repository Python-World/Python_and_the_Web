import argparse
import os
import socket
import subprocess
import sys
import threading


# to run a command
def run(cmd):
    if cmd[:2] == "cd":
        os.chdir(cmd[3:])
        return
    return subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    ).stdout.read()


# recv from remotely connected machine
def recvfrom(client):
    req = ""
    while True:
        req += client.recv(1024).decode("utf-8")
        if len(req) < 1024:
            break
    return req


# handle client thread
def client_handler(client):
    while True:
        req = recvfrom(client)
        if req == "uploading":
            client.send(b"ack")
            filename = recvfrom(client)
            print("file: ", filename)
            client.send(b"ack")
            with open(filename, "w") as fh:
                data = recvfrom(client)
                fh.write(data)
                sys.exit()
        if req == "end":
            print("session ends")
            break
        res = run(req)
        if not res:
            res = b"command executed successfully"
        client.send(res)


# get a remote shell
def getShell(host, port, _shell, cmd):
    flag = bool(cmd)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    while True:
        if not flag:
            cmd = input("# ")
        client.send(bytes(cmd, "utf-8"))
        if cmd == "end":
            print("session ends")
            break
        res = ""
        while True:
            res += client.recv(1024).decode("utf-8")
            if len(res) < 1024:
                break
        print(res)
        if flag:
            client.close()
            sys.exit()


# start a server
def server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    while True:
        sck, addr = server.accept()
        print("session started: ", addr[0], addr[1])
        client = threading.Thread(target=client_handler, args=(sck,))
        client.start()


# upload a file
def uploadFile(host, port, path, filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send(b"uploading")
    recvfrom(client)
    client.send(bytes(filename, "utf-8"))
    recvfrom(client)
    with open(path, "r") as fh:
        client.send(bytes(fh.read(), "utf-8"))
    client.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--listen", type=bool, default=False, help="start a server"
    )
    parser.add_argument(
        "-H",
        "--host",
        type=str,
        default="127.0.0.1",
        help="specify the host ip",
    )
    parser.add_argument(
        "-p", "--port", type=int, default=1234, help="specify the port"
    )
    parser.add_argument(
        "-s",
        "--shell",
        type=bool,
        default=False,
        help="get an interactive shell",
    )
    parser.add_argument(
        "-e",
        "--execute",
        type=str,
        default=None,
        help="execute a single command",
    )
    parser.add_argument(
        "-u",
        "--upload",
        type=bool,
        default=False,
        help="upload file to remote server",
    )
    options = parser.parse_args()
    host = options.host
    port = options.port
    listen = options.listen
    shell = options.shell
    execute = options.execute
    upload = options.upload

    if listen:
        server(host, port)
    elif shell:
        getShell(host, port, True, False)
    elif execute:
        getShell(host, port, False, execute)
    elif upload:
        path = input(
            "Enter absolute path of file to be uploaded on remote server: "
        )
        filename = input(
            "Enter new file name if you want to rename uploaded file on server: "
        )
        uploadFile(host, port, path, filename)


if __name__ == "__main__":
    main()
