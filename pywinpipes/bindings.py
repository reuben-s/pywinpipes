from ctypes import (
    c_void_p,
    c_ulong,
    POINTER,
    c_wchar_p,
    c_bool,
    Structure,
    windll
)

# CreateNamedPipe Parameters

# dwOpenMode
PIPE_ACCESS_DUPLEX   = 0x00000003
PIPE_ACCESS_INBOUND  = 0x00000001
PIPE_ACCESS_OUTBOUND = 0x00000002

FILE_FLAG_FIRST_PIPE_INSTANCE = 0x00080000
FILE_FLAG_WRITE_THROUGH       = 0x80000000
FILE_FLAG_OVERLAPPED          = 0x40000000

# dwPipeMode
PIPE_TYPE_BYTE        = 0x00000000
PIPE_TYPE_MESSAGE     = 0x00000004
PIPE_READMODE_BYTE    = 0x00000000
PIPE_READMODE_MESSAGE = 0x00000002

PIPE_WAIT   = 0x00000000
PIPE_NOWAIT = 0x00000001

PIPE_ACCEPT_REMOTE_CLIENTS = 0x00000000
PIPE_REJECT_REMOTE_CLIENTS = 0x00000008

# nMaxInstances
PIPE_UNLIMITED_INSTANCES = 255

# Error codes

INVALID_HANDLE_VALUE = -1
ERROR_PIPE_CONNECTED = 535
ERROR_BROKEN_PIPE    = 109
ERROR_PIPE_LISTENING = 536

# Windows data type definitions

HANDLE  = c_void_p          # A handle to an object.
DWORD   = c_ulong           # A 32-bit unsigned integer.
LPCWSTR = c_wchar_p         # A pointer to a constant null-terminated string of 16-bit Unicode characters.
BOOL    = c_bool            # A Boolean variable (should be TRUE or FALSE).
LPVOID  = c_void_p          # A pointer to any type.
LPCVOID = c_void_p          # A pointer to a constant of any type.
LPDWORD = POINTER(DWORD)    # Pointer to a DWORD type.
LPOVERLAPPED = c_void_p

class SECURITY_ATTRIBUTES(Structure):
    _fields_ = [
        ("nLength", DWORD),
        ("lpSecurityDescriptor", c_void_p),
        ("bInheritHandle", BOOL)
    ]

LPSECURITY_ATTRIBUTES = POINTER(SECURITY_ATTRIBUTES)

# Load kernel32.dll

kernel32 = windll.LoadLibrary("kernel32.dll")

# Define bindings for windows API functions

# CreateNamedPipe()
CreateNamedPipe = kernel32.CreateNamedPipeW
CreateNamedPipe.argtypes = [
    LPCWSTR,
    DWORD,
    DWORD,
    DWORD,
    DWORD,
    DWORD,
    DWORD,
    LPSECURITY_ATTRIBUTES
]
CreateNamedPipe.restype = HANDLE

# DisconnectNamedPipe()
DisconnectNamedPipe = kernel32.DisconnectNamedPipe
DisconnectNamedPipe.argtypes = [ HANDLE ]
DisconnectNamedPipe.restype  = BOOL

# CloseHandle()
CloseHandle = kernel32.CloseHandle
CloseHandle.argtypes = [ HANDLE ]
CloseHandle.restype  = BOOL

# FlushFileBuffers()
FlushFileBuffers = kernel32.FlushFileBuffers
kernel32.FlushFileBuffers.argtypes = [ HANDLE ]
kernel32.FlushFileBuffers.restype  = BOOL

# GetLastError()
GetLastError = kernel32.GetLastError
kernel32.GetLastError.restype = DWORD

# All of the following functions are wrapped in a simple function so that lpOverlapped doesn't have to be passed

# ConnectNamedPipe()
kernel32.ConnectNamedPipe.argtypes = [ 
    HANDLE, 
    LPOVERLAPPED 
]
kernel32.ConnectNamedPipe.restype  = BOOL
def ConnectNamedPipe(hNamedPipe):
    return kernel32.ConnectNamedPipe(
        hNamedPipe, 
        None
    )

# WriteFile()
kernel32.WriteFile.argtypes = [
    HANDLE,
    LPCVOID,
    DWORD,
    LPDWORD,
    LPOVERLAPPED
]
kernel32.WriteFile.restype  = BOOL
def WriteFile(
    hFile, 
    lpBuffer, 
    nNumberOfBytesToWrite, 
    lpNumberOfBytesWritten
    ):
    return kernel32.WriteFile(
        hFile,
        lpBuffer,
        nNumberOfBytesToWrite,
        lpNumberOfBytesWritten,
        None
    )

# ReadFile()
kernel32.ReadFile.argtypes = [
    HANDLE,
    LPVOID,
    DWORD,
    LPDWORD,
    LPOVERLAPPED
]
kernel32.ReadFile.restype  = BOOL
def ReadFile(
    hFile, 
    lpBuffer, 
    nNumberOfBytesToRead, 
    lpNumberOfBytesRead
    ):
    return kernel32.ReadFile(
        hFile, 
        lpBuffer, 
        nNumberOfBytesToRead, 
        lpNumberOfBytesRead, 
        None
    )

# GetNamedPipeClientProcessId()
kernel32.GetNamedPipeClientProcessId.argtypes = [
    HANDLE,
    LPDWORD
]
kernel32.GetNamedPipeClientProcessId.restype = BOOL
def GetNamedPipeClientProcessId(
    hPipe, 
    ClientProcessId
    ):
    return kernel32.GetNamedPipeClientProcessId(
        hPipe,
        ClientProcessId
    )