#include "pch.h"

#include <iostream>
#include <string>

#define EXPORT_SYMBOL __declspec(dllexport)

extern "C" 
{

    EXPORT_SYMBOL
    HANDLE bCreateNamedPipe(
        LPCWSTR               lpName,
        DWORD                 dwOpenMode,
        DWORD                 dwPipeMode,
        DWORD                 nMaxInstances,
        DWORD                 nOutBufferSize,
        DWORD                 nInBufferSize,
        DWORD                 nDefaultTimeOut,
        LPSECURITY_ATTRIBUTES lpSecurityAttributes
    ) 
    {
        return CreateNamedPipe(
            lpName,                 // Pipe name
            dwOpenMode,             // Pipe open mode
            dwPipeMode,             // Pipe mode
            nMaxInstances,          // Maximum number of instances
            nOutBufferSize,         // Output buffer size
            nInBufferSize,          // Input buffer size
            nDefaultTimeOut,        // Default timeout
            lpSecurityAttributes    // Security attributes
        );
    }


    EXPORT_SYMBOL
    BOOL bConnectNamedPipe(
        HANDLE hNamedPipe
    ) 
    {
        return ConnectNamedPipe(
            hNamedPipe,     // Pipe handle
            NULL            // OVERLAPPED structure for asynchronous operations.
        );
    }

    EXPORT_SYMBOL
    BOOL bDisconnectNamedPipe(
        HANDLE hNamedPipe
    )
    {
        return DisconnectNamedPipe(
            hNamedPipe    // Pipe Handle
        );
    }


    EXPORT_SYMBOL
    BOOL bReadFile(
        HANDLE hFile,
        LPVOID lpBuffer,
        DWORD nNumberOfBytesToRead,
        LPDWORD lpNumberOfBytesRead
    ) 
    {
        return ReadFile(
            hFile,                   // A handle to the file or I/O device to be read from.
            lpBuffer,                // A pointer to the buffer that receives the data read from the file.
            nNumberOfBytesToRead,    // The maximum number of bytes to be read.
            lpNumberOfBytesRead,     // A pointer to the variable that receives the number of bytes read.
            NULL                     // A pointer to an OVERLAPPED structure for asynchronous operations.
        );
    }


    EXPORT_SYMBOL
    BOOL bWriteFile(
        HANDLE hFile,
        LPCVOID lpBuffer,
        DWORD nNumberOfBytesToWrite,
        LPDWORD lpNumberOfBytesWritten
    ) 
    {
        return WriteFile(
            hFile,                     // A handle to the file or I/O device to be written to.
            lpBuffer,                  // A pointer to the buffer containing the data to be written.
            nNumberOfBytesToWrite,     // The number of bytes to be written from the buffer.
            lpNumberOfBytesWritten,    // A pointer to the variable that receives the number of bytes written.
            NULL                       // A pointer to an OVERLAPPED structure for asynchronous operations.
        );
    }

    EXPORT_SYMBOL
    BOOL bCloseHandle(
        HANDLE hObject
    )
    {
        return CloseHandle(
            hObject    // Handle object to be closed
        );
    }

    EXPORT_SYMBOL
    BOOL bFlushFileBuffers(
        HANDLE hFile
    )
    {
        return FlushFileBuffers(
            hFile     // Handle to file to have buffers flushed.
        );
    }

}
