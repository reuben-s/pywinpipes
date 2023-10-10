from threading import (
    Thread
)

from .winapi_utils import (
    ReadFromNamedPipe,
    WriteToNamedPipe
)

from .exceptions import (
    CLIENT_DISCONNECTED,
    READFILE_FAILED
)

class ClientConnection:
    def __init__(self, pipe, new_message = None):
        self._pipe = pipe
        self._new_message = new_message
        
        # Create thread to recieve messages
        self._t = Thread(
            target=self._recieve_messages,
            daemon=True
        )
        self._t.start()

    def _recieve_messages(self):
        while True:
            try:
                message = ReadFromNamedPipe(self._pipe)
                if self._new_message:
                    self._new_message(self, message)
            except (
                CLIENT_DISCONNECTED, 
                READFILE_FAILED,
                ) as e:
                if isinstance(e, CLIENT_DISCONNECTED):
                    print("Client disconnected!")
                    break
                else:
                    print(f"Warning! ReadFile failed: {e}")

    def send_message(self, message):
        return WriteToNamedPipe(self._pipe, message)