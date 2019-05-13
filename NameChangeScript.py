from netmiko import Netmiko
from getpass import getpass


password= "cisco"

CCL_Switches= {

    "CCL_2960_48_A_Rm1":{
    "ip": "10.82.8.21",
    "username": "cwadmin",
    "password": password,
    "device_type": "cisco_ios",
    "host": "CCL_2960_48_A_Rm1",
    },
"CCL_2960_48_B_Rm5":{
    "ip":"10.82.8.5",
    "username": "cwadmin",
    "password": password,
    "device_type": "cisco_ios",
    "host": "CCL_2960_48_B_Rm5",
    },
"CCL_2960_48_C_Rm10": {

    "ip":"10.82.8.10",
    "username": "cwadmin",
    "password": password,
    "device_type": "cisco_ios",
    "host": "CCL_2960_48_C_Rm10",
    } ,
"CCL_2960_48_D_Rm16": {
    "ip":"10.82.8.16",
    "username": "cwadmin",
    "password": password,
    "device_type": "cisco_ios",
    "host": "CCL_2960_48_D_Rm16",

    },
    
 "CCL_2960_48_E_Rm15": {
     "ip":"10.82.8.15",
    "username": "cwadmin",
    "password": password,
    "device_type": "cisco_ios",
    "host": "CCL_2960_48_E_Rm15",
     },
     "CCL_2960_48_F_Rm11": {
     "ip":"10.82.8.11",
    "username": "cwadmin",
    "password": password,
    "device_type": "cisco_ios",
    "host": "CCL_2960_48_F_Rm11",
     },
     "CCL_2960_48_H2_AV": {
     "ip":"10.82.8.26",
    "username": "cwadmin",
    "password": password,
    "device_type": "cisco_ios",
    "host": "CCL_2960_48_H2_AV",
     },
    "CCL_2960_48_H1_AV": {
     "ip":"10.82.8.25",
    "username": "cwadmin",
    "password": password,
    "device_type": "cisco_ios",
    "host": "CCL_2960_48_H1_AV",
     },
     "CCL_3560X-48P_MDF_G1": {
     "ip":"10.82.8.1",
    "username": "cwadmin",
    "password": password,
    "device_type": "cisco_ios",
    "host": "CCL_3560X-48P_MDF_G1",
     },
     "CCL_2960x_48PS_MDF": {
     "ip":"10.82.8.4",
    "username": "cwadmin",
    "password": password,
    "device_type": "cisco_ios",
    "host": "CCL_2960x_48PS_MDF",
     }
}

for k, v in CCL_Switches.items()  :
    hostname= CCL_Switches[k]['host']
    print (hostname)
    commands = ["banner motd ~\n\tThis is a secure site.\n\tOnly authorized users allowed.\n\t"+
                "For access please contact\n\tRockwood School District Technical Support."
                f"\n\tCCL \n\t"+ hostname.replace('CCL', 'CL')+"\n\t5/13/2019\r ~",
                "hostname "+ hostname.replace('CCL', 'CL'),
                "do wr me"]

    


    print(commands)
    net_connect= Netmiko(**CCL_Switches[k])
    print(net_connect.find_prompt())
    output = net_connect.send_config_set(commands)
    print (output)
    print()
