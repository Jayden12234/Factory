# Factory
Factory game made in python

To run/install
clone the folder Game into a python interputer
with an output file called out.txt
and run command: python3 Runner.py

dependices:
random: pip install random



Dev plans:

Map class:
handles display and storing the map
functions:
    __init__(self,conv_key,har_key,slm_key,mat_key,out_f) == intalize values
    map_gen(self)==add resource nodes to map
    write_val(self,pos,val)==writes a val to a postion
    output(self) == writes map to output file
variables:
    conv_key = convery key
    slm_key = semlter key
    res_key = resource key
    res = the only resource in game
Resource class:
handles what resource are in the node what rate of extraction
functions:
    __init__(self,map,pos,out_dic) intalives values
    write(self)=wries value to the map bases on it posistion
    add_conv(self,conv)=add the convery to output to 
    send_obj(self)=sends an obj(metal) to convery 
variables:
    map refers to the map class
    pos referes to the postion on the map
    out_dic referd to the fircetion it outputs
    conv is made in add_conv function if valid 
Coneyer class:
functions:
    __init__(self, pos,dic) inlaizes key values
    add_conv and next coveyer in line
    send_obj send the object to the next coneyer in line
variables:
    pos is it position on the map
    dic is dicretion it is pointing
    conv is the next coneyer in line
    obj is used to transfer objects 
selmter class:
function:
    __init__(self,pos,dic)
variables:
    pos position on map
    dic is dircetion of input output

 

Input class:

Sava_data class:
