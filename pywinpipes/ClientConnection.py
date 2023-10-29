from .winapi_utils import (
    ReadFromNamedPipe,
    WriteToNamedPipe,
    GetClientPID
)
from .exceptions import (
    CLIENT_DISCONNECTED,
    READFILE_FAILED
)
from .bindings import (
    DisconnectNamedPipe,
    CloseHandle,
    FlushFileBuffers
)

from threading import Thread

class ClientConnection:
    def __init__(self, server, pipe, new_message=None):
        print("New client connnection created")

        self._server = server
        self._pipe = pipe
        self._new_message = new_message

        self.pid = GetClientPID(self._pipe)

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
                if isinstance(e, READFILE_FAILED):
                    print(f"Warning! ReadFile failed: {e}")
                else:
                    # some other error, we need to stop listening for messages as the connection is probably dead
                    print(e)
                    break
        
        # cleanup dead connection
        self.end_connection()

    def end_connection(self):
        FlushFileBuffers(self._pipe)
        DisconnectNamedPipe(self._pipe)
        CloseHandle(self._pipe)
        del self._server._clients[self._server._clients.index(self)]

    def send_message(self, message):
        return WriteToNamedPipe(self._pipe, message)