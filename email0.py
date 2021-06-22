import smtplib
#SERVER = "localhost"

#This program works, but need to do it all in IDLE for some reason?

connection = smtplib.SMTP('smtp.gmail.com', 587)

connection.ehlo()

connection.starttls()

connection.login('pwgbusiness@gmail.com', 'M0neytalkss')

connection.sendmail('pwgbusiness@gmail.com', 'brittprimer@gmail.com', 'Subject: Testing \n\n Dear Hello, \n, I am testing sending email with Python. It rocks! \n\n -Pat')

connection.quit()
