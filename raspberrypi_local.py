import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# sender
email_address = "my.tasker.emailer@gmail.com"
# password of the sender
password = "wh1tec0llar2014"
# receiver
receiver_address = "fsaulean@gmail.com"

# uses a socket to get local ip address
my_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_sock.connect(("8.8.8.8", 80))
# local address of machine
local_address = my_sock.getsockname()[0]
my_sock.close()

# message for the email
msg = MIMEMultipart()

msg['From']=email_address
msg['To']=receiver_address
msg['Subject']=local_address

msg.attach(MIMEText('LOCAL ADDRESS', 'plain'))

# connects to smtplib server
server = smtplib.SMTP('SMTP.gmail.com', port=587)
server.starttls()
server.login(email_address, password)

# sends message
server.send_message(msg)
del msg