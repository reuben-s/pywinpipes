# custom exceptions will go here

class CLIENT_DISCONNECTED(Exception):
    pass

class READFILE_FAILED(Exception):
    pass

class WRITEFILE_FAILED(Exception):
    pass

class ERROR_PIPE_LISTENING(Exception):
    pass