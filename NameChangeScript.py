from netmiko import Netmiko
from getpass import getpass


password=getpass()

Switch_dictionary= {

    "sample_switch":{
    "ip": "ip add",
    "username": "username",
    "password": password,
    "device_type": "cisco_ios",
    "host": "hostname",
    },
     "sample_switch_2":{
    "ip": "ip add",
    "username": "username",
    "password": password,
    "device_type": "cisco_ios",
    "host": "hostname",
    }
}

for k, v in CCL_Switches.items()  :
    hostname= Switch_dictionary[k]['host']
    print (hostname)
    commands = ["banner motd ~\n\tThis is a secure site.\n\tOnly authorized users allowed.\n\t"+
                "For access please contact\n\t Technical Support."
                f"\n\tCCL \n\t"+ hostname.replace('CCL', 'CL')+"\n\t5/13/2019\r ~",
                "hostname "+ hostname.replace('CCL', 'CL'),
                "do wr me"]

    


    print(commands)
    net_connect= Netmiko(**Switch_dictionary[k])
    print(net_connect.find_prompt())
    output = net_connect.send_config_set(commands)
    print (output)
    print()
