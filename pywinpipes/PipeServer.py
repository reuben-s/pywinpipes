from win32pipe import (
    PIPE_ACCESS_DUPLEX,
    PIPE_TYPE_MESSAGE,
    PIPE_WAIT,
    PIPE_UNLIMITED_INSTANCES,
    PIPE_READMODE_MESSAGE,
)

from .bindings import (
    CreateNamedPipe,
    ConnectNamedPipe,
    DisconnectNamedPipe,
    HANDLE
)

PIPE_PREFIX: str = "\\\\.\\pipe\\"
BUFSIZE: int = 512

class PipeServer:
    def __init__(self, pipe_name: str) -> None:
        self._pipe_name = PIPE_PREFIX + pipe_name
        self._pipe: HANDLE  = None
        self._connected: bool = False

    def wait_for_message(self) -> None:
        try:
            self._pipe = CreateNamedPipe(
                self._pipe_name,          # Pipe name
                PIPE_ACCESS_DUPLEX,       # Read/write access
                PIPE_TYPE_MESSAGE |       # Message type pipe
                PIPE_WAIT |               # Message-read mode
                PIPE_READMODE_MESSAGE,    # Blocking mode
                PIPE_UNLIMITED_INSTANCES, # Max. instances
                BUFSIZE,                  # Output buffer size
                BUFSIZE,                  # Input buffer size
                0,                        # Client time-out
                None                      # Default security attribute
            )
            print(f"Pipe server: Awaiting client connection on {self._pipe_name}")

            self._connected = True if ConnectNamedPipe(self._pipe) else False

            DisconnectNamedPipe(self._pipe)
            print("Closed Pipe")

        except Exception as e:
            print(f"Failed to create pipe. Error: {e}")