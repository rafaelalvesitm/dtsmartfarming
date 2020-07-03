from opcua import Server
import opcua

server = Server()

server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840")

name = "OPCUA_TEST"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object('ns=3;i=1000' , "Parameters")
temp = Param.add_variable('ns=3;s=Temperature',"Temperature", 0)
press = Param.add_variable('ns=3;s=Pressure',"Pressure", 0)
current = Param.add_variable('ns=3;s=Current',"Current", 0)

temp.set_writable()
press.set_writable()
current.set_writable()

server.start()
print("server is starting!")