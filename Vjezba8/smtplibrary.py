import smtplib
import datetime
import smtpd
SERVER = 'localhost'
PORT = 8000
FROM = "Duje@aspira.hr"
TO = ["email@aspira.hr"]
SUBJECT = "test"
dt = datetime.datetime.now()
TEXT = "Vrijeme. @ " + str(dt)
message = """\
Salje: %s
Prima: %s
Predmet: %s
%s
""" % (FROM, ",".join(TO), SUBJECT, TEXT)
server = smtplib.SMTP(SERVER, PORT)
server.sendmail(FROM,TO,message)
server.quit()