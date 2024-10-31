from .bindings import (
    CreateFile,
    GetLastError,
    INVALID_HANDLE_VALUE,
    GENERIC_READ,
    GENERIC_WRITE,
    ERROR_PIPE_BUSY,
    OPEN_EXISTING
)

from .settings import BUFSIZE

import time

class PipeClient:
    def __init__(
            self,
            pipe_name,
            desired_access      =GENERIC_READ | 
                                 GENERIC_WRITE,
            share_mode          =0,
            creation_disposition=OPEN_EXISTING,
            flags_and_attributes=0,
            template_file       =None
            ):
        
        self._pipe_name = pipe_name
        self._desired_access = desired_access
        self._share_mode = share_mode
        self._creation_disposition = creation_disposition
        self._flags_and_attributes = flags_and_attributes
        self._template_file = template_file

        self._pipe = self._init_pipe()

        if self._pipe is not None:
            print("Pipe connected successfully.")


    def _init_pipe(self):
        while True:
            pipe = CreateFile(
                self._pipe_name,
                self._desired_access,
                self._share_mode,
                None,
                self._creation_disposition,
                self._flags_and_attributes,
                self._template_file
            )

            if pipe != INVALID_HANDLE_VALUE:
                return pipe # Unblock if pipe is created successfully.

            if (GetLastError() != ERROR_PIPE_BUSY):
                raise Exception(f"Could not open pipe. GLE={GetLastError()}")
            
            # All pipe instances are busy to wait for 20 seconds.
            time.sleep(20)