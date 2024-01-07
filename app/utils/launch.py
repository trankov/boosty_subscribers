import socket

def random_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    sock.listen(1)
    port = sock.getsockname()[1]
    sock.close()
    return port

def read_allowed_extensions() -> list[str]:
    from conf.const import BASE_PATH
    ext_file_path = BASE_PATH / 'conf' / 'allowed_extensions.txt'
    extensions = ext_file_path.read_text().splitlines()
    return [f".{ext}" for ext in extensions]
