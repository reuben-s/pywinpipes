# pywinpipes
Windows named pipes in pure Python.

## Implemented
- Win API Python bindings
- New pipe message callback
- Custom exceptions where needed

## To do
- Other various callbacks
- Pipe client wrapper

## Usage
Named pipe server
```python
from pywinpipes import PipeServer

def new_message(client, message):
    print(f"PID: {client.pid}, New Message -> \"{message}\"")
    client.send_message("Response from server")

if __name__ == "__main__":
    pipe_sever = PipeServer("TestPipe", # The pipe name is formatted as "\.\pipe\TestPipe"
                            new_message=new_message)
```

Named pipe client
```python
WIP
```
