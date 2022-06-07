from ftplib import FTP
import os


def main():
    current_directory = os.getcwd()

    ftp = FTP("")
    ftp.connect("localhost", 8010)
    ftp.login()

    while True:
        opt = menu()
        if opt == 1:
            current_directory = changeClientDirectory(current_directory)
        elif opt == 2:
            changeServerDirectory(ftp)
        elif opt == 3:
            uploadFile(ftp, current_directory)
        elif opt == 4:
            downloadFile(ftp, current_directory)
        elif opt == 5:
            executeCommand(ftp)
        elif opt == 0:
            ftp.quit()
            break


def menu():
    print("1 - Mudar diretório local")
    print("2 - Mudar diretório remoto")
    print("3 - Enviar arquivo")
    print("4 - Receber arquivo")
    print("5 - Executar comando")
    print("0 - Sair")
    return int(input("Insira a opção desejada: "))


def changeClientDirectory(current_directory):
    print("Diretório atual: " + current_directory)
    print("Diretório disponível: ")
    for file in os.listdir(current_directory):
        print(os.path.abspath(file))
    return input("Insira o diretório para onde deseja mudar (caminho absoluto): ")


def changeServerDirectory(ftp):
    print("Diretório atual: " + ftp.pwd())
    print("Diretório disponível: ")
    ftp.dir()
    directory = input("Enter the directory (relative path): ")
    ftp.cwd(directory)


def uploadFile(ftp, dir):
    filename = input(
        "Insira o nome do arquivo (relativo à localização atualmente escolhida): "
    )
    ftp.storbinary("STOR " + dir + "/" + filename, open(filename, "rb"))
    ftp.quit()


def downloadFile(ftp, dir):
    filename = input(
        "Insira o nome do arquivo (relativo à localização atualmente escolhida): "
    )
    localfile = open(dir + "/" + filename, "wb")
    ftp.retrbinary("RETR " + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()


def executeCommand(ftp):
    print("Comandos suportados:")
    print("─ " + "ls")
    print("  └ " + "lista os arquivos do diretório atual\n")
    print("─ " + "mv %1 %2")
    print("  └ " + "move o arquivo %1 para o diretório %2\n")
    print("─ " + "rm %1")
    print("  └ " + "remove o arquivo %1\n")
    print("─ " + "cd %1")
    print("  └ " + "muda o diretório atual para %1\n")
    print("─ " + "pwd")
    print("  └ " + "mostra o endereço atual\n")
    print("─ " + "rmdir %1")
    print("  └ " + "remove o diretório %1\n")
    print("─ " + "mkdir %1")
    print("  └ " + "cria um diretório %1\n")

    command = input("Insira o comando: ")

    cmd, *args = command.split(" ")

    if cmd == "ls":
        ftp.dir()
    elif command == "mv %1 %2":
        ftp.rename(args[0], args[1])
    elif cmd == "rm":
        ftp.delete(args[0])
    elif cmd == "cd":
        ftp.cwd(args[0])
    elif cmd == "pwd":
        ftp.pwd()
    elif cmd == "rmdir":
        ftp.rmd(args[0])
    elif cmd == "mkdir":
        ftp.mkd(args[0])
    else:
        print("Comando inválido")


if __name__ == "__main__":
    main()
