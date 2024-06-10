import socket
import _thread

from typing import \
    Self

from src.code.const import \
    JsonReturn

from src.code.logger import \
    log_server,\
    log_error

from src.code.loader import \
    str_to_dict,\
    dict_to_str,\
    IPv4

class Server:
    def __init__(
        self: Self
    ) -> None:
        """
        Creates a server.
        For now, only one should be started at a time, if you don\'t want a crash.
        """

        self.SERVER: socket.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        try:
            self.SERVER.bind((IPv4, 0))
        except Exception as e:
            log_server(f": Couldn't bind: {e}")
            exit(1)

        self.ADDRESS: tuple[str, int] = self.SERVER.getsockname()  # (IPv4, PORT) = ADDRESS
        self.PORT: int = self.ADDRESS[1]


    def stop(
        self: Self
    ) -> None:
        # TODO be regardful to the clients connected 
        self.SERVER.close()

    
    def send_to(
        self: Self
    ) -> None:
        """
        TODO not implemented
        """
        pass


    def respond_to_client(
        self: Self,
        respond_to: JsonReturn,
        connection: socket.socket
    ) -> None:
        """
        Used by the \'handle_client\' method.
        It is suggested to not use it alone.
        """
        
        reply: dict[str] = {
            "type": "reply",
            "reply-to-type": respond_to.get("type", None),
            "need_response": False,
            "msg": "not implemented answer"
        }

        match respond_to.get("type", None):

            case "exit":
                reply["msg"] = "why do you need a reply to an exit message?"

            case _:
                reply["msg"] = "not implemented to answer"

        connection.send(
            str.encode(
                dict_to_str(
                    reply
        )))


    def handle_client(
        self: Self,
        connection: socket.socket,
        address: tuple[str, int]
    ) -> None:
        connection.send(
            str.encode(
                dict_to_str({
                    "type": "reply",
                    "msg": "connected"
        })))

        while True:
            try:
                data: bytes = connection.recv(16 * 2**10)
                str_msg: str = data.decode("utf-8")

                if not str_msg:
                    continue
                
                dict_msg: dict = str_to_dict(str_msg)

                match dict_msg.get("type", None):
                    case "exit":
                        break
                    case _:
                        pass

                log_server(f"[{address[0]}]: GOT: {dict_msg = }")

                # RESPOND
                if not dict_msg.get("need_response", False):
                    continue
                print("responding")
                self.respond_to_client(
                    dict_msg,
                    connection
                )

            except Exception as e:
                log_error(f"[SERVER][{address[0]}]: Couldn\'t decode message")
                break
            
        log_server(f"[{address[0]}]: DISCONNECTED")
        connection.close()


    def run(
        self: Self
    ) -> None:
        """
        If you want to run something else as well, try using \'start\'.
        """

        self.SERVER.listen(2)
        log_server(
            f": STARTING AT {IPv4}:{self.PORT}"
        )

        while True:
            connection, address = self.SERVER.accept()
            log_server(
                f"[{address[0]}]: CONNECTED WITH PORT {address[1]}"
            )

            _thread.start_new_thread(
                self.handle_client, (
                    connection,
                    address
                )
            )

    
    def start(
        self: Self
    ) -> None:
        _thread.start_new_thread(
            self.run,
            tuple()
        )
