import socket


def main():
    print("Insira o IP e a porta do servidor:")
    ip, port = input(), int(input())

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, int(port)))

    for i in range(3):
        print(f"Insira o {i+1}º número:")
        sock.send(bytes(input(), "utf-8"))

        res = sock.recv(1024).decode("utf-8")
        print(res)
        if res == "Conexão fechada":
            break

    sock.close()


if __name__ == "__main__":
    main()
