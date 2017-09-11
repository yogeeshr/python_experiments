__author__ = "Yogeesh R"
__email__ = "yogeesh.srkvs@gmail.com"

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()

# HTML Content mail
filename = "../Visualtizations/population.html"
f = file(filename)
attachment = MIMEText(f.read(),'html')
msg.attach(attachment)

# Embed Image
attachment = '../Visualtizations/gender_population_compare.png'

msgText = MIMEText('<b>%s</b><br><img style="width:50%s%sborder:1px solid%s padding:10px%s border-radius:15px%s color:grey%s background-color:lightgrey" src="cid:%s"><br>' % ("", "%", ";", ";", ";", ";", ";",attachment), 'html')
msg.attach(msgText)
fp = open(attachment, 'rb')
img = MIMEImage(fp.read())
fp.close()
img.add_header('Content-ID', '<{}>'.format(attachment))
msg.attach(img)

# End Footer
msg.attach(MIMEText('--'))
msg.attach(MIMEText('Tx,\nYogeesh R'))

# Email send
msg['Subject'] = "Population Data"
msg['From'] = "Population Analysis"
msg['To'] = "yogeesh.srkvs@gmail.com"
msg['Cc'] = "yogeesh.srkvs@gmail.com"
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login("yogeesh.srkvs@gmail.com","<2 step verified app code / password>")
print "Mailing . . ."
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()