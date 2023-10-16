from .bindings import (
    CreateNamedPipe,
    ConnectNamedPipe,
    CloseHandle,
    GetLastError,
    HANDLE,
    INVALID_HANDLE_VALUE,
    PIPE_ACCESS_DUPLEX,
    PIPE_TYPE_MESSAGE,
    PIPE_WAIT,
    PIPE_UNLIMITED_INSTANCES,
    PIPE_READMODE_MESSAGE,
    ERROR_PIPE_CONNECTED
)
from .settings import BUFSIZE
from .ClientConnection import ClientConnection

from threading import Thread

PIPE_PREFIX = "\\\\.\\pipe\\"

class PipeServer:
    def __init__(
            self, 
            pipe_name, # Pipe name
            new_message=None,
            access_mode=PIPE_ACCESS_DUPLEX,       # Read/write access
            pipe_mode  =PIPE_TYPE_MESSAGE |       # Message type pipe
                        PIPE_WAIT |               # Message read mode
                        PIPE_READMODE_MESSAGE,    # Blocking mode
            max_clients=PIPE_UNLIMITED_INSTANCES, # Max. instances
            ):
        self._pipe_name = PIPE_PREFIX + pipe_name
        self._access_mode = access_mode
        self._pipe_mode = pipe_mode
        self._max_clients = max_clients
        self._connected = False
        self._value_returned = False

        # event callbacks
        self._new_message = new_message

        # connected clients
        self._clients = []

        # start listening for clients
        try:
            self._init_server()
        except Exception as e:
            for connection in self._clients:
                connection.end_connection()
            raise e

    def _init_server(self):
        while (True):
            self._pipe = CreateNamedPipe(
                self._pipe_name,
                self._access_mode,
                self._pipe_mode,
                self._max_clients,
                BUFSIZE,                  # Output buffer size
                BUFSIZE,                  # Input buffer size
                0,                        # Client time-out
                None                      # Default security attribute (Need to implement properly)
            )
            if self._pipe == INVALID_HANDLE_VALUE:
                raise Exception("CreateNamedPipe failed")  # Handle didn't open so no need to close it

            # Attempt to connect to client
            daemon_block = Thread(
                target=self._wait_for_connection,
                daemon=True
            )
            daemon_block.start()

            # Wait for ConnectNamedPipe to return a value
            while (not self._value_returned): continue

            # If successfully connected, create new ClientConnection class to manage connection
            if self._connected:
                self._clients.append(
                    ClientConnection(
                        self,
                        self._pipe,
                        self._new_message
                    )
                )
            else:
                CloseHandle(self._pipe) # Client couldn't connect so close the pipe handle

    def _wait_for_connection(self):
        self._value_returned = False
        print("Waiting for connection ..")
        self._connected = True if ConnectNamedPipe(self._pipe) else (GetLastError() == ERROR_PIPE_CONNECTED)
        self._value_returned = True