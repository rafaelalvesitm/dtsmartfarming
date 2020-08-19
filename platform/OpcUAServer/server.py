from opcua import ua, Server, uamethod
from opcua.ua.uaerrors import UaStatusCodeError
import opcua
from datetime import datetime

# Setup server endpoint
server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840")

# Register a new namespace (ns=2)
name = "OPCUA_TEST"
idx = server.register_namespace(name)

#Main Node
node = server.get_objects_node()

# Define pump parameter
pump = node.add_object(idx,"Pump")
pump_closed = pump.add_variable(idx, "pump_closed", True) # Plant Simulation uses Exit Closed so I called 
pump_closed.set_writable()
pump_q = pump.add_variable(idx, "pump_q", 0.0) # Pump flow rate
pump_q.set_writable()

# Define control área parameter
control = node.add_object(idx,"Control")

# Add variable to each of the 3 sprinklers for the Control Area
c_sp1_open = control.add_variable(idx, "c_sp1_open", False) # Sprinkler Open
c_sp1_open.set_writable()
c_sp1_q = control.add_variable(idx, "c_sp1_q", 0.0) # Sprinkler Flowrate
c_sp1_q.set_writable()
c_sp2_open = control.add_variable(idx, "c_sp2_open", False) # Sprinkler Open
c_sp2_open.set_writable()
c_sp2_q = control.add_variable(idx, "c_sp2_q", 0.0) # Sprinkler Flowrate
c_sp2_q.set_writable()
c_sp3_open = control.add_variable(idx, "c_sp3_open", False) # Sprinkler Open
c_sp3_open.set_writable()
c_sp3_q = control.add_variable(idx, "c_sp3_q", 0.0) # Sprinkler Flowrate
c_sp3_q.set_writable()

# Define variables to the control area target  
control_q = control.add_variable(idx, "control_q", 0.0) # Control area flowrate
control_q.set_writable()
control_ir = control.add_variable(idx, "control_ir", 0.0) # Control area irrigation recommendation
control_ir.set_writable()

# Define Fuzzy area parameter
fuzzy = node.add_object(idx, "Fuzzy")

# Add variable to each of the 3 sprinklers for the Control Area 
f_sp1_open = fuzzy.add_variable(idx, "f_sp1_open", False) # Sprinkler open
f_sp1_open.set_writable()
f_sp1_q = fuzzy.add_variable(idx, "f_sp1_q", 0.0) # Sprinkler flowrate
f_sp1_q.set_writable()
f_sp2_open = fuzzy.add_variable(idx, "f_sp2_open", False) # Sprinkler open
f_sp2_open.set_writable()
f_sp2_q = fuzzy.add_variable(idx, "f_sp2_q", 0.0) # Sprinkler flowrate
f_sp2_q.set_writable()
f_sp3_open = fuzzy.add_variable(idx, "f_sp3_open", False) # Sprinkler open
f_sp3_open.set_writable()
f_sp3_q = fuzzy.add_variable(idx, "f_sp3_q", 0.0) # Sprinkler flowrate
f_sp3_q.set_writable()

# Define variables to the control area target  
fuzzy_q = fuzzy.add_variable(idx, "fuzzy_q", 0.0) # Fuzzy area flowrate
fuzzy_q.set_writable()
fuzzy_ir = fuzzy.add_variable(idx, "fuzzy_ir", 0.0) # Fuzzy area irrigation recommendation
fuzzy_ir.set_writable()


@uamethod
def irrigate_control(parent, mm_control): # mm_control is obtained using FAO recommendation or the farm`s decision
    if manualoperation.get_value() == False:
        # Open all valves for the control area. 
        c_sp1_open.set_value(True)
        c_sp2_open.set_value(True)
        c_sp3_open.set_value(True)
        # Open the pump if it is not open.
        pump_closed.set_value(False)
        pump_q.set_value(1) # This flowrate(l/s) is chosen based on project details. 
        # Set the irrigation recommendation for the day
        control_ir.set_value(mm_control)
        return ua.StatusCode(0)
    else:  
        return ua.StatusCode(0x80000000) # Status code for BadCOnditionDisable error

def irrigate_fuzzy(parent, mm_fuzzy): #mm_fuzzy is obtained using fuzzy logic from another master`s degree project
    if manualoperation.get_value() == False:
        # Open all valves for the Fuzzy area. 
        f_sp1_open.set_value(True)
        f_sp2_open.set_value(True)
        f_sp3_open.set_value(True)
        # Open the pump
        pump_closed.set_value(False)
        pump_q.set_value(1)
        # Set the irrigation recommendation for the day
        fuzzy_ir.set_value(mm_fuzzy)
        return ua.StatusCode(0)
    else:  
        return ua.StatusCode(0x80000000) # Status code for BadCOnditionDisable error

