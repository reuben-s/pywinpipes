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

HANDLE  = c_void_p       # HANDLE is a pointer ((I think I need to implement the handle type properly))

DWORD   = c_ulong        # A 32-bit unsigned integer.
LPDWORD = POINTER(DWORD) # Pointer to a DWORD type.
LPCWSTR = c_wchar_p      # A pointer to a constant null-terminated string of 16-bit Unicode characters.
BOOL    = c_bool         # A Boolean variable (should be TRUE or FALSE).
LPVOID  = c_void_p       # A pointer to any type.

class SECURITY_ATTRIBUTES(Structure):
    _fields_ = [
        ("nLength", DWORD),
        ("lpSecurityDescriptor", c_void_p),
        ("bInheritHandle", BOOL)
    ]


# Load DLL

libname = Path().absolute() / "pywinpipes/bindings/x64/Debug/bindings.dll"
cdll = CDLL(str(libname))


# Define bindings for C++ functions

# CreateNamedPipe()
cdll.bCreateNamedPipe.restype = HANDLE
def CreateNamedPipe(lpName, dwOpenMode, dwPipeMode, nMaxInstances, nOutBufferSize, nInBufferSize, nDefaultTimeOut, lpSecurityAttributes) -> BOOL:
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
cdll.bConnectNamedPipe.restype = BOOL
def ConnectNamedPipe(hNamedPipe):
    return cdll.bConnectNamedPipe(
        HANDLE(hNamedPipe)
    )

# DisconnectNamedPipe()
cdll.bDisconnectNamedPipe.restype = BOOL
def DisconnectNamedPipe(hNamedPipe):
    return cdll.bDisconnectNamedPipe(
        HANDLE(hNamedPipe)
    )