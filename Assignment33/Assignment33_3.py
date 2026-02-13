'''
3. Add Actual Memory Allocation Feature
    memory usage of each process:
        RSS (Resident Set Size - actual RAM used)
        VMS (Virtual Memory)
        Memory Percentage
Requirement
Show:
    Top 10 memory consuming processes'''


import psutil
import sys
import os
import time
import schedule

def CreaateLog(FolderName):
    Border = "-"*50
    Ret = False

    Ret = os.path.exists(FolderName)
    if (Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable To create Folder")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for log file gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName  = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    
    fobj = open(FileName, "w")
    
    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Surveillance System------\n")
    fobj.write("---Log Created at : "+time.ctime()+"---\n")
    fobj.write(Border+"\n\n")

    fobj.write("---------------System Report----------------------\n")
    fobj.write(Border+"\n")

    # Process Log
    Data = ProcessScan()

    for info in Data:
        fobj.write("PID : %s\n" % info["pid"])
        fobj.write("Name : %s\n" % info["name"])
        fobj.write("Number of Threads : %s\n" % info["num_threads"])
        fobj.write("Number of files opened : %s\n" % info["open_files"])
        fobj.write("Memory usage Resident Set Size : %s\n" % info["RSS"])
        fobj.write("Memory usage Virtual Memory : %s\n" % info["VMS"])
        fobj.write("Memory Percentage : %s%\n" %info["Memory_Percent"])
        fobj.write(Border + "\n")
    
    fobj.write(Border+"\n")
    fobj.write("-----------------End of Log File------------------\n")
    fobj.write(Border+"\n")

def ProcessScan():
    listProcess = []
    # Warm up for CPU percent
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            open_file_count = len(proc.open_files())

        except psutil.AccessDenied:
            open_file_count = "Access Denied"
        
        except (psutil.NoSuchProcess, psutil.ZombieProcess):
            continue

        
        # Memory info
        mem_info = proc.memory_info()
        rss_mb = mem_info.rss / (1024 * 1024)
        vms_mb = mem_info.vms / (1024 * 1024)
        mem_percent = proc.memory_percent()

        
        try:
            info = {
                "pid": proc.pid,
                "name": proc.name(),
                "num_threads": proc.num_threads(),
                "open_files": open_file_count,
                "RSS": round(rss_mb, 2),
                "VMS": round(vms_mb, 2),
                "Memory_Percent": round(mem_percent, 2)
            }
            listProcess.append(info)

        except (psutil.NoSuchProcess , psutil.AccessDenied , psutil.ZombieProcess):
            pass
            
    return listProcess        

def main():
    Border = "-"*50
    print(Border)
    print("-----Marvellous Platform Surveillance System------")
    print(Border)

    if len(sys.argv) == 2:
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is use to: ")
            print("1: Create automatic logs")
            print("2: Execute perodically")
            print("3: send mail with the log")
            print("4: store information about Process Name")
            print("5: store information about PID")
            print("6: store information about \nNumber of Threads created by that process")
            print("7: store information about \nNumber of files opened")
            print("8: store information about \nMemory usage of each process")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : The timme in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
            
    # python Demo.py 5 Marvellous
    elif (len(sys.argv) == 3):
        # Apply the Scheduler
        schedule.every(int(sys.argv[1])).minutes.do(CreaateLog, sys.argv[2])

        print("Platform Surveillance System started successfully.")
        print("Directory created successfully with name : ", sys.argv[2])
        print("Time interval in minuts: ", sys.argv[1])
        print("Press Ctrl + C to stop the execution.")
        # Wait till abort
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        
        except KeyboardInterrupt:
                print("\nScheduler stopped by user.")
                print(Border)
                print("---------Thank you for using our script-----------")
                print(Border)
                sys.exit(0) 

    else:
        print("Invalid number of command line argument")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")


    print(Border)
    print("---------Thank you for using our script-----------")
    print(Border)



if __name__ == "__main__":
    main()