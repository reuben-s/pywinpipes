from pywinpipes import PipeServer

def new_message(client, message):
    print(f"New message recieved from server! \"{message}\"")
    client.send_message("Response from server")

if __name__ == "__main__":
    pipe_sever = PipeServer(
        "TestPipe",
        new_message=new_message
        )