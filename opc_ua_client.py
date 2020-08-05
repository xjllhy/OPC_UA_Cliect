import opcua
import time



client = opcua.Client("opc.tcp://127.0.0.1:51212/freeopcua/server/")
client.connect()
uri = "127.0.0.1"
idx=client.get_namespace_index(uri)
objects = client.get_root_node()


var = objects.get_child(["0:Objects", "2:GEDATA", "2:t1"])
while 1:
    print("Value of variable is:", var.get_value())
    time.sleep(0.02)
