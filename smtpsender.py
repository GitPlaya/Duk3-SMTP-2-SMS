import smtplib,ssl
import json

from colorama import init, Fore, Back, Style

init()

print(Fore.RED + """
██████╗░██╗░░░██╗██╗░░██╗███████╗░░░░░░░██████╗███╗░░░███╗████████╗██████╗░
██╔══██╗██║░░░██║██║░██╔╝██╔════╝░░░░░░██╔════╝████╗░████║╚══██╔══╝██╔══██╗
██║░░██║██║░░░██║█████═╝░█████╗░░█████╗╚█████╗░██╔████╔██║░░░██║░░░██████╔╝
██║░░██║██║░░░██║██╔═██╗░██╔══╝░░╚════╝░╚═══██╗██║╚██╔╝██║░░░██║░░░██╔═══╝░
██████╔╝╚██████╔╝██║░╚██╗███████╗░░░░░░██████╔╝██║░╚═╝░██║░░░██║░░░██║░░░░░
╚═════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝░░░░░░╚═════╝░╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝░░░░░ """)

print(Fore.BLUE +"DUK3J4m4l SMTP-2-SMS TOOL")
print("")
print(Fore.GREEN + "This tool is used to send bulk sms using smtp server")
print(Fore.GREEN + "It uses phone number + sim carrier@gateway system as email")
print(Fore.GREEN + "Please convert your leads.txt before usage")
print("")
print("")

#code for smtp details
print(Fore.LIGHTRED_EX)

smtp_server = input("Enter Smtp server: ")
port = input("Enter Smtp port: ")
smtp_user= input("Enter Smtp user: ")
sender_email =  input("Enter Sender email: ")
password = input("Type smtp password: ")

print("")
print("")
print(Fore.LIGHTMAGENTA_EX)

bank = input( "Name of bank: ")
text_message = input("Enter the text to send to victim and dont add scampage link yet: ")
link = input( "Enter link to scampage: ")

#code to collect list of leads

print("")
print("")

print(Fore.BLUE + "Now enter leads file")
filename=input( "Enter file name: ")

print("")
print("")

file = open(filename, 'r')
lines = file.readlines()
for index,line in enumerate(lines):
    receiver_email=("{}".format( line.strip()))
    
    message = f"""\
    Subject: {bank}
    {text_message} {link}."""

    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server, port) 
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print (receiver_email + " -- Sent")
    except Exception as ex:
        print (Fore.RED + receiver_email+ " -- Not Sent",ex)

print(Fore.GREEN)
input("DONE")
