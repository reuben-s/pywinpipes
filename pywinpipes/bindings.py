import pathlib
import ctypes

# Define necessary data types
HANDLE = ctypes.c_void_p  # HANDLE is a pointer
DWORD = ctypes.c_ulong    # DWORD is an unsigned 32-bit integer
LPCWSTR = ctypes.c_wchar_p  # LPCWSTR is a pointer to a constant wide (Unicode) string
BOOL = ctypes.c_bool

# Define the structure for LPSECURITY_ATTRIBUTES
class SECURITY_ATTRIBUTES(ctypes.Structure):
    _fields_ = [("nLength", DWORD),
                ("lpSecurityDescriptor", ctypes.c_void_p),
                ("bInheritHandle", BOOL)]


libname = pathlib.Path().absolute() / "pywinpipes/bindings/x64/Debug/bindings.dll"
cdll = ctypes.CDLL(str(libname))

# Define the function prototype for bCreateNamedPipe
cdll.bCreateNamedPipe.restype = HANDLE
def CreateNamedPipe(lpName, dwOpenMode, dwPipeMode, nMaxInstances, nOutBufferSize, nInBufferSize, nDefaultTimeOut, lpSecurityAttributes) -> BOOL:
    # Call bCreateNamedPipe
    return cdll.bCreateNamedPipe(
        LPCWSTR(lpName), 
        DWORD(dwOpenMode), 
        DWORD(dwPipeMode), 
        DWORD(nMaxInstances), 
        DWORD(nOutBufferSize), 
        DWORD(nInBufferSize), 
        DWORD(nDefaultTimeOut), 
        ctypes.byref(SECURITY_ATTRIBUTES()) # need to implement this properly
    )

# Define the function prototype for bConnectNamedPipe
cdll.bConnectNamedPipe.restype = BOOL
def ConnectNamedPipe(hNamedPipe, lpOverlapped):
    # Call bConnectNamedPipe
    return cdll.bConnectNamedPipe(
        HANDLE(hNamedPipe),
        None # need to implement this properly
    )

# Define the function prototype for bDisconnectNamedPipe
cdll.bDisconnectNamedPipe.restype = BOOL
def DisconnectNamedPipe(hNamedPipe, lpOverlapped):
    # Call bDisconnectNamedPipe
    return cdll.bDisconnectNamedPipe(
        HANDLE(hNamedPipe)
    )

# Define the function prototype for bReadFile
cdll.bReadFile.restype = ctypes.c_wchar_p
def ReadFile(hNamedPipe, lpOverlapped):
    # Call bReadFile
    value = cdll.bReadFile(
        HANDLE(hNamedPipe),
        None # need to implement this properly
    )

    return ctypes.wstring_at(value)