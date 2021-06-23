import smtplib
import datetime
import smtpd

content = 'test' 

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()
mail.starttls()
mail.login('email', 'password')

mail.sendmail('Legele@aspira.hr', 'Legele@duje.hr', content)

mail.close()