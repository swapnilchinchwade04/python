# Design automation script which accept directory name and mail id from user and create log file in that
# directory which contains information of running processes as its name, PID, Username.
# After creating log file send that log file to the specified mail.
# Usage : ProcInfoLog.py Demo useremail@gmail.com
# Demo is name of Directory.
# useremail@gmail.com is the mail id

import os
import smtplib
from sys import *
import psutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def processinfolognotification(path, emailid):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
        exits = os.path.isdir(path)
        if exits:
            print("Path : " + path)
            file_name = "ProcessLogN.txt"
            with open(path + '\\'+file_name, 'a') as log_file:
                print("Filname:", file_name)
                log_file.write(f"PID   Name                 User Name " + "\n")
                for proc in psutil.process_iter(['pid', 'name', 'username']):
                    #print(f"PID: {proc.info['pid']} - Name: {proc.info['name']} - User Name: {proc.info['username']}")
                    data = f"{proc.info['pid']} - {proc.info['name']} - {proc.info['username']}"

                    log_file.write(data + "\n")

            # Email setup
            sender_email = "youremail@gmail.com"
            receiver_email = emailid
            password = ""  # Use an App Password for Gmail
            filename = path+'\\'+file_name  # File must exist in your directory

            # Create container
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = "Process Info Log File "
            message.attach(MIMEText("Body text", 'plain'))

            # Attachment handling
            try:
                with open(filename, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename= {filename}")
                message.attach(part)
            except FileNotFoundError:
                print(f"Error: {filename} not found.")

            # Send email
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                print("Sent!")
            except Exception as e:
                print(f"Error: {e}")
            finally:
                server.quit()



def main():
    print("Automation Script which accept directory name & stores information of running process in log file.")
    print("Script Name:", argv[0])
    print("No of arguments:", len(argv)-1)

    if len(argv) < 2 or len(argv) > 3:
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

    if len(argv) == 3:
        try:
            #print("IN", argv[1], argv[2])
            processinfolognotification(argv[1], argv[2])

        except Exception:
            print("Exception")
            print("Invalid number of arguments.")
            print("Use -u for help.")


if __name__ == "__main__":
    main()
