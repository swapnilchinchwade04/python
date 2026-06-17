from datetime import datetime
import os
import time
from sys import argv
import hashlib
import time
import schedule
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def sendmail(receiver_emailid, filename, start_time, file_count, duplicates_file_count):
    # Email setup
    sender_email = "youremail@gmail.com"
    receiver_email = receiver_emailid
    password = ""  # Use an App Password for Gmail
    #filename =  file_name  # File must exist in your directory

    # Create container
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Duplicate File Removal"
    message_body = ("\nStarting time of scanning: " + str(start_time) +
                   "\nTotal number of files scanned: " + str(file_count) +
                   "\nTotal number of duplicate files found:" + str(duplicates_file_count))
    message.attach(MIMEText(message_body, 'plain'))

    # Attachment handling
    try:
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename="+ os.path.basename(filename))
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


def removeduplicatefiles(folder_name, r_email):
    start_time=  datetime.now().strftime("%H:%M:%S")
    duplicates = {}
    e_flag = 0
    if folder_name:
        if os.path.isdir(folder_name):
            flag = os.path.isabs(folder_name)
            if os.listdir(folder_name) and flag == False:
                files = os.lstat(folder_name)
                dir_path = os.path.dirname(os.path.abspath(__file__))
                # print("Directory Path: " + dir_path)
                # print("File Count: ", len(files))
                # print("Start Time: ", start_time)
                file_count = 0
                duplicates_file_count = 0
                fdata = ''
                file_count = sum(1 for entry in os.scandir(folder_name) if entry.is_file())

                if len(files) > 1:
                    for folder_path, _, files in os.walk(folder_name):
                        for file in files:
                            file_path = os.path.join(folder_path, file)

                            file_hash = hashlib.sha256(open(os.path.join(folder_path, file), "rb").read()).hexdigest()
                            #print("File Path: ",file_path)
                            if file_hash in duplicates:
                                duplicates[file_hash].append(file_path)
                                fdata = fdata + file + "\n"
                                # x = datetime.now()
                                # with open(dir_path + "\\" + "LogApp-"+x.strftime("%d-%m-%Y-%H-%M")+".txt", "a") as log_file:
                                #     log_file.write(file + "\n")
                                #     #print("Log File Name: ",log_file.name)
                                if os.path.exists(file_path):
                                    os.remove(file_path)
                                    #print("File removed")
                                    e_flag = 1
                                    duplicates_file_count  = duplicates_file_count + 1

                            else:
                                duplicates[file_hash] = [file_path]
                    if e_flag == 1 and fdata!= '':
                        #print("Mail Sent.")
                        x = datetime.now()
                        with open(dir_path + "\\" + "LogApp-" + x.strftime("%d-%m-%Y-%H-%M") + ".txt", "a") as log_file:
                            log_file.write(fdata + "\n")

                        sendmail(r_email, log_file.name,start_time, file_count, duplicates_file_count)

        else:
            print("Directory not found.")


def main():
    s = time.time()
    print("Automation Application to removes duplicate files")
    print("Script Name:", argv[0])
    print("No of arguments:", len(argv)-1)


    if len(argv) > 4 or len(argv) < 1:
        print("Invalid number of arguments!")
        print("Use -u for usage.")
        print("Use -h for help")
        exit()

    if len(argv) == 2:
        if argv[1] == "-u" or argv[1] == "-U":
            print("Script is used to find duplicate files from directory & remove those duplicate files.")
            exit()
        if argv[1] == "-h" or argv[1] == "-H":
            print("Help: Name_of_Script Directory_Name File_Extension")
            exit()



    if len(argv) == 4:
        try :
            #schedule.every(int(argv[2])).minutes.do(removeduplicatefiles, argv[1])
            schedule.every(int(argv[2])).seconds.do(removeduplicatefiles, argv[1], argv[3])
            while True:
                schedule.run_pending()
                time.sleep(1)

            #removeduplicatefiles(argv[1])
        except Exception as e:
            print(e)
            print("Invalid number of arguments!")
            print("Use -u for usage.")



if __name__ == "__main__":
    main()
