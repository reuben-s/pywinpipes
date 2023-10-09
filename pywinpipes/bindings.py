from pathlib import (
    Path
)

from ctypes import (
    c_void_p,
    c_ulong,
    POINTER,
    c_wchar_p,
    c_bool,
    c_void_p,
    CDLL,
    Structure,
    byref
)

# Parameters

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

# Windows data type definitions

HANDLE  = c_void_p       # A handle to an object.
DWORD   = c_ulong        # A 32-bit unsigned integer.
LPCWSTR = c_wchar_p      # A pointer to a constant null-terminated string of 16-bit Unicode characters.
BOOL    = c_bool         # A Boolean variable (should be TRUE or FALSE).
LPVOID  = c_void_p       # A pointer to any type.
LPCVOID = c_void_p       # A pointer to a constant of any type.
LPDWORD = POINTER(DWORD) # Pointer to a DWORD type.

class SECURITY_ATTRIBUTES(Structure):
    _fields_ = [
        ("nLength", DWORD),
        ("lpSecurityDescriptor", c_void_p),
        ("bInheritHandle", BOOL)
    ]

LPSECURITY_ATTRIBUTES = POINTER(SECURITY_ATTRIBUTES)

# Load DLL

libname = Path().absolute() / "pywinpipes/bindings/bindings.dll"
cdll = CDLL(str(libname))

# Define bindings for C++ functions

# CreateNamedPipe()
cdll.bCreateNamedPipe.argtypes = [
    LPCWSTR,
    DWORD,
    DWORD,
    DWORD,
    DWORD,
    DWORD,
    DWORD,
    LPSECURITY_ATTRIBUTES
]
cdll.bCreateNamedPipe.restype  = HANDLE
def CreateNamedPipe(
    lpName, 
    dwOpenMode, 
    dwPipeMode, 
    nMaxInstances, 
    nOutBufferSize, 
    nInBufferSize, 
    nDefaultTimeOut, 
    lpSecurityAttributes
    ):
    return cdll.bCreateNamedPipe(
        LPCWSTR(lpName), 
        DWORD(dwOpenMode), 
        DWORD(dwPipeMode), 
        DWORD(nMaxInstances), 
        DWORD(nOutBufferSize), 
        DWORD(nInBufferSize), 
        DWORD(nDefaultTimeOut), 
        None
    )

# ConnectNamedPipe()
cdll.bConnectNamedPipe.argtypes = [ HANDLE ]
cdll.bConnectNamedPipe.restype  = BOOL
def ConnectNamedPipe(hNamedPipe):
    return cdll.bConnectNamedPipe(HANDLE(hNamedPipe))

# DisconnectNamedPipe()
cdll.bDisconnectNamedPipe.argtypes = [ HANDLE ]
cdll.bDisconnectNamedPipe.restype  = BOOL
def DisconnectNamedPipe(hNamedPipe):
    return cdll.bDisconnectNamedPipe(HANDLE(hNamedPipe))

# ReadFile()
cdll.bReadFile.argtypes = [
    HANDLE,
    LPVOID,
    DWORD,
    LPDWORD
]
cdll.bReadFile.restype  = BOOL
def ReadFile(
    hFile, 
    lpBuffer, 
    nNumberOfBytesToRead, 
    lpNumberOfBytesRead
    ):
    return cdll.bReadFile(
        HANDLE(hFile),
        lpBuffer, # unicode buffer passed from calling function so no casting needed.
        DWORD(nNumberOfBytesToRead),
        lpNumberOfBytesRead # Have to pass by ref from the calling function so no casting needed.
    )

# WriteFile()
cdll.bWriteFile.argtypes = [
    HANDLE,
    LPCVOID,
    DWORD,
    LPDWORD
]
cdll.bWriteFile.restype  = BOOL
def WriteFile(
    hFile, 
    lpBuffer, 
    nNumberOfBytesToWrite, 
    lpNumberOfBytesWritten
    ):
    return cdll.bWriteFile(
        HANDLE(hFile),
        lpBuffer, # unicode buffer passed from calling function so no casting needed.
        DWORD(nNumberOfBytesToWrite),
        lpNumberOfBytesWritten # Have to pass by ref from the calling function so no casting needed.
    )

# CloseHandle()
cdll.bCloseHandle.argtypes = [ HANDLE ]
cdll.bCloseHandle.restype  = BOOL
def CloseHandle(hObject):
    return cdll.bCloseHandle(HANDLE(hObject))

# FlushFileBuffers()
cdll.bFlushFileBuffers.argtypes = [ HANDLE ]
cdll.bFlushFileBuffers.restype  = BOOL
def FlushFileBuffers(hFile):
    return cdll.bFlushFileBuffers(HANDLE(hFile))

# GetLastError()
cdll.bGetLastError.restype = DWORD
def GetLastError():
    return cdll.bGetLastError()