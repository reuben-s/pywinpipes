from .bindings import (
    ReadFile,
    WriteFile,
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

def WriteToNamedPipe(pipe, message):
    unicode_buffer = create_unicode_buffer(BUFSIZE)
    unicode_buffer.value = message
    bytes_written = c_ulong(0)

    success = WriteFile(
        pipe,
        unicode_buffer,
        sizeof(unicode_buffer),
        byref(bytes_written)
    )

    if (not success) or (sizeof(unicode_buffer) != bytes_written.value):
        raise Exception(f"WriteFile failed GLE={GetLastError()}")

    return success

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