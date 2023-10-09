from .bindings import (
    ReadFile,
    DWORD,
    GetLastError,
    ERROR_BROKEN_PIPE
)

from ctypes import (
    create_unicode_buffer,
    sizeof,
    byref,
    c_ulong
)

from .settings import BUFSIZE

def WriteToNamedPipe():
    pass

def ReadFromNamedPipe(pipe):
    unicode_buffer = create_unicode_buffer(BUFSIZE)
    bytes_read = c_ulong(0)

    success = ReadFile(
        pipe,
        unicode_buffer,
        sizeof(unicode_buffer),
        byref(bytes_read)
    )

    if (not success) or (bytes_read == 0):
        if GetLastError() == ERROR_BROKEN_PIPE:
            raise Exception("Client Disconnected")
        else:
            raise Exception(f"ReadFile failed GLE={GetLastError()}")
    
    return unicode_buffer.value