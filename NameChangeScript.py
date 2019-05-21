from netmiko import Netmiko
from run_pandas import *


def name_change(dict):
##Loop over the nested dictionary (that should be its own class, just for tidier files.) Once its looped define the host name and 
#replace the 3- character prefix with the AD friendly 2-character prefix. The indents MUST stay as is, otherwise it will not loop properly
##for loops in python are similar to foreach loops in C# 
##K, V are for key and value 
    file= input("What is the name of the file?")
    f= open(file, 'r')
    cisco_sw={}
    cisco_sw['hosts']= {}
    for line in f:
        k,v= line.strip().split(',')
        cisco_sw['hosts'][k.strip()]= v.strip()
        f.close()
    print(cisco_sw)
    command= input("What commands would you like to execute?")
    for k, v in test_dict.items() :
        hostname=test_dict[k]['host']
        print (hostname)
        
        #commands = ["banner motd ~\n\tThis is a secure site.\n\tOnly authorized users allowed.\n\t"+
               # "For access please contact\n\tRockwood School District Technical Support."
               # f"\n\tCM \n\t"+ hostname.replace('CMS', 'CM')+"\n\t5/21/2019\r ~",
                #"hostname "+ hostname.replace('CMS', 'CM'),
                #"do wr me"]
        print(command)
        #connect to the switch using Netmiko. It is using k for key so it will go from 0 to the end for each entry
        try:
            net_connect= Netmiko(**test_dict[k])
            print(net_connect.find_prompt())
        #Send the commands as previously defined to the switch. This is from Netmiko
            output = net_connect.send_config_set(command)
        #These allow me to watch as the commands are sent. You will be able to see the session as it affects the switch
            print (output)
            print()
        except Exception:
            print(hostname.capitalize()+ " could not be reached")
            continue
    
