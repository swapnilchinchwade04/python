from sys import *
import webbrowser
import re
import urllib.request
import urllib.error

def is_connected():
    try:
        urllib.request.urlopen("http://google.com", timeout=1)
        return True
    except urllib.error.URLError as err:
        #print(err.reason)
        return False

def Find(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(), ]|(?:%[0-9a-fA-F][0-9a-fA-F])+])+', string)
    #print("Url:", url)
    return url

def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            url = Find(line)
            #print(url)
            if len(url)>0:
                print("Line : ", line)
                for strl in url:
                    webbrowser.open_new_tab(strl)

def main():
    print("Automation Script for Web Launcher.")
    print("Application name :"+ argv[0])

    if len(argv)!=2:
        print("Invalid no.of arguments")
        exit()
    if argv[1]== "-h" or argv[1] == "-H":
        print("Script is used to open URL which are written in one file.")
        exit()
    if argv[1] == "-u" or argv[1] == "-U":
        print("Usage: ApplicationName Name_of_File")
        exit()

    try:
        connected = is_connected()
        if connected:
            #print("Connected")
            WebLauncher(argv[1])
        else:
            print("1Unable to connect to internet.")
    except ValueError:
        print("Error : Invalid datatype of inputs.")

    except Exception as err:
        print("Error : Invalid Input", err)


if __name__ == "__main__":
    main()
