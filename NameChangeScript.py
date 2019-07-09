from netmiko import Netmiko
from run_pandas import *

def name_change():
##Loop over the nested dictionary (that should be its own class, just for tidier files.) Once its looped define the host name and 
#replace the 3- character prefix with the AD friendly 2-character prefix. The indents MUST stay as is, otherwise it will not loop properly
##for loops in python are similar to foreach loops in C# 
##K, V are for key and value 
   
    command=[]
    getCommands= True
    items={}
    items['hosts']= {}
   
    while getCommands==True: 
        getInput=input("Would you like to enter a command? Y or N")
        gotInput= getInput.upper()
        if gotInput== 'Y':
            cli= input("What command would you like to enter?")
            command.append(cli)
        else: 
            getCommands==False
            break
    items['hosts']=clean_Excel()
    print(items['hosts'])
    print()
    for k in items['hosts']:
        hostname=items['hosts'][k]['host']
        print (hostname)
        
        #commands = ["banner motd ~\n\tThis is a secure site.\n\tOnly authorized users allowed.\n\t"+
         #       "For access please contact\n\tRockwood School District Technical Support."
          #      f"\n\tEE \n\t"+ hostname.replace('ECE', 'EE')+"\n\t5/21/2019\r ~",
           #     "hostname "+ hostname.replace('ECE', 'EE'),
            #    "do wr me"]
        #connect to the switch using Netmiko. It is using k for key so it will go from 0 to the end for each entry
        try:
            net_connect= Netmiko(**items['hosts'][k])
            print(net_connect.find_prompt())
        #Send the commands as previously defined to the switch. This is from Netmiko
            output = net_connect.send_config_set(command)
        #These allow me to watch as the commands are sent. You will be able to see the session as it affects the switch
            print (output)
            print()
        except Exception:
           print(hostname.capitalize()+ " could not be reached")
           continue
    
