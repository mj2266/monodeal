import socket
import select
import errno
import sys
from _thread import *


class clientLogic():



    def __init__(self, playername):
        self.playername = playername

        self.HEADER_LENGTH = 10
        self.IP = "127.0.0.1"
        self.PORT = 1234

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.IP, self.PORT))
        self.client_socket.setblocking(False)
        self.username = self.playername.encode("utf-8")
        self.username_header = f"{len(self.username):<{self.HEADER_LENGTH}}".encode("utf-8")
        self.client_socket.send(self.username_header + self.username)

    def fooo(self):
        while True:
            try:
                while True:
                    username_header = self.client_socket.recv(self.HEADER_LENGTH)

                    if not len(username_header):
                        print("Connection closed by the server")
                        sys.exit()

                    username_length = int(username_header.decode("utf-8").strip())

                    username = self.client_socket.recv(username_length).decode("utf-8")

                    message_header = self.client_socket.recv(self.HEADER_LENGTH)
                    message_length = int(message_header.decode("utf-8").strip())
                    message = self.client_socket.recv(message_length).decode("utf-8")

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

    def main(self):
        start_new_thread(self.fooo, ("f",))

        while True:

            # Wait for user to input a message
            message = input(f"{self.playername} > ")

            # If message is not empty - send it
            if message:

                # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
                message = message.encode("utf-8")
                message_header = f"{len(message):<{self.HEADER_LENGTH}}".encode("utf-8")
                self.client_socket.send(message_header + message)


if __name__ == "__main__":
    playerName = "Babbar"
    player = clientLogic(playerName)
    player.main()
