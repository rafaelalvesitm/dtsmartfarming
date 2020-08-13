import sys
sys.path.insert(0, "..")
import time
from opcua import ua, Server

if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4841/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "rafael"
    idx = server.reg(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space

    myobj = objects.add_object(idx, "CenterPivot") # Add Center pivot object



    # Add variables for all sprinklers
    sp1 = myobj.add_variable(idx, "sp1", 1 )
    sp1.set_writable() 
    sp2 = myobj.add_variable(idx, "sp2", 0)
    sp2.set_writable() 
    sp3 = myobj.add_variable(idx, "sp3", 0)
    sp3.set_writable() 
    sp4 = myobj.add_variable(idx, "sp4", 0)
    sp4.set_writable() 
    sp5 = myobj.add_variable(idx, "sp5", 0)
    sp5.set_writable() 
    sp6 = myobj.add_variable(idx, "sp6", 0)
    sp6.set_writable() 
    sp7 = myobj.add_variable(idx, "sp7", 0)
    sp7.set_writable() 
    sp8 = myobj.add_variable(idx, "sp8", 0)
    sp8.set_writable() 
    sp9 = myobj.add_variable(idx, "sp9", 0)
    sp9.set_writable() 
    sp10 = myobj.add_variable(idx, "sp10", 0)
    sp10.set_writable() 

    # Add variable to turn motor on/off
    motor = myobj.add_variable(idx, "motor", 0)
    motor.set_writable() 

    # starting!
    server.start()
    print(time)