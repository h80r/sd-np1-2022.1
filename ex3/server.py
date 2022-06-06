import socket
from _thread import start_new_thread

database = {}


def handle_client(conn, sock):
    while True:
        product_name = conn.recv(1024).decode("utf-8")
        if product_name == "terminar":
            conn.send(b"terminou")
            conn.close()
            sock.close()
            return

        conn.send(b"ok")
        product_amount = int(conn.recv(1024).decode("utf-8"))

        if product_name in database:
            current_amount = database[product_name]
            # Se o cliente quer remover mais do que tem
            if product_amount < current_amount * -1:
                conn.send(
                    bytes(
                        "não é possível fazer a saída de estoque – quantidade menor que o valor desejado",
                        "utf-8",
                    )
                )
            else:
                database[product_name] += product_amount
                conn.send(
                    bytes(
                        f"estoque atualizado e quantidade de {database[product_name]}",
                        "utf-8",
                    )
                )
        else:  # Produto não existe no banco de dados
            if product_amount < 0:  # Se for uma saída de estoque
                conn.send(
                    bytes(
                        "produto inexistente",
                        "utf-8",
                    )
                )
            else:  # Se for uma entrada de estoque
                database[product_name] = product_amount
                conn.send(
                    bytes(
                        "produto criado",
                        "utf-8",
                    )
                )


def main():
    ip, port = "127.0.0.1", 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    print(f"Servidor iniciado em {ip}:{port}")

    sock.listen()

    while True:
        try:
            conn, addr = sock.accept()
            print(f"Conexão recebida de {addr}")
            start_new_thread(handle_client, (conn, sock))
        except ConnectionAbortedError:
            print("Servidor encerrado")
            break


if __name__ == "__main__":
    main()
