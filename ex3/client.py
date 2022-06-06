import socket


def main():
    ip, port = "127.0.0.1", 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, int(port)))

    while True:
        try:
            product_name = input("Insira o nome do produto: ")
            sock.send(bytes(product_name, "utf-8"))
            if sock.recv(1024).decode("utf-8") == "terminou":
                break
            product_amount = int(input("Insira a quantidade do produto: "))
            sock.send(bytes(str(product_amount), "utf-8"))
            res = sock.recv(1024).decode("utf-8")
            print(res)
        except BrokenPipeError:
            print("Conexão perdida")
            break

    sock.close()


if __name__ == "__main__":
    main()
