import socket
import select
import errno
from _thread import *


class clientLogic(object):

    HEADER_LENGTH = 10
    IP = "127.0.0.1"
    PORT = 1234

    def __init__(self, playername):
        self.playername = playername

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))
    client_socket.setblocking(False)
    username = my_username.encode("utf-8")
    username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
    client_socket.send(username_header + username)

    def fooo(p):
        while True:
            try:
                while True:
                    username_header = client_socket.recv(HEADER_LENGTH)

                    if not len(username_header):
                        print("Connection closed by the server")
                        sys.exit()

                    username_length = int(username_header.decode("utf-8").strip())

                    username = client_socket.recv(username_length).decode("utf-8")

                    message_header = client_socket.recv(HEADER_LENGTH)
                    message_length = int(message_header.decode("utf-8").strip())
                    message = client_socket.recv(message_length).decode("utf-8")

                    print()
                    print(f"{username} > {message}")

            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print("Reading error: {}".format(str(e)))
                    sys.exit()

                else:
                    continue
            except Exception as e:
                print("Reading error: ".format(str(e)))
                sys.exit()

    def main():
        start_new_thread(fooo, ("f",))

        while True:

            # Wait for user to input a message
            message = input(f"{my_username} > ")

            # If message is not empty - send it
            if message:

                # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
                message = message.encode("utf-8")
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
                client_socket.send(message_header + message)


if __name__ == "__main__":
    player = clientLogic(playerName)
    player.main()
