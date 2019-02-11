# Get Your Pi's Local Address!
Send an email to your email address with the local address of your raspberry so that you don't have to use ethernet to connect to the raspberry pi.


```bash
git clone https://github.com/f-s-plus-plus/local_address_pi.git
cd local_address_pi
nano local_address_pi.py (or use your favroite text editor; better not be vim tho)
```


Change the receiver email address variable to your own email.

Example:

```python

import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# waits for 10 seconds so that the raspberry pi has enough time to get a local ip address
time.sleep(10)

# sender's email
sender_address = "my.tasker.emailer@gmail.com"
# password of the sender
password = "wh1tec0llar2014"
# receiver's email
receiver_address = "my.email@gmail.com"

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

```

Now in the cli: 

```bash
sudo nano /etc/rc.local
```

Add the line:
python3 /path/to/raspberry/local_address_pi/local_address_pi.py before exit 0


Note if the sender email address is not a gmail email, then you will have to change this line:
server = smtplib.SMTP('SMTP.gmail.com', port=587) 

Look at https://www.arclab.com/en/kb/email/list-of-smtp-and-pop3-servers-mailserver-list.html for more information
