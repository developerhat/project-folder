import smtplib
#SERVER = "localhost"

connection = smtplib.SMTP('smtp.gmail.com', 587)

connection.ehlo()

connection.starttls()

connection.login('pwgbusiness@gmail.com', 'M0neytalkss')

connection.sendmail('pwgbusiness@gmail.com', 'bprimer@wearexyz.com', 'Subject: Testing \n\n Dear Hello, \n, I am testing sending email with Python. It rocks! \n\n -Pat')

connection.quit()
