import socket
from _thread import start_new_thread


def handle_client(conn):
    nums = []
    for i in range(3):
        res = conn.recv(1024).decode("utf-8")
        if int(res) < 0:
            conn.send(bytes("Conexão fechada", "utf-8"))
            break
        conn.send(bytes("Número recebido...", "utf-8"))
        nums.append(int(res))

    if len(nums) == 3:
        conn.send(
            bytes(f"\nMenor número: {min(nums)}\nMaior número: {max(nums)}", "utf-8")
        )
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
