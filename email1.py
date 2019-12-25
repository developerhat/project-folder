import smtplib
#SERVER = "localhost"

FROM = 'pwgbusiness@gmail.com'
pas = 'M0neytalkss'
server.starttls()
server.login(FROM,pas)

TO = ["patrickwilliamgo@gmail.com"] # must be a list

SUBJECT = "Hello!"

TEXT = "This message was sent with Python's smtplib."

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP('smtp.gmail.com', 587)
server.sendmail(FROM, TO, message)
server.quit()
