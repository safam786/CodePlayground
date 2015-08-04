import smtplib

username = 'sstrickler123@gmail.com' 
password = 'qwert123!!'

ttext = '12063989906@tmomail.net'
message = 'You medication is ready!'

msg = """From: %s
To: %s
Subject: text-message
%s""" % (username, ttext, message)

server = smtplib.SMTP("smtp.gmail.com", "587")
server.starttls()
server.login(username, password)

server.sendmail(username, ttext, msg)

#server.sendmail('sstrickler123@gmail.com','safam786@gmail.com','Hello!')
server.quit()
