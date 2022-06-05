from quadrilatero import Quadrilatero
import socket


def main():
    print("Insira o IP e a porta do servidor:")
    ip, port = input(), int(input())

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, int(port)))

    print("Iremos gerar o objeto.")
    obj = Quadrilatero()
    obj.le_dados()

    print("Iremos pedir ao servidor para processar o tipo de objeto.")
    sock.send(bytes(obj.to_json(), "utf-8"))
    obj = Quadrilatero.from_json(sock.recv(1024).decode("utf-8"))

    print("Iremos mostrar os dados do objeto.")
    obj.mostra_dados()

    sock.close()


if __name__ == "__main__":
    main()