# Define manual control to close all valves and pump
def turn_all_off(parent):
    if manualoperation.get_value() == True:
        c_sp1_open.set_value(False)
        c_sp2_open.set_value(False)
        c_sp3_open.set_value(False)
        f_sp1_open.set_value(False)
        f_sp2_open.set_value(False)
        f_sp3_open.set_value(False)
        pump_closed.set_value(True)
        pump_q.set_value(0)
        return ua.StatusCode(0)
    else:  
        return ua.StatusCode(0x80000000) # Status code for BadCOnditionDisable error


# Define manual control to openall valves and pump
def turn_all_on(parent):
    if manualoperation.get_value() == True:
        c_sp1_open.set_value(True)
        c_sp2_open.set_value(True)
        c_sp3_open.set_value(True)
        f_sp1_open.set_value(True)
        f_sp2_open.set_value(True)
        f_sp3_open.set_value(True)
        pump_closed.set_value(False)
        pump_q.set_value(1)
        return ua.StatusCode(0)
    else:  
        return ua.StatusCode(0x80000000) # Status code for BadCOnditionDisable error
        

# Define manual control to open all sprinklers in Control Área
def turn_control_on(parent):
    if manualoperation.get_value() == True:
        c_sp1_open.set_value(True)
        c_sp2_open.set_value(True)
        c_sp3_open.set_value(True)
    else:  
        return ua.StatusCode(0x80000000) # Status code for BadCOnditionDisable error

# Define manual control to close all sprinklers in Control Área
def turn_control_off(parent):
    if manualoperation.get_value() == True:
        c_sp1_open.set_value(False)
        c_sp2_open.set_value(False)
        c_sp3_open.set_value(False)
    else:  
        return ua.StatusCode(0x80000000) # Status code for BadCOnditionDisable error

# Define manual control to open all sprinklers in Fuzzy Área
def turn_fuzzy_on(parent):
    if manualoperation.get_value() == True:
        f_sp1_open.set_value(True)
        f_sp2_open.set_value(True)
        f_sp3_open.set_value(True)
    else:  
        return ua.StatusCode(0x80000000) # Status code for BadCOnditionDisable error

# Define manual control to close all sprinklers in Fuzzy Área
def turn_fuzzy_off(paren):
    if manualoperation.get_value() == True:
        f_sp1_open.set_value(False)
        f_sp2_open.set_value(False)
        f_sp3_open.set_value(False)
    else:  
        return ua.StatusCode(0x80000000) # Status code for BadCOnditionDisable error

# Define Manual control to turn the pump ON
def turn_pump_on(parent):
    if manualoperation.get_value() == True:
        pump_closed.set_value(False)
        pump_q.set_value(1) # Flowrate defined in project implementation
    else:  
        return ua.StatusCode(0x80000000) # Status code for BadCOnditionDisable error

# Define Manual control to turn the pump OFF
def turn_pump_off(parent):
    if manualoperation.get_value() == True:
        pump_closed.set_value(True)
        pump_q.set_value(0) 
    else:  
        return ua.StatusCode(0x80000000) # Status code for BadCOnditionDisable error

#Define arguments for Irrigate Control and Irrigate Fuzzy Methods
# Define mm_control as an argument to the Irrigate Control Method
mm_control = ua.Argument()
mm_control.Name = "mm_control"
mm_control.DataType = ua.NodeId(ua.ObjectIds.Float)
mm_control.ValueRank = -1
mm_control.ArrayDemisions = []
mm_control.Description = ua.LocalizedText("Irrigation recommendation mm control")

# Define mm_fuzzy as an argument to the Irrigate Fuzzy Method
mm_fuzzy = ua.Argument()
mm_fuzzy.Name = "mm_fuzzy"
mm_fuzzy.DataType = ua.NodeId(ua.ObjectIds.Float)
mm_fuzzy.ValueRank = -1
mm_fuzzy.ArrayDemisions = []
mm_fuzzy.Description = ua.LocalizedText("Irrigation recommendation mm fuzzy")

# Define two folders automatic (to control irrigation by the IoT platform calculations) and manual (to control irrigation based on the farmers need)
automatic = server.nodes.objects.add_folder(idx,"Automatic")
manual = server.nodes.objects.add_folder(idx,"Manual")

# Define Automatic irrigation methods
automatic.add_method(idx, "irrigatecontrol", irrigate_control, [mm_control])
automatic.add_method(idx, "irrigatefuzzy", irrigate_fuzzy, [mm_fuzzy])

# Define manual irrigation methods
# This variable must be True in order for the manual method to work. 
manualoperation = manual.add_variable(idx, "manualoperation", False)
manualoperation.set_writable()
manual.add_method(idx, "turnalloff", turn_all_off)
manual.add_method(idx, "turnallon", turn_all_on)
manual.add_method(idx, "turncontrolon", turn_control_on)
manual.add_method(idx, "turncontroloff", turn_control_off)
manual.add_method(idx, "turnfuzzyon", irrigate_fuzzy)
manual.add_method(idx, "turnfuzzyoff", turn_fuzzy_off)
manual.add_method(idx, "turnpumpon", turn_pump_on)
manual.add_method(idx, "turnpumpoff", turn_pump_off)

# Starting the Server
server.start()
print("server is starting!")