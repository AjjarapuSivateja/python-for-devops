import psutil

def check_cpu_threshold():
    cpu_threshold=int(input("Enter the cpu threshold"))

    current_cpu = psutil.cpu_percent(interval=1)
    print("current_cpu is ",current_cpu)
    if(current_cpu>cpu_threshold):
        print("CPU  EMAIL ALERT SENT....")
    else:
        print("CPU is in  safe state")
check_cpu_threshold() 