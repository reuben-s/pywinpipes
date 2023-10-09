from .bindings import (
    CreateNamedPipe,
    ConnectNamedPipe,
    DisconnectNamedPipe,
    CloseHandle,
    GetLastError,
    HANDLE,
    INVALID_HANDLE_VALUE,
    PIPE_ACCESS_DUPLEX,
    PIPE_TYPE_MESSAGE,
    PIPE_WAIT,
    PIPE_UNLIMITED_INSTANCES,
    PIPE_READMODE_MESSAGE,
)

from .settings import BUFSIZE

from .winapi_utils import (
    ReadFromNamedPipe,
    WriteToNamedPipe
)

PIPE_PREFIX: str = "\\\\.\\pipe\\"

class PipeServer:
    def __init__(self, pipe_name: str) -> None:
        self._pipe_name = PIPE_PREFIX + pipe_name

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
        if self._pipe == INVALID_HANDLE_VALUE:
            raise Exception("CreateNamedPipe failed")  # Handle didn't open so no need to close it

        self._connected = True if ConnectNamedPipe(self._pipe) else (GetLastError() == ERROR_PIPE_CONNECTED)
        if self._connected:
            message = ReadFromNamedPipe(self._pipe)
            WriteToNamedPipe(self._pipe, "Hello from the server!")

        else:
            # Client could not connect so close pipe
            CloseHandle(self._pipe)