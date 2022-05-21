import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.login('pythonforbeginnerstest@gmail.com','rickandroll')
server.sendmail('pythonforbeginnerstest@gmail.com', 'u.mannepalli@gmail.com','this is a test message')
print('email sent')