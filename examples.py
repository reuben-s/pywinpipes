from pywinpipes import PipeServer

def main():
    pipe_server = PipeServer("ExampleServer")
    pipe_server.wait_for_message()

if __name__ == "__main__":
    main()