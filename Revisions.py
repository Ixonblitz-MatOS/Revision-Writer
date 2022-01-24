from psutil import virtual_memory,disk_usage
from wmi import WMI
from cpuinfo import get_cpu_info
from platform import uname
from datetime import datetime
import os
from os import path
import ctypes, sys
global num
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
else:
    def RevisionWrite(notes):
        my_system = uname()
        c = WMI()
        my_sys = c.Win32_ComputerSystem()[0]
        pcname = my_system.node
        date = datetime
        cpus = get_cpu_info()['brand_raw']
        ram = virtual_memory()
        storage = disk_usage('C:/').total
        motherboard = my_sys.SystemFamily
        num = 1
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        if path.exists(desktop + "/Revisions"):
            print()
        else:
            os.mkdir(desktop + "/Revisions")
        if path.exists(path.abspath() + "/RevisionsNumber.txt"):
            with open(path.abspath() + "/RevisionsNumber.txt", 'r') as reader:

                num = reader.read()
                reader.close()
        filename = "Revision" + num + ".txt"
        Message = "Revision" + str(num) + "\n________________________________\n" \
                                        f"Date: {date}" \
                                        f"PC Name: {pcname}" \
                                        f"CPU: {cpus}" \
                                        f"RAM: {ram}" \
                                        f"Storage: {storage}" \
                                        f"Motherboard: {motherboard}" \
                                        f"________________________________" \
                                        f"Notes:" \
                                        f"{notes}"

        with open(desktop+f"/Revisions/{filename}", 'w+') as writer:
            writer.write(Message)
            writer.close()
        print("Complete, hit enter to exit")
        input()
        quit()
    Extra = input("Enter notes for revision: ")
    RevisionWrite(Extra)
