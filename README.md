# pywinpipes
Windows named pipes in pure Python.

## Implemented
- Win API C++ Python bindings
- New pipe message callback
- Custom exceptions where needed

## To do
- Fix blocking behaviour from C++ dll
- Other various callbacks
- Pipe client wrapper

## Usage
```python
from pywinpipes import PipeServer

def new_message(client, message):
    print("New message recieved from server!")
    client.send_message("Message from server")

if __name__ == "__main__":
    pipe_sever = PipeServer(
        "PipeName", # pipe name, can be accessed from other programms via "\\.\pipe\PipeName"
        new_message=new_message
        )
```