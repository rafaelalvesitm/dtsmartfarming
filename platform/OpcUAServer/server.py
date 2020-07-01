from opcua import Server
import opcua

server = Server()

server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840")

name = "OPCUA_TEST"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace , "Parameters")
temp = Param.add_variable(addspace,"Temperature", 0)
press = Param.add_variable(addspace,"Pressure", 0)
time = Param.add_variable(addspace,"Time", 0)

temp.set_writable()
press.set_writable()
time.set_writable()

server.start()
print("server is starting!")