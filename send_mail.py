import email, smtplib, ssl
import csv
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open('mail_list.csv', mode='r') as csv_file:  #opening receiptent list as csv_file 
    reader = csv.reader(csv_file, delimiter=',')
    mail_ad = []
    for row in reader:
        for n in row:
            mail_ad.append(n)

subject = "Something...."
body = "Hey there, how are you"
sender_email = "#" #From(replace # with your gmail address)
password = '#' #Password (replace # with your gmail password )

#header
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ','.join(mail_ad) 
message["Subject"] = subject

# Adding body to email
message.attach(MIMEText(body, "plain"))

#Attachment path
filename = "attachment.txt"  

# Open file in binary mode
with open(filename, "rb") as attachment:
    # Adding file as application/octet-stream to make the file as downloadable 
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encoding file in ASCII characters to send by email    
encoders.encode_base64(part)

# Adding headers to attachment
part.add_header(
    "Content-Disposition", "attachment; filename= hola.txt",
)

# Adding attachment to message
message.attach(part)

#converting message to string
text = message.as_string()

#connect to the server 
server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()#For security
server.login(sender_email, password)
server.sendmail(sender_email, mail_ad, text)
