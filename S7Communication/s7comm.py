import snap7

IP = input("IP address of the machine where the PLC is running:")
RACK = 0
SLOT = 1

DB_Number = 1
Start_Address = 0
Size = 1

def s7comm():

    lamba_data = bytearray(1)
    lamba_data[0] = input("Enter the Bool True/False:")

    client = snap7.client.Client()
    client.connect(IP,RACK,SLOT)
    client.get_connected()

    cpu_info = client.get_cpu_info()
    print("CPU INFO:",cpu_info)

    cpu_state = client.get_cpu_state()
    print("CPU STATE:",cpu_state)

    db = client.db_read(DB_Number,Start_Address,Size)
    lamba = bool(db[0])
    print("lamba_state:",lamba)

    new_state = client.db_write(DB_Number,Start_Address,lamba_data)
    print("New Lamba_state:",new_state)

s7comm()