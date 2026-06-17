"""
Fake IoT Device Profile

This represents the device
our honeypot is pretending to be.
"""


DEVICE = {

    "name": "SmartCam X100",

    "type": "Security Camera",

    "firmware": "v1.0.3",

    "manufacturer": "IoT Vision Systems",

    "service": "Telnet",

    "port": 2323,

    "status": "Online"

}



def get_device_info():

    return DEVICE