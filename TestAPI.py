import socket


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return ("Connection active!")
    except OSError:
        pass
    return ("Disconnected :(")

print(is_connected())
