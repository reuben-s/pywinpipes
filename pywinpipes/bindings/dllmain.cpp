#include "pch.h"

#include <iostream>
#include <string>

#define EXPORT_SYMBOL __declspec(dllexport)
#define BUFSIZE 512

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
        HANDLE hNamedPipe,
        LPOVERLAPPED lpOverlapped
    ) 
    {
        return ConnectNamedPipe(
            hNamedPipe,     // Pipe handle
            lpOverlapped    // OVERLAPPED structure for asynchronous operations.
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

    // I decided to handle the ReadFile() buffer functionality completely in C++ and return the value read to simplify pointers usage which is not nice in Python
    EXPORT_SYMBOL
    wchar_t* bReadFile(
        HANDLE hFile,
        LPOVERLAPPED lpOverlapped
    ) 
    {
        HANDLE hHeap = GetProcessHeap();
        TCHAR* pchRequest = (TCHAR*)HeapAlloc(hHeap, 0, BUFSIZE * sizeof(TCHAR));

        DWORD cbBytesRead = 0, cbReplyBytes = 0, cbWritten = 0;
        BOOL fSuccess = FALSE;
        HANDLE hPipe = NULL;

        fSuccess = ReadFile(
            hFile,                      // File handle
            pchRequest,                 // Data collection buffer
            BUFSIZE * sizeof(TCHAR),    // Max bytes
            &cbBytesRead,               // Pointer to number of bytes read
            lpOverlapped                // OVERLAPPED structure for asynchronous operations.
        );

        if (!fSuccess || cbBytesRead == 0)
        {
            if (GetLastError() == ERROR_BROKEN_PIPE)
                // throw std::exception("Pipe client disconnected.");
                std::cout << "error";
            else
                // throw std::exception("ReadFile failed, GLE=" + GetLastError());
                std::cout << "error";
        }
        
        if (cbBytesRead > 0)
        {
            return pchRequest;
        }

        return nullptr;

    }

}
