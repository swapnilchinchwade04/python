# Design automation script which accept process name and display information of that process if
# it is running.
# Usage : CheckProcessInfo.py Notepad

from sys import argv
import psutil

def main():
    print("Automation Script to display information of running process.")
    print("Script Name:", argv[0])
    print("No of arguments:", len(argv))

    if len(argv) < 1 or len(argv) > 2:
        print("Invalid number of arguments.")
        print("Use -u for help.")
        print("Use -h for help.")

    if len(argv) == 2:
        if argv[1] == "-u" or argv[1] == "-U":
            print("Usage : ApplicationName")
            exit()
        if argv[1] == "-h" or argv[1] == "-H":
            print("Script ot display information of running process.")
            exit()

    if len(argv) == 2:
        try:
            flag = 0
            for proc in psutil.process_iter(['pid', 'name', 'username']):
                app_name = proc.info['name'].split(".")[0]
                #print("Proc name: ",proc.info['name'])
                #print("Argv name: ", app_name)
                if app_name == argv[1]:
                    #print("App name: ", app_name)
                    print(f"PID: {proc.info['pid']} - Name: {proc.info['name']} - User Name: {proc.info['username']}")
                    flag = 1
            if flag == 0:
                print("Process not found.")


        except Exception:
            print(Exception)


if __name__ == "__main__":
    main()