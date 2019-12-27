import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Something...."
body = "Hey there, how are you"
sender_email = "<#sendermail>" #From
receiver_email = "<#recieptentmail>" #To
password = '<#pass>' #Password

#header
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Adding body to email
message.attach(MIMEText(body, "plain"))

#Attachment path
filename = "test.txt"  

# Open file in binary mode
with open(filename, "rb") as attachment:
    # Adding file as application/octet-stream to make the file as downloadable 
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encoding file in ASCII characters to send by email    
encoders.encode_base64(part)

# Adding headers to attachment
part.add_header(
    "Content-Disposition", "attachment; filename= hola",
)

# Adding attachment to message
message.attach(part)

#converting message to string
text = message.as_string()

#connect to the server 
server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()#For security
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, text)
