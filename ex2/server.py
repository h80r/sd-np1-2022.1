import socket, time
from quadrilatero import Quadrilatero
from _thread import start_new_thread


def handle_client(conn):
    obj = Quadrilatero.from_json(conn.recv(1024).decode("utf-8"))
    obj.indica_tipo_quadrilatero()
    time.sleep(2)  # Simula um processamento mais demorado
    conn.send(bytes(obj.to_json(), "utf-8"))
    conn.close()


def main():
    ip, port = "127.0.0.1", 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    print(f"Servidor iniciado em {ip}:{port}")

    sock.listen()
    while True:
        conn, addr = sock.accept()
        print(f"Conexão recebida de {addr}")
        start_new_thread(handle_client, (conn,))
    sock.close()


if __name__ == "__main__":
    main()
