import psutil

def check_cpu_threshold():
    cpu_threshold=int(input("Enter the cpu threshold"))

    current_cpu = psutil.cpu_percent(interval=1)
    print("current_cpu is ",current_cpu)
    if(current_cpu>cpu_threshold):
        print("CPU  EMAIL ALERT SENT....")
    else:
        print("CPU is in  safe state")
 

def check_virtualmemory():
    memory_threshold=int(input("Enter the memory threshold"))
    current_memory=psutil.virtual_memory().percent
    print("current memory is: ",current_memory)
    if(current_memory>memory_threshold):
        print("memory exceeded! ")
    else:
        print("Memory is available to use")


def check_disk():
    disk_threshold=int(input("Enter the disk threshold"))
    current_disk=psutil.disk_usage("/").percent
    print("current disk is: ",current_disk)
    if(current_disk>disk_threshold):
        print("disk exceeded! ")
    else:
        print("disk is available to use")


check_cpu_threshold() 
check_virtualmemory()
check_disk()       