from pywinpipes import PipeServer

def new_message(client, message):
    print("New message recieved from server!")
    client.send_message("Message from server")

if __name__ == "__main__":
    pipe_sever = PipeServer(
        "TestPipe",
        new_message=new_message
        )