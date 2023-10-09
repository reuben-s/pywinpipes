from pywinpipes import PipeServer

if __name__ == "__main__":
    pipe_sever = PipeServer("TestPipe")
    pipe_sever.wait_for_message()