import socket

from typing import \
    Self

from src.code.logger import \
    log_error ,\
    log_client,\
    log_fatal_error

from src.code.loader import \
    dict_to_str,\
    str_to_dict,\
    IPv4

class Network:
    def __init__(
        self
    ) -> None:
        self.client: socket.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        
        port = None
        while port is None:
            port = input("port: ")
            try:
                port = int(port)
            except:
                log_error(
                    "Invalid port"
                )
                port = None
        self.port: int | None = port

        self.address: tuple[str, int] = (
            IPv4,
            self.port
        )

        self.connect()

    def connect(
        self
    ) -> dict | str | None:
        try:
            self.client.connect(
                self.address
            )
            log_client(
                IPv4,
                f"CONNECTED TO [SERVER]"
            )
            data: str = self.client.recv(16 * 2**10).decode()

            try: 
                return str_to_dict(data)
            except Exception as e:
                log_error(f"Couldn\'t decode connection reply msg: {data}\nException: {e}")
                return data

        except Exception as e:
            log_fatal_error(
                f"Couldn\'t connect to {self.address}\nException: {e}"
            )
            exit(1)

    def send(
        self: Self,
        data: str | dict
    ) -> dict | str | None:
        try:
            if type(data) == dict:
                data_: dict = data
            elif type(data) == str:
                data_: dict = str_to_dict(data)
            else:
                log_error(f"Given argument is not a str nor a dict; message not sent: {data}")
                return None

            # now {data_} is surely a dict
            self.client.send(str.encode(dict_to_str(data_)))

            # getting response
            if not data_.get("need_response", False):
                return None
            
            recv_str: str = self.client.recv(16 * 2**10).decode()
            log_client(
                IPv4
            )
            try:
                dict_: dict = str_to_dict(recv_str)
                return dict_
            except Exception as e:
                log_error(f"Couldn\'t decode reply msg: {data}\nException: {e}")
                return recv_str
        
        except socket.error as e:
            log_error(f"[{IPv4}]: {e}")
        
        except Exception as e:
            log_error(f"[{IPv4}]: {e}")
    
    def close(
        self: Self
    ) -> None:
        self.send({
            "type": "exit",
            "need_response": False
        })
