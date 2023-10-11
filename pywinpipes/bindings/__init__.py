from bindings import (
    # dwOpenMode param
    PIPE_ACCESS_DUPLEX,
    PIPE_ACCESS_INBOUND,
    PIPE_ACCESS_OUTBOUND,

    FILE_FLAG_FIRST_PIPE_INSTANCE,
    FILE_FLAG_WRITE_THROUGH,
    FILE_FLAG_OVERLAPPED,
    # dwPipeMode param
    PIPE_TYPE_BYTE,
    PIPE_TYPE_MESSAGE,
    PIPE_READMODE_BYTE,
    PIPE_READMODE_MESSAGE,

    PIPE_WAIT,
    PIPE_NOWAIT,

    PIPE_ACCEPT_REMOTE_CLIENTS,
    PIPE_REJECT_REMOTE_CLIENTS,
    # nMaxInstances param
    PIPE_UNLIMITED_INSTANCES,
)

__all__ = (
    "PIPE_ACCESS_DUPLEX",
    "PIPE_ACCESS_INBOUND",
    "PIPE_ACCESS_OUTBOUND",
    "FILE_FLAG_FIRST_PIPE_INSTANCE",
    "FILE_FLAG_WRITE_THROUGH",
    "FILE_FLAG_OVERLAPPED",
    "PIPE_TYPE_BYTE",
    "PIPE_TYPE_MESSAGE",
    "PIPE_READMODE_BYTE",
    "PIPE_READMODE_MESSAGE",
    "PIPE_WAIT",
    "PIPE_NOWAIT",
    "PIPE_ACCEPT_REMOTE_CLIENTS",
    "PIPE_REJECT_REMOTE_CLIENTS",
    "PIPE_UNLIMITED_INSTANCES",
)