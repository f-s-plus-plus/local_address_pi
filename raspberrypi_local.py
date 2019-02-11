import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# waits for 10 seconds so that the raspberry pi has enough time to get a local ip address
time.sleep(10)

# sender's email
sender_address = ""
# password of the sender
password = ""
# receiver's email
receiver_address = ""

# uses a socket to get local ip address
my_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_sock.connect(("8.8.8.8", 80))

# local address of machine
local_address = my_sock.getsockname()[0]

my_sock.close()

# message for the email
msg = MIMEMultipart()

msg['From'] = sender_address
msg['To'] = receiver_address
msg['Subject'] = local_address

msg.attach(MIMEText('LOCAL ADDRESS', 'plain'))

# connects to smtplib server
server = smtplib.SMTP('SMTP.gmail.com', port=587)
server.starttls()
server.login(email_address, password)

# sends message
server.send_message(msg)
