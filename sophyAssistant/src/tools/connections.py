import socket

def available():
    try:
        socket.create_connection(("www.google.com", 443))
        return True
    except OSError:
        pass
    return False