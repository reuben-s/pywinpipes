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

# Windows data type definitions

HANDLE  = c_void_p       # A handle to an object.
DWORD   = c_ulong        # A 32-bit unsigned integer.
LPDWORD = POINTER(DWORD) # Pointer to a DWORD type.
LPCWSTR = c_wchar_p      # A pointer to a constant null-terminated string of 16-bit Unicode characters.
BOOL    = c_bool         # A Boolean variable (should be TRUE or FALSE).
LPVOID  = c_void_p       # A pointer to any type.
LPCVOID = c_void_p       # A pointer to a constant of any type.

class SECURITY_ATTRIBUTES(Structure):
    _fields_ = [
        ("nLength", DWORD),
        ("lpSecurityDescriptor", c_void_p),
        ("bInheritHandle", BOOL)
    ]

LPSECURITY_ATTRIBUTES = POINTER(SECURITY_ATTRIBUTES)

# Load DLL

libname = Path().absolute() / "pywinpipes/bindings/x64/Debug/bindings.dll"
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
        byref(SECURITY_ATTRIBUTES()) # need to implement this properly
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
        LPVOID(lpBuffer),
        DWORD(nNumberOfBytesToRead),
        LPDWORD(lpNumberOfBytesRead)
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
        LPCVOID(lpBuffer),
        DWORD(nNumberOfBytesToWrite),
        LPDWORD(lpNumberOfBytesWritten)
    )

# CloseHandle()
cdll.bCloseHandle.argtypes = [ HANDLE ]
cdll.bCloseHandle.restype  = BOOL
def CloseHandle(hObject):
    return cdll.bCloseHandle(HANDLE(hFile))

# FlushFileBuffers()
cdll.bFlushFileBuffers.argtypes = [ HANDLE ]
cdll.bFlushFileBuffers.restype  = BOOL
def FlushFileBuffers(hFile):
    return cdll.bFlushFileBuffers(HANDLE(hFile))